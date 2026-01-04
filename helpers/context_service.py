# -------------------------------------------------
# Servicio de gestión de respuestas de contexto.
# Maneja la inicialización, captura temporal y
# registro definitivo de respuestas CTX.
# -------------------------------------------------

import streamlit as st
import time

# -------------------------------------------------
# Inicializa el contenedor persistente de respuestas
# de contexto dentro de la sesión.
# -------------------------------------------------

def init_context_responses() -> None:

    if "_context_responses" not in st.session_state:
        st.session_state["_context_responses"] = []

# -------------------------------------------------
# Inicializa el buffer temporal de respuestas de contexto.
# Este buffer se usa solo a nivel de UI y no se persiste
# directamente como resultado del test.
# -------------------------------------------------

def init_context_buffer() -> None:
 
    if "context_buffer" not in st.session_state:
        st.session_state.context_buffer = {}


# -------------------------------------------------
# Registra una respuesta de contexto definitiva.
# Normaliza la respuesta al mismo esquema que los
# ítems experimentales (tipo CTX).
# -------------------------------------------------

def record_context_response(question_id: str, value) -> None:

    st.session_state["_context_responses"].append({
        "item_id": question_id,
        "item_type": "CTX",
        "value": value,
        "timestamp": int(time.time() * 1000)  # Timestamp almacenado como Unix time en milisegundos (UTC)
    })

# -------------------------------------------------
# Devuelve todas las respuestas de contexto registradas.
# Se utiliza en la fase de guardado para persistencia.
# -------------------------------------------------

def get_context_responses() -> list[dict]:

    return st.session_state.get("_context_responses", [])

# -------------------------------------------------
# Congela las respuestas de contexto desde el buffer.
# Transforma las respuestas temporales de la UI
# en respuestas definitivas registradas.
# -------------------------------------------------

def freeze_context_responses(context_buffer: dict) -> None:

    for question_id, value in context_buffer.items():
        if value is not None:
            record_context_response(
                question_id=question_id,
                value=value
            )
