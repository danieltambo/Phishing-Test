# -------------------------------------------------
# Capa de acceso a datos (Google Sheets).
# Encapsula toda la lógica de autenticación,
# acceso y escritura en hojas de cálculo.
# -------------------------------------------------

import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import time


# -------------------------------------------------
# Autenticación con Google Sheets.
# Inicializa el cliente usando credenciales
# definidas en secrets.toml (Streamlit).
# -------------------------------------------------

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


# -------------------------------------------------
# Utilidades de acceso a hojas y worksheets.
# Permiten abrir documentos y hojas concretas
# de forma uniforme desde la aplicación.
# -------------------------------------------------

# -------------------------------------------------
# Abre un documento de Google Sheets.
# Permite identificarlo por nombre o por ID,
# pero exige que al menos uno esté definido.
# -------------------------------------------------

def open_sheet(sheet_name=None, sheet_id=None):
    if not sheet_name and not sheet_id:
        raise ValueError("Debes indicar sheet_name o sheet_id")

    gc = get_gsheet_client()

    if sheet_id:
        return gc.open_by_key(sheet_id)
    else:
        return gc.open(sheet_name)


# -------------------------------------------------
# Obtiene una worksheet concreta dentro de un sheet.
# Aísla la lógica de acceso a hojas específicas
# usadas por el instrumento.
# -------------------------------------------------

def get_worksheet(sheet_id: str, worksheet_name: str):
    """
    Devuelve una worksheet concreta a partir del sheet_id
    """
    sh = open_sheet(sheet_id=sheet_id)
    return sh.worksheet(worksheet_name)


# -------------------------------------------------
# Añade una fila representada como diccionario.
# Garantiza consistencia de cabeceras y permite
# evolución dinámica del esquema.
# -------------------------------------------------

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


# -------------------------------------------------
# Guarda una respuesta individual en formato largo.
# Normaliza la estructura común a ítems experimentales
# y preguntas de contexto.
# -------------------------------------------------

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
        "timestamp": int(time.time() * 1000) # antiguo datetime.utcnow().isoformat(),
    }

    append_row_dict(
        row=row,
        sheet_id=sheet_id,
        worksheet_name=worksheet_name,
    )

# -------------------------------------------------
# Inserta múltiples filas en bloque.
# Optimiza la escritura en Google Sheets y
# asegura consistencia de cabeceras.
# -------------------------------------------------

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
