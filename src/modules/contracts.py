"""Tipos comunes para las operaciones de los módulos educativos."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class ResultadoOperacion:
    """Respuesta uniforme que un simulador o reto entrega al frontend."""

    ok: bool
    mensaje: str
    datos: dict[str, Any] = field(default_factory=dict)

    def a_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def exito(cls, mensaje: str, datos: dict[str, Any] | None = None) -> "ResultadoOperacion":
        return cls(ok=True, mensaje=mensaje, datos=datos or {})

    @classmethod
    def error(cls, mensaje: str, datos: dict[str, Any] | None = None) -> "ResultadoOperacion":
        return cls(ok=False, mensaje=mensaje, datos=datos or {})

