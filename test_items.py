import streamlit as st
from helpers.items_loader import load_pl_items, load_item_html
from helpers.html_loader import load_shared_html
from event_logger import event_logger
from helpers.event_logger_service import init_event_logger, push

st.set_page_config(layout="wide")

st.title("🔎 Debug Item Viewer")

# 1️⃣ Cargar todos los ítems
items = load_pl_items()
item_ids = [item["item_id"] for item in items]

# 2️⃣ Selector
selected_id = st.selectbox("Selecciona item", item_ids)

# 3️⃣ Buscar item concreto
item = next(i for i in items if i["item_id"] == selected_id)

# 4️⃣ Componer HTML
mail_html = load_item_html(item)
decision_html = load_shared_html("decision_panel.html")
full_html = mail_html + decision_html

# 5️⃣ Inicializar logger
init_event_logger()

# 6️⃣ Render
event = event_logger(
    key=f"debug_{item['item_id']}",
    html=full_html,
)

# 7️⃣ Mostrar evento crudo
if event:
    push(event)
    st.write("EVENT RAW:", event)
