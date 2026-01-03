# helpers/item_service.py

import streamlit as st
from datetime import datetime

# -----------------------------
# Inicialización
# -----------------------------
def init_items(items: list[dict]) -> None:
    """
    Inicializa el servicio de ítems.
    Idempotente: si ya está inicializado, no hace nada.
    """
    if "_items" not in st.session_state:
        st.session_state["_items"] = items
        st.session_state["_item_index"] = 0
        st.session_state["_item_responses"] = []


# -----------------------------
# Acceso al ítem actual
# -----------------------------
def current_item() -> dict:
    items = st.session_state["_items"]
    index = st.session_state["_item_index"]

    if index < 0 or index >= len(items):
        raise IndexError("Índice de ítem fuera de rango")

    return items[index]

# -----------------------------
#  Devuelve True si el ítem actual ya tiene decisión registrada
# -----------------------------
def has_response() -> bool:
    
    item = current_item()
    item_id = item["item_id"]

    responses = st.session_state["_item_responses"]

    return any(
        r["item_id"] == item_id
        for r in responses
    )
    
   

# -----------------------------
# Registro de respuesta
# -----------------------------
def record_response(value) -> None:
    item = current_item()

    st.session_state["_item_responses"].append({
        "item_id": item["item_id"],
        "item_type": item.get("item_type", "PL"),
        "value": value,
        "timestamp": datetime.utcnow().isoformat(),
    })


# -----------------------------
# Progreso
# -----------------------------
def next_item() -> None:
    st.session_state["_item_index"] += 1


def is_last() -> bool:
    items = st.session_state["_items"]
    index = st.session_state["_item_index"]
    return index == len(items) - 1


def current_index():
    return st.session_state["_item_index"]

def total_items():
    return len(st.session_state["_items"])


# -----------------------------
# Salida de datos
# -----------------------------
def get_all_responses() -> list[dict]:
    return list(st.session_state["_item_responses"])


def get_item_responses() -> list[dict]:
    """
    Devuelve las respuestas de los ítems P/L.
    """
    return st.session_state.get("_item_responses", [])
