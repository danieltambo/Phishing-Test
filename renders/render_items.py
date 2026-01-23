# -------------------------------------------------
# Render de los ítems P/L del estudio.
# Gestiona la presentación de cada correo, la captura de eventos (event_logger) y el registro de la decisión del participante.
# -------------------------------------------------

# -------------------------------------------------
# Dependencias del render de ítems.
# Incluye carga de estímulos HTML, gestión de estado, captura de eventos y control del flujo experimental.
# -------------------------------------------------
import streamlit as st
from event_logger import event_logger  # Mi componente

from helpers.flow_helpers import go_to
from helpers.items_loader import load_pl_items, load_item_html
from helpers.html_loader import load_shared_html
from helpers.item_service import init_items, current_item, record_response, has_response, next_item, is_last, current_index, total_items
from helpers.event_logger_service import init_event_logger, push, freeze_item_events
from helpers.events import is_decision_event, extract_decision, is_next_event


# -------------------------------------------------
# Renderiza un único ítem del test. 
# Esta función se ejecuta de forma reactiva y responde a los eventos emitidos por el componente.
# -------------------------------------------------

def render_items():
    
    # 1️⃣  Inicialización idempotente del servicio de ítems y del sistema de captura de eventos.
    items = load_pl_items()
    init_items(items)
    init_event_logger() 

    # 2️⃣ Recupera el ítem activo según el índice actual
    item = current_item()
    
    # Información de progreso para el participante
    i = current_index()
    total = total_items()
    st.caption(f"Mensaje {i+1} de {total}")
    

    # Composición del estímulo completo: correo HTML + panel de decisión
    mail_html = load_item_html(item)
    decision_html = load_shared_html("decision_panel.html")
    full_html = mail_html + decision_html

    # 3️⃣ Render del componente. Devuelve eventos de interacción del usuario.
    event = event_logger(
       key=f"mail_{item['item_id']}",   #Pone la clave indexada al item_id para tener una clave unica y una iframe distinto en cada item
        html=full_html,
    )

    # Es una prueba para ver si se visualizan los eventos
    # st.write("EVENT RAW:", event)

    # Si no hay evento, no se ejecuta ninguna lógica
    if event is None:
        return
    
    # 4️⃣ Registra SIEMPRE el evento crudo del ítem activo
    push(event)

    # 5️⃣ Evento de decisión: el usuario clasifica el correo como phishing o legítimo
    if is_decision_event(event):
        decision = extract_decision(event)
        record_response(decision)
        return

    # 6️⃣ # Evento de avance al siguiente ítem
    if is_next_event(event):

        # Evita avanzar si no existe decisión registrada
        if not has_response():
            st.warning("Selecciona Phishing o Legítimo antes de continuar")
            return

        # Congela los eventos del ítem actual y los añade al buffer global
        freeze_item_events(item["item_id"])

        # Si es el último ítem, se pasa al bloque de contexto
        if is_last():
            go_to("CONTEXT")

        else:
            # Avanza al siguiente ítem del test
            next_item()
            st.rerun()

    # BORRAR
    # Seguridad adicional para capturar eventos no relacionados con la decisión explícita
    #if event and event.get("event") != "decision":
    #    push(event)

