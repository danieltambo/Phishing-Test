# renders/items.py

import streamlit as st
from helpers.flow_helpers import go_to
from helpers.ui_texts import CONTEXT_INTRO_TEXT, CONTEXT_QUESTIONS
from helpers.context_service import init_context_responses, record_context_response,init_context_buffer
from helpers.context_service import freeze_context_responses




def render_context():
    #st.subheader("CONTEXT")

    # Texto introductorio
    st.markdown(CONTEXT_INTRO_TEXT, unsafe_allow_html=True)

    st.markdown( "<hr style='margin:0rem 0 0.8rem 0;'>", unsafe_allow_html=True)

    # Inicializamos buffer para almacenar resultados
    init_context_responses()
    init_context_buffer()

    # 👉 A partir de aquí, la primera pregunta aparece directamente
    # render_context_question_1()

    st.markdown( """
        <div style=" font-size:0.9rem; font-style:italic; color:#6b7280; margin-bottom:1.2rem;">
            En las siguientes afirmaciones, utiliza una escala: 
            1 = Poco · 5 = Mucho
        </div> 
        """, unsafe_allow_html=True )


    for q in CONTEXT_QUESTIONS:
        #st.markdown(f"**{q['question']}**")
        st.markdown(
            f"<div style='margin-bottom:0.35rem; line-height: 1.35;'> {q['question']}</div>",
            unsafe_allow_html=True
        )

        if q["type"] == "choice":
            response = st.radio(
                label="Escala de respuesta",
                options=q["options"],
                index=None,
                key=q["id"],
                label_visibility="collapsed"
            )

        elif q["type"] == "likert_5":
            response = st.radio(
                label="Escala de respuesta",
                options=[1, 2, 3, 4, 5],
                index=None,
                key=q["id"],
                horizontal=True,
                label_visibility="collapsed"
            )

        st.session_state.context_buffer[q["id"]] = response

        st.markdown("<div style='margin-bottom:1rem'></div>", unsafe_allow_html=True)

    if st.button("Guardar Respuestas", key="context_next"):

        # Guardamos todas las respuestas para luego recuperarlas
        freeze_context_responses(st.session_state.context_buffer)

        st.info ("Guardando tus respuestas…")

        go_to("SAVE")

        
        
