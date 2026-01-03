# helpers/events.py

# Logica minima sobre eventos para limpiar el codigo de la app principal

def is_decision_event(event: dict) -> bool:
    return (
        event.get("event") == "click" and
        event.get("target") in {"decision_phishing", "decision_legitimo"}
    )

def is_next_event(event: dict) -> bool:
    return (
        event.get("event") == "click" and
        event.get("target") == "next_item"
    )

def extract_decision(event: dict) -> str | None:
    if event.get("target") == "decision_phishing":
        return "phishing"
    if event.get("target") == "decision_legitimo":
        return "legitimo"
    return None
