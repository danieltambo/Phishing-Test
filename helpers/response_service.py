# helpers/response_service.py

from helpers.item_service import  get_item_responses
from helpers.context_service import get_context_responses


def get_all_responses():
    """
    Devuelve todas las respuestas del estudio en formato homogéneo,
    listas para persistir.
    """
    return (
        get_item_responses()
        + get_context_responses()
    )
