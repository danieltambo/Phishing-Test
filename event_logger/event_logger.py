# Wrapper Python del componente frontend (JS/HTML) EventLogger
# Permite integrar el tracking de interacciones en Streamlit

import os
import streamlit.components.v1 as components

_COMPONENT_PATH = os.path.join(
    os.path.dirname(__file__),
    "build",
)

_component_func = components.declare_component(
    "EventLogger",
    path=_COMPONENT_PATH,
)

def event_logger(key=None, html=None):
    return _component_func(key=key, html=html)
