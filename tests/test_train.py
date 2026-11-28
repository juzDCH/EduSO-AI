"""Prueba de extremo a extremo del entrenamiento con un dataset pequeño."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import joblib
import pandas as pd

from src.train import entrenar


def _dataset_sintetico(ruta: Path) -> None:
    filas = []
    temas = {
        "procesos": [
            "¿Qué es un proceso?",
            "¿Cuáles son los estados de un proceso?",
            "¿Qué es el planificador de procesos?",
            "¿Qué es un cambio de contexto?",
            "¿Qué es un proceso zombi?",
            "¿Qué es un hilo?",
            "¿Qué es el bloque de control de proceso?",
            "¿Qué es un proceso listo?",
            "¿Qué es un proceso en espera?",
            "¿Qué es la multitarea?",
            "¿Qué es un proceso hijo?",
            "¿Qué es el despacho de procesos?",
            "¿Qué es la exclusión mutua?",
            "¿Qué es un semáforo?",
            "¿Qué es la inanición?",
            "¿Qué es el interbloqueo?",
            "¿Qué es un proceso huérfano?",
            "¿Qué es la concurrencia?",
            "¿Qué es un PID?",
            "¿Qué es un proceso ligero?",
        ],
        "memoria": [
            "¿Qué es la memoria RAM?",
            "¿Qué es la memoria virtual?",
            "¿Qué es la paginación?",
            "¿Qué es un fallo de página?",
            "¿Qué es la fragmentación interna?",
            "¿Qué es la memoria caché?",
            "¿Qué es la MMU?",
            "¿Qué es la tabla de páginas?",
            "¿Qué es el swapping?",
            "¿Qué es el thrashing?",
            "¿Qué es el heap?",
            "¿Qué es la pila?",
            "¿Qué es la memoria compartida?",
            "¿Qué es una dirección física?",
            "¿Qué es el reemplazo de páginas?",
            "¿Qué es la memoria no volátil?",
            "¿Qué es el bus de memoria?",
            "¿Qué es la latencia de memoria?",
            "¿Qué es la memoria de solo lectura?",
            "¿Qué es la asignación dinámica?",
        ],
        "kernel": [
            "¿Qué es el kernel?",
            "¿Qué es una llamada al sistema?",
            "¿Qué es una interrupción?",
            "¿Qué es un driver?",
            "¿Qué es el modo usuario?",
            "¿Qué es el espacio del kernel?",
            "¿Qué es un microkernel?",
            "¿Qué es un módulo del kernel?",
            "¿Qué es el arranque del sistema?",
            "¿Qué es el planificador del kernel?",
            "¿Qué es un demonio?",
            "¿Qué es POSIX?",
            "¿Qué es el búfer del kernel?",
            "¿Qué es un hilo del kernel?",
            "¿Qué es la protección de memoria?",
            "¿Qué es una interrupción de software?",
            "¿Qué es el gestor de dispositivos?",
            "¿Qué es el registro del sistema?",
            "¿Qué es la multitarea preventiva?",
            "¿Qué es el API del sistema operativo?",
        ],
    }
    for intencion, preguntas in temas.items():
        for pregunta in preguntas:
            filas.append({"pregunta": pregunta, "intencion": intencion})
    pd.DataFrame(filas).to_csv(ruta, index=False, encoding="utf-8")


class PruebasEntrenamiento(unittest.TestCase):
    def test_entrenamiento_genera_artefactos(self) -> None:
        with tempfile.TemporaryDirectory() as carpeta:
            base = Path(carpeta)
            dataset = base / "dataset.csv"
            _dataset_sintetico(dataset)
            modelo = base / "modelo.joblib"
            reportes = base / "reports"

            metricas = entrenar(
                dataset_path=dataset,
                model_path=modelo,
                reports_dir=reportes,
                negativos_path=None,
                sondas_path=None,
            )

            self.assertEqual(metricas["total_ejemplos"], 60)
            self.assertIn("validacion_cruzada", metricas)
            self.assertIn("umbral", metricas)
            self.assertTrue(0.0 <= metricas["accuracy"] <= 1.0)
            self.assertTrue(modelo.exists())
            for nombre in (
                "metricas.json",
                "matriz_confusion.csv",
                "comparacion_modelos.csv",
                "umbral.csv",
                "palabras_por_tema.csv",
                "muestra_preprocesamiento.csv",
            ):
                self.assertTrue((reportes / nombre).exists(), nombre)

            guardado = json.loads((reportes / "metricas.json").read_text(encoding="utf-8"))
            self.assertEqual(guardado["total_ejemplos"], 60)

            cargado = joblib.load(modelo)
            prediccion = cargado.predict(["¿Qué es un proceso?"])[0]
            self.assertEqual(prediccion, "procesos")


if __name__ == "__main__":
    unittest.main()
