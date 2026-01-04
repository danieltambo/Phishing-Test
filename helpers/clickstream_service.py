# -------------------------------------------------
# Servicio de gestión del clickstream.
# Gestiona el ciclo de vida de los eventos de interacción:
# captura por ítem, congelado y acumulación final.
# -------------------------------------------------


import streamlit as st

# -------------------------------------------------
# Inicializa las estructuras de clickstream en sesión.
# Crea un buffer para los eventos del ítem activo
# y un buffer global para los eventos congelados.
# -------------------------------------------------

def init_clickstream():
    if "current_item_events" not in st.session_state:
        st.session_state.current_item_events = []

    if "events_buffer" not in st.session_state:
        st.session_state.events_buffer = []


# -------------------------------------------------
# Registra un evento de interacción del ítem activo.
# El evento se almacena temporalmente hasta que
# el ítem se cierra mediante el congelado.
# -------------------------------------------------

def push(event: dict):
    st.session_state.current_item_events.append(event)

# -------------------------------------------------
# Congela los eventos del ítem activo.
# Enriquece cada evento con el item_id,
# los mueve al buffer final y limpia el buffer activo.
# -------------------------------------------------

def freeze_item_events(item_id: str):
 
    # Lista temporal para los eventos congelados de este ítem
    frozen_events = []

    # -------------------------------------------------
    # Transformación de eventos crudos a filas finales.
    # Se normaliza la estructura de cada evento antes
    # de añadirlo al buffer global.
    # -------------------------------------------------

    for e in st.session_state["current_item_events"]:
        row = {
            "item_id": item_id,
            "event": e.get("event"),
            "target": e.get("target"),
            "timestamp": e.get("timestamp"),
            "duration": e.get("duration"),
        }
        frozen_events.append(row)

    # Añadimos los eventos congelados al buffer global
    st.session_state["events_buffer"].extend(frozen_events)

    # Limpiamos los eventos del ítem actual
    st.session_state["current_item_events"] = []



# -------------------------------------------------
# Devuelve todos los eventos congelados.
# Esta función expone los eventos listos
# para su persistencia externa.
# -------------------------------------------------

def get_all_events() -> list[dict]:
    return st.session_state.get("events_buffer", [])
