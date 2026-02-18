# -------------------------------------------------
# Render del bloque de preguntas de contexto (CTX).
# Muestra el cuestionario final y recoge las respuestas de forma temporal antes de persistirlas.
# -------------------------------------------------

import streamlit as st
from helpers.flow_helpers import go_to
from helpers.ui_texts import CONTEXT_INTRO_TEXT, CONTEXT_QUESTIONS
from helpers.context_service import init_context_responses, init_context_buffer
from helpers.context_service import freeze_context_responses

# -------------------------------------------------
# Comprueba si todas las pregunas de contexto han sido contestadas.
# Es un helper local.
# -------------------------------------------------
def all_context_answered():
    return all(
        v is not None
        for v in st.session_state.context_buffer.values()
    )



# -------------------------------------------------
# Renderiza el cuestionario de contexto.
# Las respuestas se almacenan primero en un buffer temporal y se congelan al finalizar el bloque.
# -------------------------------------------------

def render_context():

    # Texto introductorio
    st.markdown(CONTEXT_INTRO_TEXT, unsafe_allow_html=True)
    st.markdown( "<hr style='margin:0rem 0 0.8rem 0;'>", unsafe_allow_html=True)

   
    # Inicializa estructuras de sesión:
    # - respuestas definitivas (CTX)
    # - buffer temporal para la UI
    init_context_responses()
    init_context_buffer()

    # 👉 A partir de aquí, la primera pregunta aparece directamente
    # render_context_question_1()


    # Render secuencial de todas las preguntas de contexto definidas en eñ config.
    
    for q in CONTEXT_QUESTIONS:
        
        # --- TEXTO DE LA PREGUNTA ---
        if q["type"] == "likert_5":
            st.markdown(
                f""" <div style="margin-bottom:0.35rem; line-height:1.35;">  {q['question']} <span style="font-size:0.8rem; font-style:italic; color:#6b7280; "> (1 = Poco · 5 = Mucho)  </span>    </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='margin-bottom:0.35rem; line-height:1.35;'>{q['question']}</div>",
                unsafe_allow_html=True
            )

        # --- TEXTO DE LA RESPUESTA ---
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


        # Almacena la respuesta en el buffer temporal (aún no persistida).
        st.session_state.context_buffer[q["id"]] = response

        st.markdown("<div style='margin-bottom:1rem'></div>", unsafe_allow_html=True)

    # Al finalizar el cuestionario, se congelan todas las respuestas de contexto y se avanza a la pantalla de guardado.
    if st.button("Guardar Respuestas", key="context_next"):

        # Comrpueba que todas las preguntas se hayan contestado
        if not all_context_answered():
            st.warning("Por favor, responde a todas las preguntas antes de continuar.")
            
            # En pruebas poner # antes de return. En produccion eliminar #.
            return 
        
        # Convierte el buffer temporal en respuestas definitivas de tipo CTX.
        freeze_context_responses(st.session_state.context_buffer)

        st.info ("Guardando tus respuestas…")

        go_to("SAVE")

        
        
