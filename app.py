"""Frontend mínimo de EduSO AI; Antonio puede ampliar diseño y navegación."""

from __future__ import annotations

import streamlit as st

from src.modules.catalog import listar_modulos
from src.services.tutor import PreguntaInvalidaError, ServicioTutor


st.set_page_config(page_title="EduSO AI", page_icon="🧠", layout="wide")


@st.cache_resource
def obtener_tutor() -> ServicioTutor:
    return ServicioTutor()


def mostrar_inicio() -> None:
    st.title("EduSO AI")
    st.write("Entiende lo que sucede dentro de tu computadora.")
    st.caption("Aprende Sistemas Operativos con explicaciones y experimentos guiados.")

    st.subheader("Módulos del proyecto")
    columnas = st.columns(2)
    for indice, modulo in enumerate(listar_modulos()):
        with columnas[indice % 2]:
            estado = "Disponible" if modulo["listo"] else "En desarrollo"
            st.info(
                f"**{modulo['titulo']}** · {estado}\n\n"
                f"Responsable: {modulo['responsable']}\n\n{modulo['resumen']}"
            )


def mostrar_tutor() -> None:
    st.title("Tutor de Sistemas Operativos")
    st.write("Pregunta sobre procesos, memoria, kernel, comandos o archivos.")

    with st.form("formulario_tutor", clear_on_submit=False):
        pregunta = st.text_area(
            "Tu pregunta",
            placeholder="Ej.: ¿Qué pasa cuando abro un programa?",
            max_chars=500,
            height=100,
        )
        enviar = st.form_submit_button("Consultar al tutor", type="primary")

    if not enviar:
        return
    if not pregunta.strip():
        st.warning("Escribe una pregunta para continuar.")
        return

    try:
        respuesta = obtener_tutor().responder(pregunta)
    except FileNotFoundError:
        st.error("No encuentro el modelo. Ejecuta `python -m src.train` desde la carpeta del proyecto.")
        return
    except PreguntaInvalidaError as error:
        st.warning(str(error))
        return

    st.subheader(respuesta.titulo)
    st.write(respuesta.explicacion)
    if respuesta.requiere_reformular:
        st.warning("Prueba a reformular la pregunta con un concepto más concreto.")
    else:
        izquierda, derecha = st.columns(2)
        with izquierda:
            st.markdown("**Analogía**")
            st.write(respuesta.analogia)
        with derecha:
            st.markdown("**Ejemplo**")
            st.write(respuesta.ejemplo)
        st.info(f"Comprueba lo aprendido: {respuesta.pregunta_comprobacion}")

    if respuesta.intencion_sugerida:
        st.caption(
            f"Tema sugerido: {respuesta.intencion_sugerida} · "
            f"Confianza del clasificador: {respuesta.confianza:.0%}"
        )


def main() -> None:
    with st.sidebar:
        st.title("EduSO AI")
        vista = st.radio("Navegación", ["Inicio", "Tutor IA"])
        st.divider()
        st.caption("Los simuladores y retos se habilitarán al completar sus módulos.")

    if vista == "Inicio":
        mostrar_inicio()
    else:
        mostrar_tutor()


if __name__ == "__main__":
    main()

