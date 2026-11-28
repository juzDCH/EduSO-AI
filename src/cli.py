"""Punto de entrada de consola para usar el backend antes de tener frontend."""

from __future__ import annotations

import argparse
import sys

from src.knowledge_base import listar_intenciones
from src.modules.catalog import listar_modulos
from src.services.tutor import PreguntaInvalidaError, ServicioTutor


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prueba el backend de EduSO AI desde la consola."
    )
    parser.add_argument(
        "pregunta", nargs="?", help="Pregunta sobre Sistemas Operativos"
    )
    parser.add_argument(
        "--temas", action="store_true", help="Muestra las intenciones reconocidas"
    )
    parser.add_argument(
        "--modulos", action="store_true", help="Muestra las partes y su estado"
    )
    args = parser.parse_args()

    if args.temas:
        print("Temas: " + ", ".join(listar_intenciones()))
        return
    if args.modulos:
        for modulo in listar_modulos():
            estado = "listo" if modulo["listo"] else "pendiente"
            print(f"{modulo['titulo']} — {modulo['responsable']}: {estado}")
        return
    if not args.pregunta:
        parser.print_help()
        return

    try:
        respuesta = ServicioTutor().responder(args.pregunta)
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(2) from error
    except PreguntaInvalidaError as error:
        print(f"Pregunta no válida: {error}", file=sys.stderr)
        raise SystemExit(2) from error

    print(f"{respuesta.titulo} (confianza: {respuesta.confianza:.0%})")
    print(respuesta.explicacion)
    if respuesta.analogia:
        print(f"Analogía: {respuesta.analogia}")
    if respuesta.ejemplo:
        print(f"Ejemplo: {respuesta.ejemplo}")
    if respuesta.pregunta_comprobacion:
        print(f"Comprueba lo aprendido: {respuesta.pregunta_comprobacion}")
    if respuesta.requiere_reformular and respuesta.intencion_sugerida:
        print("El tema sugerido fue: " + str(respuesta.intencion_sugerida))


if __name__ == "__main__":
    main()

