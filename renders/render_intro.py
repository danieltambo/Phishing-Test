# -------------------------------------------------
# Render de la pantalla de introducción del estudio.
# Gestiona la presentación inicial, el consentimiento
# informado y el acceso al inicio del ejercicio.
# -------------------------------------------------


# -------------------------------------------------
# Dependencias de UI y flujo.
# Incluye textos estáticos de la introducción y utilidades para avanzar en el flujo del test.
# -------------------------------------------------
import streamlit as st
from helpers.ui_texts import INTRO_TEXT, CONSENT_TEXT, MAIL_TEXT
from helpers.flow_helpers import go_to

# -------------------------------------------------
# Render actual de la pantalla de introducción.
# Presenta el consentimiento informado y permite iniciar el test tras la aceptación explícita.
# -------------------------------------------------

def render_intro():
    # Introducción
    st.markdown(INTRO_TEXT, unsafe_allow_html=True)
    st.markdown("---")

    # Consentimiento
    st.markdown("### Consentimiento informado")
    st.markdown(CONSENT_TEXT)

    # El usuario debe aceptar explícitamente el consentimient antes de poder iniciar el estudio.
    consent = st.checkbox( "He leído la información y acepto participar en el estudio", key="consent_checkbox")
    
        
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

            # Avanza a la fase de ítems tras completar la introducción
            go_to("ITEMS")
            
            # Esto es una prueba para acortar
            #go_to("CONTEXT")
            
