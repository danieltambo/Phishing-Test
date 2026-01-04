# -------------------------------------------------
# Utilidades para la carga de ítems Phishing / Legítimos.
# Se encarga de localizar los archivos HTML de los ítems
# y preparar su representación para el flujo del test.
# -------------------------------------------------

from config import ITEMS_PL_DIR

# -------------------------------------------------
# Carga la lista de ítems P/L disponibles.
# Cada ítem se representa como un diccionario con:
# - item_id: identificador derivado del nombre del archivo
# - path: ruta al archivo HTML del ítem
# -------------------------------------------------

# -------------------------------------------------
# Estructura de los ítems P/L cargados.
# La función devuelve una lista de diccionarios, uno por cada archivo HTML de ítem disponible.
#
# Ejemplo de estructura:
# [
#     {
#         "item_id": "ITEM001_DECATHLON",
#         "path": Path(".../items/PL/ITEM001_DECATHLON.html"),
#     },
#     ...
# ]
# -------------------------------------------------

def load_pl_items():
    files = sorted(ITEMS_PL_DIR.glob("*.html"))
    return [
        {
            # El identificador del ítem se deriva del nombre del archivo HTML
            "item_id": f.stem,   # ITEM001_DECATHLON
            "path": f,
        }
        for f in files
    ]


# -------------------------------------------------
# Carga el contenido HTML de un ítem.
# Asume que el ítem contiene una clave "path"
# apuntando al archivo HTML correspondiente.
# -------------------------------------------------

def load_item_html(item):
    return item["path"].read_text(encoding="utf-8")
