# -------------------------------------------------
# Servicio de agregación de respuestas.
# Unifica las respuestas de ítems experimentales
# y preguntas de contexto en un único formato.
# -------------------------------------------------

# -------------------------------------------------
# Se importan las respuestas de ítems P/L y de
# contexto para construir una salida homogénea.
# -------------------------------------------------

from helpers.item_service import  get_item_responses
from helpers.context_service import get_context_responses



# -------------------------------------------------
# Devuelve todas las respuestas del estudio.
# Combina respuestas de ítems P/L y de contexto
# en un único listado listo para persistencia.
# -------------------------------------------------

def get_all_responses():

    return (
        get_item_responses()
        + get_context_responses()
    )
