# -------------------------------------------------
# Definición del flujo y estados del test.
# Este archivo actúa como contrato del flujo 
# -------------------------------------------------


# -------------------------------------------------
# Estados del flujo.
# Definen las fases posibles del test y su orden lógico.
# Actúan como contrato compartido entre módulos.
# -------------------------------------------------

INTRO = "INTRO"
ITEMS = "ITEMS"
CONTEXT = "CONTEXT"
SAVE = "SAVE"

# -------------------------------------------------
# Lista completa de estados válidos del sistema.
# -------------------------------------------------
ALL_STATES = [
    INTRO,
    ITEMS,
    CONTEXT,
    SAVE,
]


# -------------------------------------------------
# Mapa de estados
# Asocia cada estado con su función de render correspondiente.
# -------------------------------------------------

def build_state_map(
    render_intro,
    render_items,
    render_context,
    render_save,
):
    return {
        INTRO: render_intro,
        ITEMS: render_items,
        CONTEXT: render_context,
        SAVE: render_save,
    }
