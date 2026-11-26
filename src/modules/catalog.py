"""Estado común de módulos para que el frontend pueda mostrar su avance."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class EstadoModulo:
    clave: str
    titulo: str
    responsable: str
    listo: bool
    resumen: str
    archivo: str

    def a_dict(self) -> dict[str, str | bool]:
        return asdict(self)


MODULOS: tuple[EstadoModulo, ...] = (
    EstadoModulo(
        clave="tutor",
        titulo="Tutor IA",
        responsable="Dante",
        listo=True,
        resumen="Clasifica preguntas y entrega una explicación educativa.",
        archivo="src/services/tutor.py",
    ),
    EstadoModulo(
        clave="procesos",
        titulo="Simulador de procesos",
        responsable="Marco",
        listo=False,
        resumen="Estados y transiciones de procesos del sistema operativo.",
        archivo="src/modules/processes.py",
    ),
    EstadoModulo(
        clave="memoria",
        titulo="Laboratorio de memoria",
        responsable="Marco",
        listo=False,
        resumen="Asignación, liberación y visualización de bloques de RAM.",
        archivo="src/modules/memory.py",
    ),
    EstadoModulo(
        clave="terminal",
        titulo="Terminal Linux simulada",
        responsable="Nicol",
        listo=False,
        resumen="Intérprete educativo sin ejecutar comandos del sistema real.",
        archivo="src/modules/terminal.py",
    ),
    EstadoModulo(
        clave="retos",
        titulo="Retos y evaluaciones",
        responsable="Nicol",
        listo=False,
        resumen="Preguntas, puntaje y retroalimentación por respuesta.",
        archivo="src/modules/quizzes.py",
    ),
)


def listar_modulos() -> list[dict[str, str | bool]]:
    """Devuelve tarjetas listas para que una interfaz las presente."""
    return [modulo.a_dict() for modulo in MODULOS]

