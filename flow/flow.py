# -------------------------
# Estados (contrato mínimo)
# -------------------------

INTRO = "INTRO"
ITEMS = "ITEMS"
CONTEXT = "CONTEXT"
SAVE = "SAVE"

ALL_STATES = [
    INTRO,
    ITEMS,
    CONTEXT,
    SAVE,
]


# -------------------------
# Máquina de estados
# -------------------------

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
