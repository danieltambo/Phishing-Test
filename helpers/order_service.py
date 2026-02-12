# -------------------------------------------------
# Servicio de generación de orden experimental.
# Controla la lógica de randomización de ítems
# respetando reglas de diseño experimental:
#
# - Primer ítem fijo (no se modifica)
# - Bloques por dificultad (bajo → medio → alto)
# - Random puro dentro de cada bloque
# - Restricción de canal: no dos SMS/WhatsApp seguidos
# - Restricción aplicada también entre bloques
# -------------------------------------------------

import random


# -------------------------------------------------
# Canales considerados "rápidos" (mayor priming).
# Se evita que aparezcan consecutivamente.
# -------------------------------------------------

FAST_CHANNELS = {"sms", "whatsapp"}


# -------------------------------------------------
# Función principal de randomización.
# Recibe la lista completa de ítems y devuelve
# una nueva lista ordenada según reglas experimentales.
# -------------------------------------------------

def random_items(items: list[dict]) -> list[dict]:

    # --- 1️⃣ Primer ítem fijo ---
    # Se mantiene como elemento inicial para
    # facilitar aprendizaje y adaptación del usuario.
    first_item = items[0]

    # El resto de ítems sí se reorganiza
    rest = items[1:]

    # --- 2️⃣ Agrupación por dificultad ---
    # Se respeta progresión cognitiva:
    # bajo → medio → alto
    bajo = [i for i in rest if i["difficulty"] == "bajo"]
    medio = [i for i in rest if i["difficulty"] == "medio"]
    alto = [i for i in rest if i["difficulty"] == "alto"]

    # --- 3️⃣ Random puro dentro de cada bloque ---
    # shufle es barajar :)
    
    random.shuffle(bajo)
    random.shuffle(medio)
    random.shuffle(alto)

    # Concatenación estructurada por bloques
    ordered = bajo + medio + alto

    # --- 4️⃣ Aplicación de restricción de canal ---
    # Se evita que haya dos SMS/WhatsApp consecutivos,
    # incluyendo la transición desde el primer ítem fijo.
    ordered = enforce_channel_constraint(
        ordered,
        previous_channel=first_item["canal"]
    )

    # --- 5️⃣ Reconstrucción final ---
    return [first_item] + ordered


# -------------------------------------------------
# Aplica restricción de canal sobre una secuencia.
# Si detecta conflicto, busca más adelante un ítem
# compatible y realiza intercambio local.
# -------------------------------------------------

def enforce_channel_constraint(
    items: list[dict],
    previous_channel: str | None = None
) -> list[dict]:

    items = items.copy()

    for i in range(len(items)):

        current_channel = items[i]["canal"].lower()

        # Si existe conflicto con el canal previo
        if previous_channel and conflict(previous_channel, current_channel):

            swap_index = find_compatible_index(
                items,
                start_index=i,
                previous_channel=previous_channel
            )

            # Si se encuentra candidato compatible, intercambiar
            if swap_index is not None:
                items[i], items[swap_index] = items[swap_index], items[i]

        # Actualizar canal previo para siguiente iteración
        previous_channel = items[i]["canal"].lower()

    return items


# -------------------------------------------------
# Determina si dos canales generan conflicto.
# Conflicto = ambos pertenecen a FAST_CHANNELS.
# -------------------------------------------------

def conflict(prev_channel: str, current_channel: str) -> bool:

    return (
        prev_channel in FAST_CHANNELS
        and current_channel in FAST_CHANNELS
    )


# -------------------------------------------------
# Busca un ítem posterior compatible para intercambio.
# Recorre la lista desde start_index + 1 hasta final.
# Devuelve índice si encuentra candidato válido.
# -------------------------------------------------

def find_compatible_index(
    items: list[dict],
    start_index: int,
    previous_channel: str
) -> int | None:

    for j in range(start_index + 1, len(items)):

        candidate_channel = items[j]["canal"].lower()

        if not conflict(previous_channel, candidate_channel):
            return j

    # Si no encuentra candidato compatible
    return None
