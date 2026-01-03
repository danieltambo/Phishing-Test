# helpers/gsheet.py

import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime



# -----------------------------
# Autenticación
# -----------------------------
def get_gsheet_client():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["google_service_account"],
        scopes=scopes
    )

    return gspread.authorize(creds)


# -----------------------------
# Abrir hoja
# -----------------------------
def open_sheet(sheet_name=None, sheet_id=None):
    if not sheet_name and not sheet_id:
        raise ValueError("Debes indicar sheet_name o sheet_id")

    gc = get_gsheet_client()

    if sheet_id:
        return gc.open_by_key(sheet_id)
    else:
        return gc.open(sheet_name)

def get_worksheet(sheet_id: str, worksheet_name: str):
    """
    Devuelve una worksheet concreta a partir del sheet_id
    """
    sh = open_sheet(sheet_id=sheet_id)
    return sh.worksheet(worksheet_name)

# --- LEGACY (wide format, no usar en PhD final) ---
def append_row(
    data: dict,
    sheet_name=None,
    sheet_id=None,
    worksheet_name=None,
    add_timestamp=True
):
    """
    data: dict con las respuestas
    """

    sh = open_sheet(sheet_name=sheet_name, sheet_id=sheet_id)
    ws = sh.worksheet(worksheet_name) if worksheet_name else sh.sheet1

    row = data.copy()

    if add_timestamp:
        row["timestamp"] = datetime.utcnow().isoformat()

    # --- CABECERAS ---
    headers = ws.row_values(1)

    # Si la hoja está vacía, crear cabeceras
    if not headers:
        headers = list(row.keys())
        ws.append_row(headers)

    # 🔑 Detectar nuevas columnas (claves no existentes)
    new_keys = [k for k in row.keys() if k not in headers]

    if new_keys:
        headers.extend(new_keys)
        ws.update('1:1', [headers])  # actualizar fila de cabecera

    # --- FILA ---
    values = [row.get(h, "") for h in headers]
    ws.append_row(values)

def save_responses(
    data: dict,
    sheet_name=None,
    sheet_id=None,
    worksheet_name=None,
    add_timestamp=True
):
    """
    Alias semántico de append_row para uso desde la app.
    """
    return append_row(
        data=data,
        sheet_name=sheet_name,
        sheet_id=sheet_id,
        worksheet_name=worksheet_name,
        add_timestamp=add_timestamp
    )

# --- LEGACY (events específico, sustituido por append_rows_dicts) ---
def append_events_old(
    events: list[dict],
    sheet_name=None,
    sheet_id=None,
    worksheet_name="events_raw"
):
    """
    Guarda una lista de eventos crudos en formato largo.
    Cada evento = una fila.
    """

    if not events:
        return

    sh = open_sheet(sheet_name=sheet_name, sheet_id=sheet_id)
    ws = sh.worksheet(worksheet_name)

    # Cabecera fija y controlada
    headers = [
        "session_id",
        "item_id",
        "event",
        "target",
        "timestamp",
        "duration", #es es para los hover_end
    ]

    # Crear cabecera si no existe
    existing_headers = ws.row_values(1)
    if not existing_headers:
        ws.append_row(headers)

    rows = []
    for e in events:
        rows.append([
            e.get("session_id", ""),
            e.get("item_id", ""),
            e.get("event", ""),
            e.get("target", ""),
            e.get("timestamp", ""),
            e.get("duration",""),
        ])

    # Escritura en bloque (importante para rendimiento)
    ws.append_rows(rows, value_input_option="RAW")

def append_row_dict(*, row: dict, sheet_id: str, worksheet_name: str):
    worksheet = get_worksheet(sheet_id, worksheet_name)

    # Leer cabeceras existentes (fila 1)
    headers = worksheet.row_values(1)

    # Si la hoja está vacía, inicializamos cabeceras
    if not headers:
        headers = list(row.keys())
        worksheet.append_row(headers)

    # Asegurar que todas las claves existen como columnas
    for key in row.keys():
        if key not in headers:
            headers.append(key)
            worksheet.update_cell(1, len(headers), key)

    # Construir fila en el orden de headers
    values = [row.get(h) for h in headers]
    worksheet.append_row(values)

def save_response_long(
    *,
    session_id: str,
    email: str | None,
    item_id: str,
    item_type: str,
    value,
    sheet_id: str,
    worksheet_name: str,
):
    row = {
        "session_id": session_id,
        "email": email,
        "item_id": item_id,
        "item_type": item_type,
        "value": value,
        "timestamp": datetime.utcnow().isoformat(),
    }

    append_row_dict(
        row=row,
        sheet_id=sheet_id,
        worksheet_name=worksheet_name,
    )

def append_rows_dicts(
    *,
    rows: list[dict],
    sheet_id: str,
    worksheet_name: str,
):
    if not rows:
        return

    worksheet = get_worksheet(sheet_id, worksheet_name)

    # 1. Cabeceras existentes
    headers = worksheet.row_values(1)

    # 2. Si la hoja está vacía, inicializamos con las claves del primer row
    if not headers:
        headers = list(rows[0].keys())
        worksheet.append_row(headers)

    # 3. Asegurar que todas las claves existen como columnas
    for row in rows:
        for key in row.keys():
            if key not in headers:
                headers.append(key)
                worksheet.update_cell(1, len(headers), key)

    # 4. Construir filas respetando el orden de headers
    values = [
        [row.get(h, "") for h in headers]
        for row in rows
    ]

    # 5. Escritura en bloque
    worksheet.append_rows(values, value_input_option="USER_ENTERED")
