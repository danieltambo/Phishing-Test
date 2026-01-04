# -------------------------------------------------
# Punto de entrada principal de la aplicación Streamlit.
# Coordina el flujo del test en función del estado actual.
# No contiene lógica de negocio ni render específico de fases.
# -------------------------------------------------

# -------------------------------------------------
# Imports principales:
# - helpers: inicialización de sesión, flujo y layout
# - flow: definición del estado inicial y mapa de estados
# - renders: funciones de render de cada fase del test
# -------------------------------------------------
import streamlit as st
from helpers.flow_helpers import init_flow, render_current_state
from helpers.session import init_session
from helpers.ui_layout import  render_layout
from flow import build_state_map, INTRO
from renders import render_intro, render_items, render_context, render_save


# -------------------------------------------------
# Mapa central de estados del test.
# Asocia cada estado lógico del flujo experimental
# con su función de render correspondiente.
# -------------------------------------------------

STATE_MAP = build_state_map(
    render_intro,
    render_items,
    render_context,
    render_save,
)

# -------------------------------------------------
# Función orquestadora principal del test.
# Inicializa la sesión, el flujo experimental
# y delega el renderizado según el estado actual.
# -------------------------------------------------

def main():
    
    # -------------------------------------------------
    # Inicialización secuencial de la aplicación:
    # 1. Sesión y identificadores
    # 2. Estado inicial del flujo
    # 3. Layout general
    # 4. Render según estado
    # -------------------------------------------------

    
    init_session() # Sesion_id es una variable global
    init_flow(INTRO)
    render_layout()
    render_current_state(STATE_MAP)


# -------------------------------------------------
# Punto de entrada de la aplicación
# -------------------------------------------------

if __name__ == "__main__":
    main()




