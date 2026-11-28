"""Pruebas del servicio del tutor con un predictor simulado y con el modelo real."""

from __future__ import annotations

import unittest
from pathlib import Path

from src.services.tutor import (
    PreguntaInvalidaError,
    ServicioTutor,
)
from src.train import MODEL_PATH


class PredictorFalso:
    """Predictor controlado para probar el flujo sin cargar el modelo."""

    def __init__(self, intencion: str, confianza: float) -> None:
        self.intencion = intencion
        self.confianza = confianza

    def predecir(self, pregunta: str) -> dict[str, str | float]:
        return {"intencion": self.intencion, "confianza": self.confianza}


class PruebasServicioTutor(unittest.TestCase):
    def test_respuesta_con_alta_confianza(self) -> None:
        servicio = ServicioTutor(predictor=PredictorFalso("procesos", 0.90))
        respuesta = servicio.responder("¿Qué es un proceso?")
        self.assertFalse(respuesta.requiere_reformular)
        self.assertEqual(respuesta.intencion, "procesos")
        datos = respuesta.a_dict()
        for clave in (
            "pregunta",
            "intencion",
            "confianza",
            "titulo",
            "explicacion",
            "analogia",
            "ejemplo",
            "pregunta_comprobacion",
            "requiere_reformular",
        ):
            self.assertIn(clave, datos)

    def test_baja_confianza_pide_reformular(self) -> None:
        servicio = ServicioTutor(predictor=PredictorFalso("memoria", 0.10))
        respuesta = servicio.responder("algo confuso")
        self.assertTrue(respuesta.requiere_reformular)
        self.assertIsNone(respuesta.intencion)
        self.assertEqual(respuesta.intencion_sugerida, "memoria")

    def test_pregunta_fuera_de_tema(self) -> None:
        servicio = ServicioTutor(predictor=PredictorFalso("otros", 0.90))
        respuesta = servicio.responder("¿Cuál es la capital de Francia?")
        self.assertTrue(respuesta.requiere_reformular)
        self.assertIn("Sistemas Operativos", respuesta.explicacion)

    def test_pregunta_vacia_o_larga(self) -> None:
        servicio = ServicioTutor(predictor=PredictorFalso("procesos", 0.90))
        with self.assertRaises(PreguntaInvalidaError):
            servicio.responder("   ")
        with self.assertRaises(PreguntaInvalidaError):
            servicio.responder("x" * 501)
        with self.assertRaises(PreguntaInvalidaError):
            servicio.responder(123)  # type: ignore[arg-type]

    def test_umbral_invalido(self) -> None:
        with self.assertRaises(ValueError):
            ServicioTutor(predictor=PredictorFalso("procesos", 0.9), umbral_confianza=1.5)

    @unittest.skipUnless(Path(MODEL_PATH).exists(), "El modelo no está entrenado")
    def test_modelo_real_responde_un_tema_conocido(self) -> None:
        respuesta = ServicioTutor().responder("¿Qué es un proceso?")
        self.assertFalse(respuesta.requiere_reformular)
        self.assertEqual(respuesta.intencion, "procesos")
        self.assertGreater(respuesta.confianza, 0.35)


if __name__ == "__main__":
    unittest.main()
