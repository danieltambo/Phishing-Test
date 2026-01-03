# helpers/clickstream_helpers.py

# Helper del componente de Clickstream. Para acumular eventos por item y congelarlos al decidir.

import streamlit as st

def init_item_events():
    if "item_events" not in st.session_state:
        st.session_state.item_events = []

def push_event(event):
    st.session_state.item_events.append(event)

def freeze_item_events(session_id, item_id):
    frozen = []
    for e in st.session_state.item_events:
        e2 = e.copy()
        e2["session_id"] = session_id
        e2["item_id"] = item_id
        frozen.append(e2)
    st.session_state.item_events = []  # reset para el siguiente ítem
    return frozen
