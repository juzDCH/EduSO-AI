"""Entrena y evalúa el clasificador de intenciones de EduSO AI.

Uso desde la raíz del proyecto:
    python -m src.train
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.preprocess import normalizar_texto


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "data" / "dataset.csv"
MODEL_PATH = ROOT / "models" / "modelo_nlp.joblib"
REPORTS_DIR = ROOT / "reports"
RANDOM_STATE = 42


def construir_pipeline() -> Pipeline:
    """Crea el flujo reproducible de TF-IDF seguido de Regresión Logística."""
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    preprocessor=normalizar_texto,
                    lowercase=False,
                    ngram_range=(1, 2),
                    sublinear_tf=True,
                ),
            ),
            (
                "clasificador",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )


def entrenar(dataset_path: Path = DATASET_PATH) -> dict:
    """Entrena con 80% de los datos, evalúa el 20% y guarda artefactos reales."""
    datos = pd.read_csv(dataset_path)
    columnas_requeridas = {"pregunta", "intencion"}
    if not columnas_requeridas.issubset(datos.columns):
        raise ValueError("dataset.csv debe incluir las columnas pregunta,intencion")

    datos = datos.dropna(subset=["pregunta", "intencion"]).copy()
    datos["pregunta"] = datos["pregunta"].astype(str).str.strip()
    datos["intencion"] = datos["intencion"].astype(str).str.strip()
    datos = datos[(datos["pregunta"] != "") & (datos["intencion"] != "")]
    datos = datos.drop_duplicates(subset=["pregunta", "intencion"])

    conteo = datos["intencion"].value_counts()
    if len(conteo) < 2 or conteo.min() < 2:
        raise ValueError("Se necesitan al menos dos intenciones y dos ejemplos por intención.")

    preguntas_entrenamiento, preguntas_prueba, etiquetas_entrenamiento, etiquetas_prueba = (
        train_test_split(
            datos["pregunta"],
            datos["intencion"],
            test_size=0.20,
            random_state=RANDOM_STATE,
            stratify=datos["intencion"],
        )
    )

    modelo = construir_pipeline()
    modelo.fit(preguntas_entrenamiento, etiquetas_entrenamiento)
    predicciones = modelo.predict(preguntas_prueba)

    etiquetas = sorted(datos["intencion"].unique().tolist())
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

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(modelo, MODEL_PATH)
    pd.DataFrame(matriz, index=etiquetas, columns=etiquetas).to_csv(
        REPORTS_DIR / "matriz_confusion.csv", index_label="real"
    )
    muestra = datos.head(10).copy()
    muestra["texto_limpio"] = muestra["pregunta"].map(normalizar_texto)
    muestra.to_csv(REPORTS_DIR / "muestra_preprocesamiento.csv", index=False)

    try:
        dataset_label = str(dataset_path.relative_to(ROOT))
    except ValueError:
        dataset_label = str(dataset_path)

    metricas = {
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "dataset": dataset_label,
        "total_ejemplos": int(len(datos)),
        "ejemplos_entrenamiento": int(len(preguntas_entrenamiento)),
        "ejemplos_prueba": int(len(preguntas_prueba)),
        "semilla": RANDOM_STATE,
        "proporcion_prueba": 0.20,
        "intenciones": etiquetas,
        "ejemplos_por_intencion": {str(k): int(v) for k, v in conteo.sort_index().items()},
        "accuracy": float(accuracy_score(etiquetas_prueba, predicciones)),
        "precision_macro": float(precision_macro),
        "recall_macro": float(recall_macro),
        "f1_macro": float(f1_macro),
        "reporte_por_intencion": informe,
        "modelo": str(MODEL_PATH.relative_to(ROOT)),
        "nota": "Métricas calculadas sobre el conjunto de prueba separado; no son resultados de validación externa.",
    }
    (REPORTS_DIR / "metricas.json").write_text(
        json.dumps(metricas, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return metricas


def main() -> None:
    parser = argparse.ArgumentParser(description="Entrena y evalúa el clasificador de EduSO AI.")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH, help="Ruta al dataset CSV")
    args = parser.parse_args()
    metricas = entrenar(args.dataset.resolve())
    print("Entrenamiento completado")
    print(f"Ejemplos: {metricas['total_ejemplos']} ({metricas['ejemplos_entrenamiento']} train / {metricas['ejemplos_prueba']} prueba)")
    print(f"Accuracy: {metricas['accuracy']:.3f}")
    print(f"Precision macro: {metricas['precision_macro']:.3f}")
    print(f"Recall macro: {metricas['recall_macro']:.3f}")
    print(f"F1 macro: {metricas['f1_macro']:.3f}")
    print(f"Modelo guardado en: {MODEL_PATH.relative_to(ROOT)}")
    print(f"Métricas guardadas en: {(REPORTS_DIR / 'metricas.json').relative_to(ROOT)}")


if __name__ == "__main__":
    main()

