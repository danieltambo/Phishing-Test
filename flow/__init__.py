# -------------------------------------------------
# Fachada del módulo flow.
# Expone de forma controlada los estados del flujo
# y la función de construcción del mapa de estados.
# -------------------------------------------------

# -------------------------------------------------
# Reexportación explícita del contrato del flujo.
# Permite importar estados y utilidades del flujo
# desde el módulo flow sin acceder a su implementación.
# -------------------------------------------------
from .flow import (
    INTRO,
    ITEMS,
    CONTEXT,
    SAVE,
    build_state_map,
)

# -------------------------------------------------
# API pública del módulo flow.
# Limita explícitamente los símbolos accesibles
# al usar importaciones con comodines.
# -------------------------------------------------

__all__ = [
    "INTRO",
    "ITEMS",
    "CONTEXT",
    "SAVE",
    "build_state_map",
]
