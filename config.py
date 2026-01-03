
#config.py
from pathlib import Path

# ID de la Google Sheet - es el cuestionario_expertos_respuestas
GSHEET_ID = "1bH3O0TdAi0SZX39f_flRtZo9fLEjk6zHhPPsPI5Ieys"   

# Hoja donde se grabaran las respuestas y los eventos
RESPONSES_SHEET = "responses_long"
EVENTS_SHEET = "events_raw"
CONTACT_INFO_SHEET = "contact_info"

# Base del proyecto (raíz)
BASE_DIR = Path(__file__).resolve().parent

# Directorio donde se encuetran los html de los items P/L
# ITEMS_PL_DIR = Path("items/pl")
ITEMS_PL_DIR = BASE_DIR / "items" / "pl"
