"""Carga el modelo entrenado y clasifica preguntas en español."""

from __future__ import annotations

from pathlib import Path

import joblib


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_PATH = ROOT / "models" / "modelo_nlp.joblib"


class PredictorIntenciones:
    """Interfaz pequeña para integrar el modelo con el tutor de Streamlit."""

    def __init__(self, model_path: Path = DEFAULT_MODEL_PATH) -> None:
        if not model_path.exists():
            raise FileNotFoundError(
                f"No se encontró {model_path}. Ejecuta primero: python -m src.train"
            )
        self.modelo = joblib.load(model_path)

    def predecir(self, pregunta: str) -> dict[str, str | float]:
        texto = pregunta.strip()
        if not texto:
            raise ValueError("Escribe una pregunta antes de clasificarla.")

        intencion = str(self.modelo.predict([texto])[0])
        probabilidades = self.modelo.predict_proba([texto])[0]
        confianza = float(max(probabilidades))
        return {"intencion": intencion, "confianza": confianza}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Clasifica una pregunta de Sistemas Operativos.")
    parser.add_argument("pregunta", help="Pregunta escrita por el estudiante")
    args = parser.parse_args()
    resultado = PredictorIntenciones().predecir(args.pregunta)
    print(f"Intención: {resultado['intencion']}")
    print(f"Confianza: {resultado['confianza']:.1%}")

