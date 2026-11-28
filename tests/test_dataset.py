"""Pruebas de integridad del dataset y de los conjuntos de rechazo."""

from __future__ import annotations

import unittest
from pathlib import Path

from src.train import (
    NEGATIVOS_PATH,
    SONDAS_PATH,
    cargar_datos,
    cargar_sondas,
)


class PruebasDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.datos = cargar_datos()

    def test_minimo_academico_y_balance(self) -> None:
        self.assertGreaterEqual(len(self.datos), 300)
        conteo = self.datos["intencion"].value_counts()
        self.assertEqual(set(conteo.index), {"procesos", "memoria", "kernel", "comandos", "archivos", "otros"})
        for intencion in ("procesos", "memoria", "kernel", "comandos", "archivos"):
            self.assertEqual(int(conteo[intencion]), 60)

    def test_sin_duplicados_ni_vacios(self) -> None:
        self.assertEqual(int(self.datos["pregunta"].duplicated().sum()), 0)
        self.assertFalse(self.datos["pregunta"].str.strip().eq("").any())
        self.assertFalse(self.datos["intencion"].str.strip().eq("").any())

    def test_preguntas_bien_formadas(self) -> None:
        educativas = self.datos[self.datos["intencion"] != "otros"]
        self.assertTrue(educativas["pregunta"].str.endswith("?").all())
        self.assertGreaterEqual(int(self.datos["pregunta"].str.len().min()), 5)

    def test_archivos_de_apoyo_existen(self) -> None:
        self.assertTrue(Path(NEGATIVOS_PATH).exists())
        self.assertTrue(Path(SONDAS_PATH).exists())
        self.assertEqual(len(cargar_sondas()), 23)

    def test_sondas_no_estan_en_entrenamiento(self) -> None:
        preguntas_entrenamiento = set(self.datos["pregunta"].str.casefold())
        for sonda in cargar_sondas():
            self.assertNotIn(sonda.casefold(), preguntas_entrenamiento)


if __name__ == "__main__":
    unittest.main()
