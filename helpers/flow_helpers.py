# flow_helpers.py
import streamlit as st
from helpers.ui_layout import render_header


# -------------------------
# Inicialización
# -------------------------

def init_flow(initial_state: str):
    if "state" not in st.session_state:
        st.session_state.state = initial_state


# -------------------------
# Lectura / escritura
# -------------------------

def get_state() -> str:
    return st.session_state.state


def go_to(state: str):
    st.session_state.state = state
    st.rerun()


def is_state(state: str) -> bool:
    return st.session_state.state == state


# -------------------------
# Router
# -------------------------

def render_current_state(state_map: dict):
    """
    state_map: dict[str, callable]
    """
    state = st.session_state.state
    render_fn = state_map.get(state)

    if render_fn is None:
        st.error(f"Estado no definido: {state}")
        return

    # 🔹 Header común dependiente del estado
    render_header(state)

    # 🔹 Contenido específico del estado
    render_fn()


# -------------------------
# Debug (opcional pero muy útil)
# -------------------------

def show_flow_debug():
    with st.sidebar:
        st.markdown("### 🧭 Flow debug")
        st.write("Estado actual:", st.session_state.state)
