"""Entrena, evalúa y documenta el clasificador de intenciones de EduSO AI.

El flujo es reproducible desde la raíz del proyecto:

    python -m src.train

Genera el modelo de producción y todos los artefactos de evaluación en
``reports/`` (métricas, matriz de confusión, comparación de modelos, análisis
del umbral de confianza y palabras con más peso por tema).
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_predict,
    cross_val_score,
    train_test_split,
)
from sklearn.pipeline import FeatureUnion, Pipeline

from src.preprocess import normalizar_texto


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "data" / "dataset.csv"
NEGATIVOS_PATH = ROOT / "data" / "ejemplos_fuera_de_tema.csv"
SONDAS_PATH = ROOT / "data" / "sondas_fuera_de_tema.csv"
INTENCION_RECHAZO = "otros"
MODEL_PATH = ROOT / "models" / "modelo_nlp.joblib"
REPORTS_DIR = ROOT / "reports"
RANDOM_STATE = 42
UMBRALES_CANDIDATOS = (0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70)
COBERTURA_MINIMA = 0.85
ACEPTACION_FUERA_MAXIMA = 0.10
ACIERTO_MINIMO = 0.90


def construir_vectorizador(usar_caracteres: bool = True) -> FeatureUnion | TfidfVectorizer:
    """Vectorizador TF-IDF de palabras y, opcionalmente, de fragmentos de caracteres."""
    palabras = TfidfVectorizer(
        preprocessor=normalizar_texto,
        lowercase=False,
        ngram_range=(1, 2),
        sublinear_tf=True,
        min_df=1,
    )
    if not usar_caracteres:
        return palabras
    caracteres = TfidfVectorizer(
        preprocessor=normalizar_texto,
        lowercase=False,
        analyzer="char_wb",
        ngram_range=(3, 5),
        sublinear_tf=True,
        min_df=2,
    )
    return FeatureUnion(
        [("palabras", palabras), ("caracteres", caracteres)],
        transformer_weights={"palabras": 1.0, "caracteres": 0.7},
    )


def construir_pipeline(usar_caracteres: bool = True) -> Pipeline:
    """Flujo TF-IDF + Regresión Logística, con probabilidades interpretables."""
    return Pipeline(
        [
            ("vectorizador", construir_vectorizador(usar_caracteres)),
            (
                "clasificador",
                LogisticRegression(
                    max_iter=2000,
                    class_weight="balanced",
                    C=4.0,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )


MODELOS_CANDIDATOS = {
    "tfidf_palabras_lr": lambda: construir_pipeline(usar_caracteres=False),
    "tfidf_palabras_caracteres_lr": lambda: construir_pipeline(usar_caracteres=True),
}


def cargar_datos(
    dataset_path: Path = DATASET_PATH,
    negativos_path: Path | None = NEGATIVOS_PATH,
) -> pd.DataFrame:
    """Lee, limpia y valida el dataset educativo más la clase de rechazo.

    ``dataset.csv`` contiene las cinco intenciones educativas. Los ejemplos de
    ``ejemplos_fuera_de_tema.csv`` se etiquetan como ``otros`` para que el tutor
    aprenda a rechazar preguntas que no pertenecen a la materia. Las sondas de
    ``sondas_fuera_de_tema.csv`` nunca se entrenan: solo se usan para revisar el
    umbral de confianza.
    """
    datos = pd.read_csv(dataset_path, encoding="utf-8")
    columnas_requeridas = {"pregunta", "intencion"}
    if not columnas_requeridas.issubset(datos.columns):
        raise ValueError("dataset.csv debe incluir las columnas pregunta,intencion")

    piezas = [datos[["pregunta", "intencion"]]]
    if negativos_path is not None and negativos_path.exists():
        negativos = pd.read_csv(negativos_path, encoding="utf-8")
        if "pregunta" not in negativos.columns:
            raise ValueError("ejemplos_fuera_de_tema.csv debe incluir la columna pregunta")
        piezas.append(
            pd.DataFrame(
                {
                    "pregunta": negativos["pregunta"],
                    "intencion": INTENCION_RECHAZO,
                }
            )
        )
    datos = pd.concat(piezas, ignore_index=True)

    datos = datos.dropna(subset=["pregunta", "intencion"]).copy()
    datos["pregunta"] = datos["pregunta"].astype(str).str.strip()
    datos["intencion"] = datos["intencion"].astype(str).str.strip()
    datos = datos[(datos["pregunta"] != "") & (datos["intencion"] != "")]
    datos = datos.drop_duplicates(subset=["pregunta"])

    conteo = datos["intencion"].value_counts()
    if len(conteo) < 2 or conteo.min() < 2:
        raise ValueError("Se necesitan al menos dos intenciones y dos ejemplos por intención.")
    if len(datos) < 50:
        raise ValueError(
            "El dataset debe tener al menos 50 ejemplos para el prototipo académico."
        )
    return datos


def cargar_sondas(sondas_path: Path | None = SONDAS_PATH) -> list[str]:
    """Preguntas fuera de tema usadas solo para revisar el umbral de confianza."""
    if sondas_path is None or not sondas_path.exists():
        return []
    sondas = pd.read_csv(sondas_path, encoding="utf-8")
    if "pregunta" not in sondas.columns:
        return []
    return [str(texto).strip() for texto in sondas["pregunta"].dropna() if str(texto).strip()]


def evaluar_umbral(
    probabilidades_cv: np.ndarray,
    clases: np.ndarray,
    etiquetas: pd.Series,
    probabilidades_fuera: np.ndarray,
) -> dict:
    """Mide cobertura y rechazo de preguntas fuera de tema para cada umbral.

    Una pregunta se considera respondida solo si la clase predicha no es
    ``otros`` y la confianza alcanza el umbral. Así el análisis refleja lo que
    realmente hará ``ServicioTutor``.
    """
    confianza = probabilidades_cv.max(axis=1)
    prediccion = clases[probabilidades_cv.argmax(axis=1)]
    es_educativa = (etiquetas.to_numpy() != INTENCION_RECHAZO)
    aciertos = prediccion == etiquetas.to_numpy()

    confianza_fuera = (
        probabilidades_fuera.max(axis=1) if len(probabilidades_fuera) else np.array([])
    )
    prediccion_fuera = (
        clases[probabilidades_fuera.argmax(axis=1)]
        if len(probabilidades_fuera)
        else np.array([])
    )

    filas = []
    for umbral in UMBRALES_CANDIDATOS:
        respondidas = es_educativa & (prediccion != INTENCION_RECHAZO) & (confianza >= umbral)
        cobertura = (
            float(respondidas.sum() / es_educativa.sum()) if es_educativa.any() else 0.0
        )
        acierto_respondidas = (
            float(aciertos[respondidas].mean()) if respondidas.any() else 0.0
        )
        if len(confianza_fuera):
            aceptacion_fuera = float(
                ((prediccion_fuera != INTENCION_RECHAZO) & (confianza_fuera >= umbral)).mean()
            )
        else:
            aceptacion_fuera = 0.0
        filas.append(
            {
                "umbral": umbral,
                "cobertura": cobertura,
                "acierto_entre_respondidas": acierto_respondidas,
                "aceptacion_fuera_de_tema": aceptacion_fuera,
            }
        )

    elegibles = [
        fila
        for fila in filas
        if fila["cobertura"] >= COBERTURA_MINIMA
        and fila["acierto_entre_respondidas"] >= ACIERTO_MINIMO
        and fila["aceptacion_fuera_de_tema"] <= ACEPTACION_FUERA_MAXIMA
    ]
    recomendado = min((fila["umbral"] for fila in elegibles), default=0.35)
    return {
        "candidatos": filas,
        "recomendado": recomendado,
        "criterio": (
            f"Menor umbral con cobertura >= {COBERTURA_MINIMA:.0%}, acierto entre "
            f"respuestas >= {ACIERTO_MINIMO:.0%} y aceptación de fuera de tema "
            f"<= {ACEPTACION_FUERA_MAXIMA:.0%}."
        ),
        "sondas_fuera_de_tema": int(len(probabilidades_fuera)),
    }


def _top_palabras_por_tema(modelo: Pipeline, limite: int = 10) -> pd.DataFrame:
    """Extrae las palabras con mayor peso positivo para cada intención."""
    vectorizador = modelo.named_steps["vectorizador"]
    if isinstance(vectorizador, FeatureUnion):
        vocabulario = vectorizador.transformer_list[0][1].get_feature_names_out()
    else:
        vocabulario = vectorizador.get_feature_names_out()
    coeficientes = modelo.named_steps["clasificador"].coef_
    filas = []
    for indice_clase, clase in enumerate(modelo.classes_):
        pesos = coeficientes[indice_clase][: len(vocabulario)]
        mejores = pesos.argsort()[::-1][:limite]
        for posicion, indice in enumerate(mejores, start=1):
            filas.append(
                {
                    "intencion": str(clase),
                    "posicion": posicion,
                    "palabra": str(vocabulario[indice]),
                    "peso": float(pesos[indice]),
                }
            )
    return pd.DataFrame(filas)


def entrenar(
    dataset_path: Path = DATASET_PATH,
    model_path: Path = MODEL_PATH,
    reports_dir: Path = REPORTS_DIR,
    negativos_path: Path | None = NEGATIVOS_PATH,
    sondas_path: Path | None = SONDAS_PATH,
) -> dict:
    """Evalúa con holdout y validación cruzada, y guarda el modelo final."""
    datos = cargar_datos(dataset_path, negativos_path)
    etiquetas = sorted(datos["intencion"].unique().tolist())
    conteo = datos["intencion"].value_counts().sort_index()

    preguntas_entrenamiento, preguntas_prueba, etiquetas_entrenamiento, etiquetas_prueba = (
        train_test_split(
            datos["pregunta"],
            datos["intencion"],
            test_size=0.20,
            random_state=RANDOM_STATE,
            stratify=datos["intencion"],
        )
    )

    pliegues = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    comparacion = []
    for nombre, fabrica in MODELOS_CANDIDATOS.items():
        modelo = fabrica()
        puntajes_f1 = cross_val_score(
            modelo, datos["pregunta"], datos["intencion"], cv=pliegues, scoring="f1_macro"
        )
        puntajes_exactitud = cross_val_score(
            modelo, datos["pregunta"], datos["intencion"], cv=pliegues, scoring="accuracy"
        )
        comparacion.append(
            {
                "modelo": nombre,
                "f1_macro_media": float(puntajes_f1.mean()),
                "f1_macro_desviacion": float(puntajes_f1.std()),
                "accuracy_media": float(puntajes_exactitud.mean()),
            }
        )
    comparacion.sort(key=lambda fila: fila["f1_macro_media"], reverse=True)
    elegido = comparacion[0]["modelo"]

    modelo_evaluado = MODELOS_CANDIDATOS[elegido]()
    modelo_evaluado.fit(preguntas_entrenamiento, etiquetas_entrenamiento)
    predicciones = modelo_evaluado.predict(preguntas_prueba)

    precision_macro, recall_macro, f1_macro, _ = precision_recall_fscore_support(
        etiquetas_prueba, predicciones, average="macro", zero_division=0
    )
    matriz = confusion_matrix(etiquetas_prueba, predicciones, labels=etiquetas)
    informe = classification_report(
        etiquetas_prueba,
        predicciones,
        labels=etiquetas,
        output_dict=True,
        zero_division=0,
    )

    # Modelo de producción: se reentrena con todos los ejemplos disponibles
    # después de haber medido el rendimiento con el holdout.
    modelo_final = MODELOS_CANDIDATOS[elegido]()
    modelo_final.fit(datos["pregunta"], datos["intencion"])

    probabilidades_cv = cross_val_predict(
        MODELOS_CANDIDATOS[elegido](),
        datos["pregunta"],
        datos["intencion"],
        cv=pliegues,
        method="predict_proba",
    )
    sondas = cargar_sondas(sondas_path)
    probabilidades_fuera = (
        modelo_final.predict_proba(sondas) if sondas else np.empty((0, len(etiquetas)))
    )
    analisis_umbral = evaluar_umbral(
        probabilidades_cv,
        modelo_final.classes_,
        datos["intencion"],
        probabilidades_fuera,
    )

    model_path.parent.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(modelo_final, model_path)
    pd.DataFrame(matriz, index=etiquetas, columns=etiquetas).to_csv(
        reports_dir / "matriz_confusion.csv", index_label="real", encoding="utf-8"
    )
    pd.DataFrame(comparacion).to_csv(
        reports_dir / "comparacion_modelos.csv", index=False, encoding="utf-8"
    )
    pd.DataFrame(analisis_umbral["candidatos"]).to_csv(
        reports_dir / "umbral.csv", index=False, encoding="utf-8"
    )
    _top_palabras_por_tema(modelo_final).to_csv(
        reports_dir / "palabras_por_tema.csv", index=False, encoding="utf-8"
    )
    muestra = datos.head(10).copy()
    muestra["texto_limpio"] = muestra["pregunta"].map(normalizar_texto)
    muestra.to_csv(reports_dir / "muestra_preprocesamiento.csv", index=False, encoding="utf-8")

    errores = pd.DataFrame(
        {
            "pregunta": preguntas_prueba.to_numpy(),
            "intencion_real": etiquetas_prueba.to_numpy(),
            "intencion_predicha": predicciones,
        }
    )
    errores = errores[errores["intencion_real"] != errores["intencion_predicha"]]
    errores.to_csv(reports_dir / "errores_holdout.csv", index=False, encoding="utf-8")

    try:
        dataset_label = str(dataset_path.relative_to(ROOT))
    except ValueError:
        dataset_label = str(dataset_path)
    try:
        model_label = str(model_path.relative_to(ROOT))
    except ValueError:
        model_label = str(model_path)

    metricas = {
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "dataset": dataset_label,
        "total_ejemplos": int(len(datos)),
        "ejemplos_entrenamiento": int(len(preguntas_entrenamiento)),
        "ejemplos_prueba": int(len(preguntas_prueba)),
        "semilla": RANDOM_STATE,
        "proporcion_prueba": 0.20,
        "intenciones": etiquetas,
        "ejemplos_por_intencion": {str(k): int(v) for k, v in conteo.items()},
        "validacion_cruzada": {
            "pliegues": 5,
            "modelo": elegido,
            "f1_macro_media": comparacion[0]["f1_macro_media"],
            "f1_macro_desviacion": comparacion[0]["f1_macro_desviacion"],
            "accuracy_media": comparacion[0]["accuracy_media"],
        },
        "comparacion_modelos": comparacion,
        "modelo_elegido": elegido,
        "accuracy": float(accuracy_score(etiquetas_prueba, predicciones)),
        "precision_macro": float(precision_macro),
        "recall_macro": float(recall_macro),
        "f1_macro": float(f1_macro),
        "reporte_por_intencion": informe,
        "umbral": analisis_umbral,
        "modelo": model_label,
        "nota": (
            "Métricas de holdout y validación cruzada sobre el dataset propio; "
            "no son validación externa ni miden aprendizaje de estudiantes."
        ),
    }
    (reports_dir / "metricas.json").write_text(
        json.dumps(metricas, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return metricas


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Entrena y evalúa el clasificador de EduSO AI."
    )
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH, help="Ruta al dataset CSV")
    parser.add_argument("--modelo", type=Path, default=MODEL_PATH, help="Ruta del modelo de salida")
    parser.add_argument(
        "--reportes", type=Path, default=REPORTS_DIR, help="Carpeta de artefactos de evaluación"
    )
    args = parser.parse_args()
    metricas = entrenar(
        args.dataset.resolve(), args.modelo.resolve(), args.reportes.resolve()
    )
    print("Entrenamiento completado")
    print(
        f"Ejemplos: {metricas['total_ejemplos']} "
        f"({metricas['ejemplos_entrenamiento']} train / {metricas['ejemplos_prueba']} prueba)"
    )
    print(f"Modelo elegido: {metricas['modelo_elegido']}")
    print(
        "Validación cruzada (5 pliegues): "
        f"F1 macro {metricas['validacion_cruzada']['f1_macro_media']:.3f} "
        f"± {metricas['validacion_cruzada']['f1_macro_desviacion']:.3f}"
    )
    print(f"Holdout accuracy: {metricas['accuracy']:.3f}")
    print(f"Holdout F1 macro: {metricas['f1_macro']:.3f}")
    print(f"Umbral de confianza recomendado: {metricas['umbral']['recomendado']:.2f}")
    print(f"Modelo guardado en: {metricas['modelo']}")
    print(f"Métricas guardadas en: {(args.reportes / 'metricas.json')}")


if __name__ == "__main__":
    main()
