# -------------------------------------------------
# Helpers de control del flujo.
# Gestiona el estado actual del test y coordina
# el enrutado y renderizado según dicho estado.
# -------------------------------------------------

import streamlit as st
from helpers.ui_layout import render_header


# -------------------------------------------------
# Inicialización del flujo.
# Define el estado inicial del test al arrancar
# la sesión del usuario.
# -------------------------------------------------

def init_flow(initial_state: str):
    if "state" not in st.session_state:
        st.session_state.state = initial_state


# -------------------------------------------------
# Acceso y modificación del estado del flujo.
# Funciones auxiliares para consultar o cambiar
# la fase actual del test.
# -------------------------------------------------


def get_state() -> str:
    return st.session_state.state


# -------------------------------------------------
# Cambia explícitamente el estado del flujo.
# Fuerza un rerender inmediato de la aplicación
# para reflejar el nuevo estado.
# -------------------------------------------------
def go_to(state: str):
    st.session_state.state = state
    st.rerun()


def is_state(state: str) -> bool:
    return st.session_state.state == state


# -------------------------------------------------
# Enrutador central del flujo experimental.
# Selecciona y ejecuta el render correspondiente
# al estado actual.
# -------------------------------------------------

# -------------------------------------------------
# Dispatcher principal de estados.
# Renderiza un header común dependiente del estado
# y delega el contenido a la función específica.
# -------------------------------------------------

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


# -------------------------------------------------
# Utilidades de depuración del flujo.
# Permiten inspeccionar el estado actual durante
# el desarrollo y pruebas del instrumento.
# -------------------------------------------------

def show_flow_debug():
    with st.sidebar:
        st.markdown("### 🧭 Flow debug")
        st.write("Estado actual:", st.session_state.state)
