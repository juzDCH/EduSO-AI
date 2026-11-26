"""Normalización de texto en español para el clasificador de intenciones."""

from __future__ import annotations

import re
import unicodedata


def normalizar_texto(texto: str) -> str:
    """Pasa el texto a minúsculas, quita tildes y puntuación y ordena espacios.

    Se conserva el contenido de las palabras. No se eliminan palabras vacías,
    porque expresiones cortas como "qué es" también pueden aportar contexto.
    """
    texto = unicodedata.normalize("NFKD", str(texto))
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


if __name__ == "__main__":
    ejemplos = [
        "¿QUÉ es un PROCESO?",
        "   ¿Para qué sirve la memoria RAM?   ",
        "¡El kernel administra CPU, memoria y dispositivos!",
    ]
    for original in ejemplos:
        print(f"Original: {original}\nLimpio:   {normalizar_texto(original)}\n")

