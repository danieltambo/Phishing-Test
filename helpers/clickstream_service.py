# helpers/clickstream_service.py

import streamlit as st


def init_clickstream():
    if "current_item_events" not in st.session_state:
        st.session_state.current_item_events = []

    if "events_buffer" not in st.session_state:
        st.session_state.events_buffer = []


def push(event: dict):
    """
    Guarda SIEMPRE el evento del ítem activo
    """
    st.session_state.current_item_events.append(event)


def freeze_item_events(item_id: str):
    """
    Congela los eventos del ítem actual:
    - añade item_id a cada evento
    - los mueve al buffer final
    - limpia los eventos activos
    """
    
    #Esto es temporal
    #print("FREEZE CALLED FOR:", item_id)
    #print("N current events:", len(st.session_state["current_item_events"]))

    # Lista temporal para los eventos congelados de este ítem
    frozen_events = []

    # Recorremos los eventos del ítem activo
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



def get_all_events() -> list[dict]:
    """
    Devuelve todos los eventos congelados listos para persistir
    """
    return st.session_state.get("events_buffer", [])
