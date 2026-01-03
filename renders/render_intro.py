# renders/intro.py

import streamlit as st
from helpers.ui_texts import INTRO_TEXT, CONSENT_TEXT, MAIL_TEXT
from helpers.flow_helpers import go_to


def render_intro_LEGACY():
    if "intro_step" not in st.session_state:
        st.session_state.intro_step = 1

    if st.session_state.intro_step == 1:

        st.markdown(INTRO_TEXT, unsafe_allow_html=True)

        st.markdown("---")

        # Consentimiento
        st.markdown("### Consentimiento informado")
        st.markdown(CONSENT_TEXT)

        consent = st.checkbox(
            "He leído la información y acepto participar en el estudio",
            key="consent_checkbox"
        )
        
        email = None
        if consent:
            st.markdown(
                "<strong>Correo electrónico (opcional)</strong>",
                unsafe_allow_html=True
            )

            email = st.text_input(
                label="Correo electrónico (opcional)",
                placeholder="tu@email.com",
                label_visibility="collapsed",
                key="email_input"
            )

            st.caption(MAIL_TEXT)
                
        if consent and st.button("Empezar"):
            #guardar email
            st.session_state.intro_step = 2
            st.rerun()



    elif st.session_state.intro_step == 2:
        st.subheader("Instrucciones del ejercicio")
        st.write(
            """
            Verás una serie de correos.
            Decide como lo harías habitualmente.
            No es un examen.
            """
        )

        if st.button("Empezar"):
            go_to("ITEMS")


def render_intro():
    # Introducción
    st.markdown(INTRO_TEXT, unsafe_allow_html=True)
    st.markdown("---")

    # Consentimiento
    st.markdown("### Consentimiento informado")
    st.markdown(CONSENT_TEXT)

    consent = st.checkbox( "He leído la información y acepto participar en el estudio",
            key="consent_checkbox")
        
    email = None
    if consent:
        st.markdown( "<strong>Correo electrónico (opcional)</strong>", unsafe_allow_html=True)

        col_left, col_right = st.columns([6, 6])

        with col_left:
            email = st.text_input(
                label="Correo electrónico (opcional)",
                placeholder="tu@email.com",
                label_visibility="collapsed",
                key="email_input"
        )

        # Informacón sobre la opcionalidad de dar el email
        st.caption(MAIL_TEXT)
                
        start = st.button("Empezar")
      
        if start and consent:
            # Guarda email si existe
            if email:
                st.session_state["email"] = email

            # Ir a la pantalla de items
            go_to("ITEMS")
