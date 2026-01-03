import uuid
import streamlit as st
from datetime import datetime


_SESSION_ID_KEY = "session_id"


# la variable sesion_id es global a toda la app
def init_session():
    if _SESSION_ID_KEY not in st.session_state:
        st.session_state[_SESSION_ID_KEY] = str(uuid.uuid4())



def get_session_id() -> str:
    """
    Identificador único y estable para la sesión actual.
    """
    if "session_id" not in st.session_state:
        init_session()
        
    return st.session_state[_SESSION_ID_KEY]


