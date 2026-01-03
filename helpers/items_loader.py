# helpers/items_loader.py

from config import ITEMS_PL_DIR

def load_pl_items():
    files = sorted(ITEMS_PL_DIR.glob("*.html"))
    return [
        {
            "item_id": f.stem,   # ITEM001_DECATHLON
            "path": f,
        }
        for f in files
    ]

def load_item_html(item):
    return item["path"].read_text(encoding="utf-8")
