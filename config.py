# -------------------------------------------------
# Archivo de configuración global del instrumento.
# Centraliza constantes, rutas del proyecto y
# convenciones compartidas por toda la aplicación.
# -------------------------------------------------

from pathlib import Path

# ID de la Google Sheet - es el Phising_test_log
GSHEET_ID = "1bH3O0TdAi0SZX39f_flRtZo9fLEjk6zHhPPsPI5Ieys"   

# Hojas donde se grabaran las respuestas y los eventos
CONTACT_INFO_SHEET = "contact_info"
RESPONSES_SHEET = "responses"
EVENTS_SHEET = "events_raw"

# -------------------------------------------------
# Ruta base del proyecto.
# Se utiliza para construir rutas absolutas y garantizar
# compatibilidad entre ejecución local y en cloud.
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# -------------------------------------------------
# Directorio de los ítems Phishing / Legítimos.
# Se define mediante ruta absoluta anclada al proyecto
# para evitar problemas de working directory.
# -------------------------------------------------

ITEMS_PL_DIR = BASE_DIR / "items" / "PL"

# -------------------------------------------------
# Convención de timestamps del sistema.
# Todos los tiempos se almacenan como Unix time en
# milisegundos (UTC): ms desde 01-01-1970.
# -------------------------------------------------

