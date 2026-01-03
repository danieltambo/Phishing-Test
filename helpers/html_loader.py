# helpers/html_loader.py
from pathlib import Path

def load_html(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def load_shared_html(filename: str) -> str:
    return load_html(Path("items/shared") / filename)
