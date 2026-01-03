# renders/render_items.py

import streamlit as st
from clickstream import clickstream  # Mi componente

from helpers.flow_helpers import go_to
from helpers.items_loader import load_pl_items, load_item_html
from helpers.html_loader import load_shared_html
from helpers.item_service import init_items, current_item, record_response, has_response, next_item, is_last, current_index, total_items
from helpers.clickstream_service import init_clickstream, push, freeze_item_events
from helpers.events import is_decision_event, extract_decision, is_next_event



def render_items():
    
    # 1️⃣ Inicialización idempotente
    items = load_pl_items()
    init_items(items)
    init_clickstream()

    #Esto es para debug, se tiene que borrar
    #st.write("DEBUG _items:", st.session_state.get("_items"))
    #st.write("DEBUG _item_index:", st.session_state.get("_item_index"))

    # 2️⃣ Ítem actual
    item = current_item()
    #st.caption(item["item_id"])

    i = current_index()
    total = total_items()
    st.caption(f"Ejercicio {i+1} de {total}")
    
    mail_html = load_item_html(item)
    decision_html = load_shared_html("decision_panel.html")
    full_html = mail_html + decision_html

    # 3️⃣ Render del componente
    event = clickstream(
       key=f"mail_{item['item_id']}",   #Pone la clave indexada al item_id para tener una clave unica y una iframe distinto en cada item
        html=full_html,
    )
    
    if event is None:
        return
    
    # 4️⃣ Evento crudo SIEMPRE
    push(event)

    # 5️⃣ Selección PHISHING / LEGIT
    if is_decision_event(event):
        decision = extract_decision(event)
        record_response(decision)
        return

    # 6️⃣ Botón “Siguiente”
    if is_next_event(event):

        if not has_response():
            st.warning("Selecciona Phishing o Legítimo antes de continuar")
            return

        # Esto es temporal
        #print("NEXT_ITEM for:", item["item_id"])
        freeze_item_events(item["item_id"])

        if is_last():
            go_to("CONTEXT")
        else:
            next_item()
            st.rerun()


    if event and event.get("event") != "decision":
        push(event)

