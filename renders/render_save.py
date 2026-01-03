# renders/items.py

import streamlit as st
from datetime import datetime

from helpers.clickstream_service import get_all_events
from helpers.session import get_session_id
from helpers.gsheet import  append_rows_dicts
from helpers.response_service import get_all_responses
from helpers.ui_texts import SAVE_TEXT

from config import GSHEET_ID, RESPONSES_SHEET, EVENTS_SHEET, CONTACT_INFO_SHEET

def persistir_todo():
    session_id = get_session_id()
    # ---------- CONTACT INFO ----------
    email = st.session_state.get("email")

    if email:
        email_row = {
            "session_id": session_id,
            "email": email,
            "timestamp": datetime.utcnow().isoformat(),
        }
        
        append_rows_dicts(
            rows=[email_row],
            sheet_id=GSHEET_ID,
            worksheet_name=CONTACT_INFO_SHEET,
        )
        

    # ---------- RESPONSES ----------
    responses = get_all_responses()
    responses_to_save = []

    for r in responses:
        responses_to_save.append({
            "session_id": session_id,
            "item_id": r.get("item_id"),
            "item_type": r.get("item_type"),
            "value": r.get("value"),
            "timestamp": r.get("timestamp"),
        })

    if responses_to_save:
        append_rows_dicts(
            rows=responses_to_save,
            sheet_id=GSHEET_ID,
            worksheet_name=RESPONSES_SHEET,
        )

    # ---------- EVENTS ----------
    events = get_all_events()
    events_to_save = []

    for e in events:
        events_to_save.append({
            "session_id": session_id,
            "item_id": e.get("item_id"),
            "event": e.get("event"),
            "target": e.get("target"),
            "timestamp": e.get("timestamp"),
            "duration": e.get("duration"),
        })

    if events_to_save:
        append_rows_dicts(
            rows=events_to_save,
            sheet_id=GSHEET_ID,
            worksheet_name=EVENTS_SHEET,
        )

def render_save():
    st.empty()

    with st.spinner("Guardando tus respuestas…"):
        persistir_todo()

    st.success("Los datos se han guardado correctamente.")
    st.markdown(SAVE_TEXT, unsafe_allow_html=True)

