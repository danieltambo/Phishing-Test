# helpers/layout.py
import streamlit as st
from helpers.ui_texts import HEADERS

def render_header(screen):
    header = HEADERS.get(screen)

    if not header:
        return

    col_title, col_logo = st.columns([10, 2])

    with col_title:
        st.markdown(
            f"<h3 style='margin-bottom:0.2rem;'>{header['title']}</h3>",
            unsafe_allow_html=True
        )

    with col_logo:
        st.image("assets/uoc_logo.png", width=80)

    #st.markdown("---")


def render_layout():
   
    st.set_page_config(page_title="Identificación  Phishing", layout="centered", page_icon="🤓")

    """CSS global + header común"""

        # ---------- CSS GLOBAL ----------
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


    # ---------- HEADER ----------
    # col_left, col_right = st.columns([10, 2])

    # with col_left:
    #     #st.markdown(" ")
    #     st.markdown("### Estudio sobre la identificación de correos electrónicos engañosos (phishing)")

    # with col_right:
    #     st.image("assets/uoc_logo.png", width=120)
