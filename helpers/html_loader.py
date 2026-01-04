# -------------------------------------------------
# Utilidades para la carga de fragmentos HTML.
# Centraliza la lectura de templates HTML desde
# el sistema de archivos.
# -------------------------------------------------

from pathlib import Path

# -------------------------------------------------
# Carga el contenido de un archivo HTML arbitrario.
# Se utiliza para leer ítems o fragmentos HTML
# desde una ruta explícita.
# -------------------------------------------------

def load_html(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# -------------------------------------------------
# Carga un fragmento HTML compartido.
# Asume una estructura fija bajo items/shared
# para componentes reutilizables.
# -------------------------------------------------

def load_shared_html(filename: str) -> str:
    return load_html(Path("items/shared") / filename)
