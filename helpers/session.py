# -------------------------------------------------
# Gestión del identificador de sesión.
# Define y mantiene un identificador único y estable
# para cada sesión de usuario en la aplicación.
# -------------------------------------------------

import uuid
import streamlit as st


# -------------------------------------------------
# El session_id es global a toda la aplicación.
# Se utiliza para vincular respuestas y eventos
# a una misma sesión de usuario.
# -------------------------------------------------

# -------------------------------------------------
# Inicializa el identificador de sesión.
# Genera un UUID único y lo almacena en sesión
# si todavía no existe.
# -------------------------------------------------
def init_session():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())


# -------------------------------------------------
# Devuelve el identificador de la sesión actual.
# Garantiza su inicialización antes de devolverlo
# para asegurar consistencia en toda la app.
# -------------------------------------------------

def get_session_id() -> str:
    if "session_id" not in st.session_state:
        init_session()

    return st.session_state["session_id"]
