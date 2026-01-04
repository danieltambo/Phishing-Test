# -------------------------------------------------
# Utilidades mínimas para el manejo de eventos.
# Encapsula la lógica de interpretación de eventos
# para simplificar el código de la aplicación principal.
# -------------------------------------------------

# -------------------------------------------------
# Identifica si un evento corresponde a una decisión
# explícita del usuario (phishing vs legítimo).
# Se utiliza para detectar el cierre lógico de un ítem.
# -------------------------------------------------

def is_decision_event(event: dict) -> bool:
    return (
        event.get("event") == "click" and
        event.get("target") in {"decision_phishing", "decision_legitimo"}
    )

# -------------------------------------------------
# Identifica si un evento corresponde a la acción
# de avanzar  al siguiente ítem.
# -------------------------------------------------

def is_next_event(event: dict) -> bool:
    return (
        event.get("event") == "click" and
        event.get("target") == "next_item"
    )

# -------------------------------------------------
# Extrae la decisión semántica a partir de un evento.
# Traduce el target técnico del click a una etiqueta
# de decisión normalizada para el análisis.
# -------------------------------------------------

def extract_decision(event: dict) -> str | None:
    if event.get("target") == "decision_phishing":
        return "phishing"
    if event.get("target") == "decision_legitimo":
        return "legitimo"
    return None
