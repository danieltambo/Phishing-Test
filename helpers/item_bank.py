# ==================================================
# ITEM BANK METADATA
# Contiene la información estructurada de cada ítem
# ==================================================

_ITEM_LIST = [

    # --- BAJO ---
    {"item_id": "01_Familia", "correct_answer": "phishing", "difficulty": "bajo", "channel": "whatsapp"},
    {"item_id": "02_AmazonUrgente", "correct_answer": "phishing", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "03_Decathlon", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "04_AEAT", "correct_answer": "phishing", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "05_Airbnb", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "06_Netflix", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "07_GoogleSMS", "correct_answer": "phishing", "difficulty": "bajo", "channel": "sms"},
    {"item_id": "08_UPS_Envio", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "10_BBVA", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "sms"},
    {"item_id": "12_Sabadell", "correct_answer": "phishing", "difficulty": "bajo", "channel": "sms"},
    {"item_id": "13_Nespresso", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "mail"},
    {"item_id": "14_Adobe", "correct_answer": "legitimo", "difficulty": "bajo", "channel": "mail"},

    # --- MEDIO ---
    {"item_id": "09_Dropbox", "correct_answer": "phishing", "difficulty": "medio", "channel": "mail"},
    {"item_id": "11_AdobeSign", "correct_answer": "phishing", "difficulty": "medio", "channel": "mail"},
    {"item_id": "15_GLS", "correct_answer": "phishing", "difficulty": "medio", "channel": "mail"},
    {"item_id": "16_GoogleDrive", "correct_answer": "legitimo", "difficulty": "medio", "channel": "drive"},
    {"item_id": "17_Iberdrola", "correct_answer": "phishing", "difficulty": "medio", "channel": "mail"},
    {"item_id": "18_Seur", "correct_answer": "phishing", "difficulty": "medio", "channel": "sms"},
    {"item_id": "19_GoogleAlert", "correct_answer": "legitimo", "difficulty": "medio", "channel": "mail"},
    {"item_id": "20_Starbucks", "correct_answer": "legitimo", "difficulty": "medio", "channel": "mail"},
    {"item_id": "22_UPS_Incidencia", "correct_answer": "phishing", "difficulty": "medio", "channel": "mail"},
    {"item_id": "24_AmazonCuenta", "correct_answer": "legitimo", "difficulty": "medio", "channel": "mail"},
    
    # --- ALTO ---
    {"item_id": "21_Apple", "correct_answer": "legitimo", "difficulty": "alto", "channel": "mail"},
    {"item_id": "23_CaixaBank", "correct_answer": "phishing", "difficulty": "alto", "channel": "mail"},
    {"item_id": "25_DeptFinazas", "correct_answer": "phishing", "difficulty": "alto", "channel": "drive"},
    {"item_id": "27_Shein", "correct_answer": "phishing", "difficulty": "alto", "channel": "mail"},
    {"item_id": "26_UPS_Entrega", "correct_answer": "legitimo", "difficulty": "alto", "channel": "sms"},
    {"item_id": "28_LinkedIn", "correct_answer": "phishing", "difficulty": "alto", "channel": "mail"},
    {"item_id": "29_DHL", "correct_answer": "legitimo", "difficulty": "alto", "channel": "whatsapp"},
    
]



# -------------------------------------------------
# Conversión automática a diccionario indexado
# por item_id para acceso rápido O(1)
# -------------------------------------------------

ITEM_BANK = {
    item["item_id"]: item
    for item in _ITEM_LIST
}