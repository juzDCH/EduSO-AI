"""Respuestas didácticas revisables que acompañan al clasificador de intención.

El modelo reconoce el tema de una pregunta; este módulo aporta el contenido
educativo. Así evitamos presentar el clasificador como un modelo generativo.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ContenidoEducativo:
    intencion: str
    titulo: str
    explicacion: str
    analogia: str
    ejemplo: str
    pregunta_comprobacion: str

    def a_dict(self) -> dict[str, str]:
        return asdict(self)


BASE_CONOCIMIENTO: dict[str, ContenidoEducativo] = {
    "procesos": ContenidoEducativo(
        intencion="procesos",
        titulo="Procesos: programas en ejecución",
        explicacion=(
            "Un proceso es una instancia de un programa que está ejecutándose. "
            "El sistema operativo registra su estado y los recursos que necesita, "
            "como memoria y tiempo de CPU. Puede estar nuevo, listo, ejecutándose, "
            "esperando una operación o terminado."
        ),
        analogia=(
            "El programa es una receta guardada; el proceso es alguien preparando "
            "esa receta ahora, con una mesa de trabajo y utensilios asignados."
        ),
        ejemplo=(
            "Al abrir un navegador, el sistema operativo crea uno o más procesos "
            "para ejecutar sus tareas."
        ),
        pregunta_comprobacion=(
            "Si un proceso espera que termine una lectura del disco, ¿está usando "
            "la CPU en ese instante?"
        ),
    ),
    "memoria": ContenidoEducativo(
        intencion="memoria",
        titulo="Memoria: espacio de trabajo temporal",
        explicacion=(
            "La memoria RAM guarda temporalmente instrucciones y datos que los "
            "procesos usan mientras trabajan. El sistema operativo asigna y libera "
            "espacio. La RAM es volátil: su contenido se pierde al apagar el equipo."
        ),
        analogia=(
            "Piensa en la RAM como una mesa de trabajo: los documentos que usas "
            "ahora están sobre la mesa y los demás quedan guardados en un archivo."
        ),
        ejemplo=(
            "Al abrir un editor y un navegador, ambos necesitan espacio en RAM "
            "para mantener sus datos activos."
        ),
        pregunta_comprobacion=(
            "¿Qué sucede con los datos guardados únicamente en RAM cuando se apaga "
            "la computadora?"
        ),
    ),
    "kernel": ContenidoEducativo(
        intencion="kernel",
        titulo="Kernel: núcleo del sistema operativo",
        explicacion=(
            "El kernel es la parte central del sistema operativo. Coordina el uso "
            "de CPU, memoria y dispositivos, y ofrece servicios a los programas "
            "mediante mecanismos controlados como las llamadas al sistema."
        ),
        analogia=(
            "Es como una central de coordinación: recibe solicitudes, comprueba "
            "qué recurso se necesita y organiza el acceso compartido."
        ),
        ejemplo=(
            "Cuando una aplicación solicita leer un archivo, pide el servicio al "
            "sistema operativo; el kernel coordina el acceso al dispositivo."
        ),
        pregunta_comprobacion=(
            "¿Por qué una aplicación solicita servicios al sistema operativo en "
            "vez de controlar directamente todos los dispositivos?"
        ),
    ),
    "comandos": ContenidoEducativo(
        intencion="comandos",
        titulo="Comandos: instrucciones para la terminal",
        explicacion=(
            "Un comando es una instrucción que escribes en una interfaz de línea "
            "de comandos. Por ejemplo, pwd muestra la ubicación actual, ls lista "
            "elementos y cd cambia de directorio."
        ),
        analogia=(
            "La terminal funciona como un intérprete: escribes una instrucción "
            "con una forma acordada y recibes una acción o resultado."
        ),
        ejemplo=(
            "pwd permite consultar la ruta actual; ls permite ver qué hay en esa "
            "ubicación."
        ),
        pregunta_comprobacion=(
            "¿Qué comando usarías para ver la ruta actual y cuál para listar su "
            "contenido?"
        ),
    ),
    "archivos": ContenidoEducativo(
        intencion="archivos",
        titulo="Archivos y directorios",
        explicacion=(
            "Un archivo almacena información y un directorio organiza archivos y "
            "otros directorios. En Linux, herramientas como mkdir, touch y cp "
            "permiten crear directorios, crear archivos vacíos y copiar elementos."
        ),
        analogia=(
            "Un directorio se parece a una carpeta organizadora; dentro puede "
            "haber documentos y otras carpetas."
        ),
        ejemplo=(
            "mkdir tareas crea un directorio llamado tareas. En esta aplicación, "
            "los comandos se practicarán en una simulación educativa."
        ),
        pregunta_comprobacion=(
            "¿Qué diferencia hay entre un archivo y el directorio que lo contiene?"
        ),
    ),
}


def obtener_contenido(intencion: str) -> ContenidoEducativo | None:
    """Devuelve contenido para una intención conocida; None si no existe."""
    return BASE_CONOCIMIENTO.get(intencion)


def listar_intenciones() -> list[str]:
    """Lista las categorías cubiertas por el dataset y el tutor."""
    return sorted(BASE_CONOCIMIENTO)

