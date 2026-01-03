# helpers/context_service.py

import streamlit as st
from datetime import datetime


def init_context_responses() -> None:
    """
    Inicializa el contenedor de respuestas de contexto.
    """
    if "_context_responses" not in st.session_state:
        st.session_state["_context_responses"] = []

def init_context_buffer() -> None:
    """
    Inicializa el buffer temporal de respuestas de contexto
    (solo para la UI, no persistente).
    """
    if "context_buffer" not in st.session_state:
        st.session_state.context_buffer = {}



def record_context_response(question_id: str, value) -> None:
    """
    Registra una respuesta de contexto usando el mismo esquema
    que los ítems experimentales.
    """
    st.session_state["_context_responses"].append({
        "item_id": question_id,
        "item_type": "CTX",
        "value": value,
        "timestamp": datetime.utcnow().isoformat(),
    })


def get_context_responses() -> list[dict]:
    """
    Devuelve todas las respuestas de contexto registradas.
    """
    return st.session_state.get("_context_responses", [])


def freeze_context_responses(context_buffer: dict) -> None:
    """
    Congela las respuestas de contexto almacenadas en el buffer temporal
    y las registra como respuestas definitivas (CTX).
    """
    for question_id, value in context_buffer.items():
        if value is not None:
            record_context_response(
                question_id=question_id,
                value=value
            )
