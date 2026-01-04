# -------------------------------------------------
# Fachada del módulo renders.
# Expone de forma explícita las funciones de render
# asociadas a cada fase del flujo experimental.
# -------------------------------------------------

# -------------------------------------------------
# Importación de renders por fase.
# Cada función encapsula el renderizado de una
# pantalla específica del flujo del test.
# -------------------------------------------------
from .render_intro import render_intro
from .render_items import render_items
from .render_context import render_context
from .render_save import render_save


# -------------------------------------------------
# API pública del módulo renders.
# Define explícitamente qué funciones de render están disponibles para el resto de la aplicación.
# -------------------------------------------------
__all__ = [
    "render_intro",
    "render_items",
    "render_context",
    "render_save",
]
