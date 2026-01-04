# -------------------------------------------------
# Servicio de gestión de ítems experimentales.
# Controla la secuencia de ítems, el registro de
# respuestas y el progreso del usuario en el test.
# -------------------------------------------------


import streamlit as st
import time

# -------------------------------------------------
# Inicialización del servicio de ítems.
# Prepara la lista de ítems, el índice actual
# y el contenedor de respuestas en sesión.
# -------------------------------------------------

# -------------------------------------------------
# Inicializa el estado interno de los ítems.
# Es idempotente: solo se ejecuta si el estado
# aún no existe en la sesión.
# -------------------------------------------------

def init_items(items: list[dict]) -> None:

    if "_items" not in st.session_state:
        st.session_state["_items"] = items
        st.session_state["_item_index"] = 0
        st.session_state["_item_responses"] = []


# -------------------------------------------------
# Devuelve el ítem actualmente activo.
# -------------------------------------------------

def current_item() -> dict:
    items = st.session_state["_items"]
    index = st.session_state["_item_index"]

    if index < 0 or index >= len(items):
        raise IndexError("Índice de ítem fuera de rango")

    return items[index]


# -------------------------------------------------
# Indica si el ítem actual ya tiene una respuesta.
# Se utiliza para evitar dobles registros y
# controlar el flujo de avance.
# -------------------------------------------------

def has_response() -> bool:
    
    item = current_item()
    item_id = item["item_id"]

    responses = st.session_state["_item_responses"]

    return any(
        r["item_id"] == item_id
        for r in responses
    )
    
   

# -------------------------------------------------
# Registra la respuesta del ítem actual.
# Añade metadatos mínimos (item_id, tipo y tiempo)
# y la almacena como respuesta definitiva.
# -------------------------------------------------

def record_response(value) -> None:
    item = current_item()

    st.session_state["_item_responses"].append({
        "item_id": item["item_id"],
        "item_type": item.get("item_type", "PL"),
        "value": value,
        "timestamp": int(time.time() * 1000) 
    })


# -------------------------------------------------
# Gestión del progreso del test.
# Controla el avance entre ítems y
# expone información sobre el estado actual.
# -------------------------------------------------

# -------------------------------------------------
# Avanza al siguiente ítem del test.
# Incrementa el índice interno sin validación.
# -------------------------------------------------

def next_item() -> None:
    st.session_state["_item_index"] += 1


# -------------------------------------------------
# Indica si el ítem actual es el último del test.
# Se utiliza para decidir transiciones de estado.
# -------------------------------------------------

def is_last() -> bool:
    items = st.session_state["_items"]
    index = st.session_state["_item_index"]
    return index == len(items) - 1


# -------------------------------------------------
# Devuelve el índice actual del ítem.
# Útil para indicadores de progreso en la UI.
# -------------------------------------------------

def current_index():
    return st.session_state["_item_index"]

# -------------------------------------------------
# Devuelve el número total de ítems del test.
# Se utiliza para cálculos de progreso.
# -------------------------------------------------

def total_items():
    return len(st.session_state["_items"])


# -------------------------------------------------
# Acceso a las respuestas registradas.
# Expone las respuestas acumuladas para
# persistencia o análisis posterior.
# -------------------------------------------------


# -------------------------------------------------
# Devuelve las respuestas de los ítems P/L.
# No incluye preguntas de contexto ni metadatos
# externos al flujo de ítems.
# -------------------------------------------------

def get_item_responses() -> list[dict]:

    return st.session_state.get("_item_responses", [])
