"""Frontend mínimo de EduSO AI; Antonio puede ampliar diseño y navegación."""

from __future__ import annotations

import streamlit as st

from src.modules.catalog import listar_modulos
from src.services.tutor import PreguntaInvalidaError, ServicioTutor


st.set_page_config(page_title="EduSO AI", page_icon="🧠", layout="wide")

TEMAS = ["procesos", "memoria", "kernel", "comandos", "archivos"]
TITULOS_TEMA = {
    "procesos": "Procesos",
    "memoria": "Memoria RAM",
    "kernel": "Kernel",
    "comandos": "Comandos Linux",
    "archivos": "Archivos y carpetas",
}
DESCRIPCIONES_TEMA = {
    "procesos": "Descubre qué ocurre cuando abres una aplicación.",
    "memoria": "Aprende cómo se usa y se libera la RAM.",
    "kernel": "Conoce quién coordina el hardware y los programas.",
    "comandos": "Practica instrucciones básicas de la terminal.",
    "archivos": "Aprende a organizar archivos y carpetas.",
}
PREGUNTAS_EJEMPLO = {
    "procesos": "¿Qué es un proceso?",
    "memoria": "¿Para qué sirve la memoria RAM?",
    "kernel": "¿Qué hace el kernel?",
    "comandos": "¿Qué hace el comando pwd?",
    "archivos": "¿Cómo creo una carpeta en Linux?",
}


@st.cache_resource
def obtener_tutor() -> ServicioTutor:
    return ServicioTutor()


def abrir_tema(tema: str) -> None:
    st.session_state["selector_tema"] = tema
    st.session_state["tema_seleccionado"] = tema
    st.session_state["navegacion"] = "Explorar temas"


def preguntar_sobre_tema(tema: str) -> None:
    st.session_state["tema_seleccionado"] = tema
    st.session_state["selector_tema"] = tema
    st.session_state["pregunta_tutor"] = PREGUNTAS_EJEMPLO[tema]
    st.session_state["navegacion"] = "Tutor IA"


def mostrar_inicio() -> None:
    st.title("¿Qué te gustaría entender hoy?")
    st.write(
        "Aprende Sistemas Operativos a tu ritmo. Elige un tema que te dé curiosidad "
        "o escribe tu duda con tus propias palabras."
    )

    st.subheader("Elige un tema para empezar")
    st.caption("Puedes empezar por lo que más te interese; no necesitas saber términos técnicos.")
    columnas = st.columns(3)
    for indice, tema in enumerate(TEMAS):
        with columnas[indice % 3]:
            with st.container(border=True):
                st.markdown(f"### {TITULOS_TEMA[tema]}")
                st.write(DESCRIPCIONES_TEMA[tema])
                st.button(
                    "Explorar tema",
                    key=f"abrir_{tema}",
                    on_click=abrir_tema,
                    args=(tema,),
                    use_container_width=True,
                )

    st.divider()
    st.subheader("Así te ayuda el tutor")
    pasos = st.columns(4)
    for columna, numero, titulo, detalle in zip(
        pasos,
        ("1", "2", "3", "4"),
        ("Pregunta", "Entiende", "Mira un ejemplo", "Comprueba"),
        (
            "Escribe la duda como te salga.",
            "Recibe una explicación sencilla.",
            "Conecta la idea con algo cotidiano.",
            "Responde una pregunta breve para repasar.",
        ),
    ):
        with columna:
            st.markdown(f"**{numero}. {titulo}**")
            st.caption(detalle)

    pendientes = [modulo for modulo in listar_modulos() if not modulo["listo"]]
    if pendientes:
        with st.expander("Otros laboratorios que se están preparando"):
            for modulo in pendientes:
                st.markdown(f"**{modulo['titulo']}** — {modulo['resumen']}")


def mostrar_tema() -> None:
    st.title("Explora un tema")
    tema_inicial = st.session_state.get("tema_seleccionado", TEMAS[0])
    indice_inicial = TEMAS.index(tema_inicial) if tema_inicial in TEMAS else 0
    tema = st.selectbox(
        "¿Qué te interesa aprender?",
        options=TEMAS,
        index=indice_inicial,
        format_func=lambda clave: TITULOS_TEMA[clave],
        key="selector_tema",
    )
    st.session_state["tema_seleccionado"] = tema

    contenido = obtener_tutor_contenido(tema)
    st.subheader(contenido.titulo)
    st.markdown("**La idea principal**")
    st.write(contenido.explicacion)

    izquierda, derecha = st.columns(2)
    with izquierda:
        st.markdown("**Una comparación sencilla**")
        st.write(contenido.analogia)
    with derecha:
        st.markdown("**Un ejemplo**")
        st.write(contenido.ejemplo)

    st.info(f"**Comprueba lo que entendiste:** {contenido.pregunta_comprobacion}")
    st.button(
        "Preguntarle al tutor sobre este tema",
        type="primary",
        on_click=preguntar_sobre_tema,
        args=(tema,),
    )


def obtener_tutor_contenido(tema: str):
    from src.knowledge_base import obtener_contenido

    contenido = obtener_contenido(tema)
    if contenido is None:
        raise ValueError(f"No hay contenido educativo registrado para: {tema}")
    return contenido


def mostrar_tutor() -> None:
    st.title("Pregunta al tutor")
    st.write(
        "Escribe tu duda como se la preguntarías a un docente. El tutor identifica "
        "el tema y te responde con una explicación sencilla, una analogía, un ejemplo "
        "y una pregunta para repasar."
    )
    st.caption(
        "Temas disponibles: procesos, memoria RAM, kernel, comandos Linux y archivos. "
        "No necesitas escribir palabras técnicas."
    )

    with st.form("formulario_tutor", clear_on_submit=False):
        pregunta = st.text_area(
            "¿Qué te confunde o te da curiosidad?",
            placeholder="Ej.: ¿Qué es un proceso?",
            max_chars=500,
            height=100,
            key="pregunta_tutor",
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
        vista = st.radio(
            "Navegación",
            ["Inicio", "Explorar temas", "Tutor IA"],
            key="navegacion",
        )
        st.divider()
        st.caption("Aprende con una idea, una comparación y un ejemplo.")

    if vista == "Inicio":
        mostrar_inicio()
    elif vista == "Explorar temas":
        mostrar_tema()
    else:
        mostrar_tutor()


if __name__ == "__main__":
    main()

