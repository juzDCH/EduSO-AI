"""Orquesta clasificación, confianza y contenido educativo del tutor."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from src.knowledge_base import ContenidoEducativo, obtener_contenido
from src.predictor import PredictorIntenciones


UMBRAL_CONFIANZA_INICIAL = 0.30
LONGITUD_MAXIMA_PREGUNTA = 500


class PreguntaInvalidaError(ValueError):
    """La pregunta no cumple las reglas de entrada del tutor."""


@dataclass(frozen=True)
class RespuestaTutor:
    pregunta: str
    intencion: str | None
    intencion_sugerida: str | None
    confianza: float
    titulo: str
    explicacion: str
    analogia: str
    ejemplo: str
    pregunta_comprobacion: str
    requiere_reformular: bool

    def a_dict(self) -> dict[str, Any]:
        """Formato simple para Streamlit, una API o cualquier otra interfaz."""
        return asdict(self)


class ServicioTutor:
    """Servicio independiente del frontend para responder preguntas educativas.

    El predictor solamente clasifica la intención. Las explicaciones proceden
    de la base de conocimiento y se pueden revisar sin reentrenar el modelo.
    """

    def __init__(
        self,
        predictor: Any | None = None,
        umbral_confianza: float = UMBRAL_CONFIANZA_INICIAL,
    ) -> None:
        if not 0.0 <= umbral_confianza <= 1.0:
            raise ValueError("El umbral de confianza debe estar entre 0 y 1.")
        self.predictor = predictor if predictor is not None else PredictorIntenciones()
        self.umbral_confianza = umbral_confianza

    def responder(self, pregunta: str) -> RespuestaTutor:
        texto = self._validar_pregunta(pregunta)
        prediccion = self.predictor.predecir(texto)
        intencion_sugerida = str(prediccion["intencion"])
        confianza = float(prediccion["confianza"])
        if not 0.0 <= confianza <= 1.0:
            raise ValueError("El predictor devolvió una confianza fuera del rango 0–1.")

        contenido = obtener_contenido(intencion_sugerida)
        if contenido is None or confianza < self.umbral_confianza:
            return self._respuesta_de_reformulacion(
                texto, intencion_sugerida, confianza
            )
        return self._respuesta_desde_contenido(texto, confianza, contenido)

    @staticmethod
    def _validar_pregunta(pregunta: str) -> str:
        if not isinstance(pregunta, str):
            raise PreguntaInvalidaError("La pregunta debe ser texto.")
        texto = pregunta.strip()
        if not texto:
            raise PreguntaInvalidaError("Escribe una pregunta para el tutor.")
        if len(texto) > LONGITUD_MAXIMA_PREGUNTA:
            raise PreguntaInvalidaError(
                f"La pregunta debe tener {LONGITUD_MAXIMA_PREGUNTA} caracteres o menos."
            )
        return texto

    @staticmethod
    def _respuesta_desde_contenido(
        pregunta: str, confianza: float, contenido: ContenidoEducativo
    ) -> RespuestaTutor:
        return RespuestaTutor(
            pregunta=pregunta,
            intencion=contenido.intencion,
            intencion_sugerida=contenido.intencion,
            confianza=confianza,
            titulo=contenido.titulo,
            explicacion=contenido.explicacion,
            analogia=contenido.analogia,
            ejemplo=contenido.ejemplo,
            pregunta_comprobacion=contenido.pregunta_comprobacion,
            requiere_reformular=False,
        )

    @staticmethod
    def _respuesta_de_reformulacion(
        pregunta: str, intencion_sugerida: str | None, confianza: float
    ) -> RespuestaTutor:
        return RespuestaTutor(
            pregunta=pregunta,
            intencion=None,
            intencion_sugerida=intencion_sugerida,
            confianza=confianza,
            titulo="Ayúdame a entender mejor la pregunta",
            explicacion=(
                "No pude identificar el tema con suficiente seguridad. Prueba "
                "mencionando un concepto concreto, como proceso, memoria RAM, "
                "kernel, comando o archivo."
            ),
            analogia="",
            ejemplo="Por ejemplo: ¿qué ocurre con un proceso cuando espera una operación de disco?",
            pregunta_comprobacion="",
            requiere_reformular=True,
        )

