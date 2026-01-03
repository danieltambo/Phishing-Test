import streamlit as st
from helpers.flow_helpers import init_flow, render_current_state
from helpers.session import init_session
from helpers.ui_layout import  render_layout
from flow import build_state_map, INTRO, CONTEXT
from renders import render_intro, render_items, render_context, render_save


STATE_MAP = build_state_map(
    render_intro,
    render_items,
    render_context,
    render_save,
)


def main():
    init_session() # Sesion_id es una variable global
    init_flow(INTRO)
    render_layout()
    render_current_state(STATE_MAP)

if __name__ == "__main__":
    main()


