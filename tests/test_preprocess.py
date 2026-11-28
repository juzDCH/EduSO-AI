"""Pruebas de la normalización de texto usada por el clasificador."""

from __future__ import annotations

import unittest

from src.preprocess import normalizar_texto


class PruebasPreprocesamiento(unittest.TestCase):
    def test_quita_tildes_mayusculas_y_puntuacion(self) -> None:
        self.assertEqual(normalizar_texto("¿QUÉ es un PROCESO?"), "que es un proceso")

    def test_colapsa_espacios_y_simbolos(self) -> None:
        self.assertEqual(normalizar_texto("  memoria---RAM!!!  "), "memoria ram")

    def test_es_idempotente(self) -> None:
        original = "¿Cómo se administra la memoria virtual?"
        una_vez = normalizar_texto(original)
        self.assertEqual(una_vez, normalizar_texto(una_vez))

    def test_conserva_numeros(self) -> None:
        self.assertEqual(normalizar_texto("chmod 755"), "chmod 755")

    def test_texto_vacio(self) -> None:
        self.assertEqual(normalizar_texto("   "), "")


if __name__ == "__main__":
    unittest.main()
