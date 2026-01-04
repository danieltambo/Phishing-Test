# -------------------------------------------------
# Layout y elementos comunes de la interfaz.
# Define el header compartido entre pantallas
# y la configuración visual global de la app.
# -------------------------------------------------

# -------------------------------------------------
# Dependencias de UI.
# HEADERS define los textos y títulos asociados a cada pantalla del flujo.
# -------------------------------------------------
import streamlit as st
from helpers.ui_texts import HEADERS


# -------------------------------------------------
# Renderiza el header común de la pantalla actual.
# Muestra el título contextual y el logo institucional
# en función del estado del flujo.
# -------------------------------------------------

def render_header(screen):
    # screen corresponde al estado actual del flujo y se utiliza como clave para obtener el header.

    header = HEADERS.get(screen)

    if not header:
        return

    # Layout del header en dos columnas:
    # título a la izquierda y logo a la derecha.
    col_title, col_logo = st.columns([10, 2])

    with col_title:
        st.markdown(
            f"<h3 style='margin-bottom:0.2rem;'>{header['title']}</h3>",
            unsafe_allow_html=True
        )

    with col_logo:
        st.image("assets/uoc_logo.png", width=80)

    #st.markdown("---")


# -------------------------------------------------
# Configura el layout global de la aplicación.
# Define parámetros de página y estilos CSS
# compartidos por todas las pantallas.
# -------------------------------------------------

def render_layout():
   
    # Configuración global de la página Streamlit
    st.set_page_config(page_title="Identificación  Phishing", layout="centered", page_icon="🤓")

    # CSS global para ajustar márgenes y ancho máximo
    # del contenedor principal de la aplicación.
    
    st.markdown(
        """
        <style>
        section.main {
            padding-top: 0rem !important;
        }

        .block-container {
            max-width: 1000px;
            padding-top: 3rem !important;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
