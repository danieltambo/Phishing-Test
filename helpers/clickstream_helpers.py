# -------------------------------------------------
# Helpers para la gestión del clickstream por ítem.
# Acumula eventos de interacción del usuario y los
# congela cuando se toma una decisión.
# -------------------------------------------------

# -------------------------------------------------
# Buffer de eventos de interacción por ítem.
#
# item_events es una lista temporal de eventos
# (diccionarios) correspondiente al ítem actual.
# Cada evento tiene una estructura similar a:
#
# {
#     "type": "hover",
#     "target": "...",
#     "ts": 1767469702889,
#     ...
# }
#
# Los eventos no incluyen session_id ni item_id
# hasta que se congelan al tomar una decisión.
# -------------------------------------------------


import streamlit as st

# -------------------------------------------------
# Inicializa la estructura de eventos del ítem actual.
# Garantiza que exista una lista de eventos en sesión
# antes de empezar a capturar interacciones.
# -------------------------------------------------

def init_item_events():
    if "item_events" not in st.session_state:
        st.session_state.item_events = []

# -------------------------------------------------
# Añade un evento  al ítem actual.
# Los eventos se acumulan temporalmente en sesión
# hasta que el ítem queda cerrado.
# -------------------------------------------------

def push_event(event):
    st.session_state.item_events.append(event)


# -------------------------------------------------
# Congela los eventos del ítem actual.
# Asocia cada evento con la sesión y el ítem,
# y limpia el buffer para el siguiente ítem.
# -------------------------------------------------

def freeze_item_events(session_id, item_id):
    frozen = []
    for e in st.session_state.item_events:
        e2 = e.copy()
        e2["session_id"] = session_id
        e2["item_id"] = item_id
        frozen.append(e2)
    st.session_state.item_events = []  # reset para el siguiente ítem
    return frozen
