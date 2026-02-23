# -------------------------------------------------
# Textos y contenidos estáticos de la interfaz.
# Centraliza títulos, textos informativos y
# preguntas de contexto del estudio.
# -------------------------------------------------


# -------------------------------------------------
# Definición de headers por pantalla.
# Asocia cada estado del flujo con el título
# mostrado en el header de la interfaz.
# -------------------------------------------------

HEADERS = {
    "INTRO": {
        "title": " ¿Serías capaz de identificar un correo engañoso (phishing)?"
    },
    "ITEMS": {
        "title": "¿Cómo clasificarías este mensaje?"
    },
  
  "CONTEXT": {
          "title": "Preguntas finales"
      },
  
  "SAVE": {
          "title": "Gracias por participar"
      },

}


# -------------------------------------------------
# Texto introductorio del estudio.
# Se muestra al inicio e informa sobre el objetivo, dinámica y contexto de la investigación.
# -------------------------------------------------

INTRO_TEXT = """
<div style="font-size:1.1rem; line-height:1.6;">
  Te invitamos a participar en un estudio de investigación de la universidad
  sobre cómo las personas interpretan correos electrónicos engañosos (<em>phishing</em>).
</div>

<hr style="margin:0.8rem 0; border:0; border-top:1px solid #e5e7eb;">

<strong>¿En qué consiste este estudio?</strong>
<ul>
  <li>Verás una serie de <strong>correos electrónicos</strong>, similares a los que podrías recibir habitualmente.</li>
  <li>En cada caso, deberás indicar si crees que se trata de un <strong>correo engañoso <em>(phishing)</em></strong> o un correo normal.</li>
  <li>No es un examen: responde <strong>cómo lo harías en tu día a día. </strong></li>
</ul>

<ul>
  La duración aproximada es de <strong>10 minutos</strong>.
</ul>

<em>
Proyecto de doctorado en Psicología y Salud – Universitat Oberta de Catalunya (UOC)<br>
Contacto: Daniel de la Fuente Tambo – 
<a href="mailto:ddela_fuente@uoc.edu">ddela_fuente@uoc.edu</a>
</em>

"""

# -------------------------------------------------
# Texto de consentimiento informado.
# Resume las condiciones de participación, uso de datos y confidencialidad.
# -------------------------------------------------

CONSENT_TEXT = """
- Este estudio forma parte de un proyecto de investigación de la **Universitat Oberta de Catalunya (UOC)** y está en fase de desarrollo.
- Tu participación es **voluntaria** y puedes abandonar el estudio en cualquier momento sin dar explicaciones.
- Las respuestas se utilizarán **exclusivamente con fines de investigación**.
- Los datos serán tratados de forma **confidencial y anonimizada**.
- No se recogerán datos con fines comerciales ni se cederán a terceros.

Si tienes cualquier duda sobre el estudio, puedes contactar con el equipo investigador.
"""

# -------------------------------------------------
# Texto informativo para la recogida opcional del correo electrónico del participante.
# -------------------------------------------------

MAIL_TEXT = """
Si deseas recibir información general sobre el estudio o resultados agregados, puedes dejar tu correo electrónico. Este dato no se vinculará a tus respuestas.
"""

# -------------------------------------------------
# Texto introductorio del bloque de contexto.
# Indica el cierre de la parte principal del estudio y prepara al participante para el cuestionario final.
# -------------------------------------------------

CONTEXT_INTRO_TEXT = """
<strong>Has terminado la parte principal del estudio.</strong><br>
Solo quedan unas preguntas muy rapidas (1 min) <br>
No hay respuestas correctas o incorrectas: nos interesa tu opinión.<br>
"""

# -------------------------------------------------
# Definición de las preguntas de contexto (CTX).
# Cada pregunta se define mediante un diccionario que especifica identificador, texto y tipo de respuesta.
# -------------------------------------------------

CONTEXT_QUESTIONS = [
    # Cada entrada define una pregunta de contexto con:
    # - id: identificador único (CTX_xx)
    # - question: texto mostrado al participante
    # - type: tipo de respuesta (choice, likert_5, etc.)
    # - options / anchors: configuración específica del tipo

    {
        "id": "CTX_01",
        "question": "1. Suelo recibir aproximadamente este número de correos electrónicos al día.",
        "type": "choice",
        "options": ["0–20", "21–50", "51–100", "Más de 100"]
    },
    {
        "id": "CTX_02",
        "question": "2. Suelo leer o responder correos desde el teléfono móvil.",
        "type": "choice",
        "options": ["Nunca", "A veces", "A menudo",  "Siempre"]
        #"type": "likert_5",
    },
    {
        "id": "CTX_03",
        "question": "3. Cuándo estoy en reuniones o en llamadas, suelo responder correos electrónicos.",
        "type": "choice", 
        "options": ["Nunca", "A veces", "A menudo",  "Siempre"]
    },
    {
        "id": "CTX_04",
        "question": "4. Mi organización realiza simulaciones de phishing.",
        "type": "choice",
        "options": ["Sí", "No", "No lo sé", "No trabajo en una organización"]
    },
    {
        "id": "CTX_05",
        "question": "5. Cuándo sospecho que un correo puede ser engañoso, lo primero que hago es:",
        "type": "choice",
        "options": [
            "Ignorarlo",
            "Eliminarlo",
            "Consultarlo con un compañero",
            "Reportarlo a través del canal oficial"
        ]
    },
    {
        "id": "CTX_06",
        "question": "6. Cuando recibo un correo de mi superior, siento presión por responder rápido.",
        "type": "choice",
        "options": ["No me influye", "Me influye en parte", "Me influye claramente"]
    },
    {
        "id": "CTX_07",
        "question": "7. ¿Alguna vez has sufrido un fraude digital (por ejemplo, phishing, estafa online, suplantación de identidad)?",
        "type": "choice",
        "options": ["Sí", "No", "No estoy seguro"]
    },
    {
        "id": "CTX_08",
        "question": "8. Considero que soy capaz de reconocer cuando un correo es malicioso ",
        "type": "likert_5",
        "anchors": ["Nada capaz", "Muy capaz"]
    },
    {
        "id": "CTX_09",
        "question": "9. En este estudio, creo que he identificado correctamente los correos.",
        "type": "choice",
        "options": ["En todos o casi todos", "En algunos", "En unos pocos correos o ninguno", "No lo sé"]
    },
    {
        "id": "CTX_10",
        "question": "10. Me considero vulnerable frente a correos engañosos.",
        "type": "choice", 
        "options": ["Nada", "Algo", "Bastante",  "Mucho"]
    },
    {
        "id": "CTX_11",
        "question": "11. Edad:",
        "type": "choice", 
        "options": ["18–30", "31–45", "46–60",  "61 o más"]
    },
    {
        "id": "CTX_12",
        "question": "12. Género:",
        "type": "choice", 
        "options": ["Mujer", "Hombre", "No binario", "Prefiero no decirlo"]
    },
    {
        "id": "CTX_13",
        "question": "13. Rol principal en el trabajo:",
        "type": "choice", 
        "options": ["Técnico / Especialista", "Administrativo", "Atención al público / Comercial",  "Gestión o Dirección", "No trabajo actualmente", "Otro"]
    },



]

# -------------------------------------------------
# Texto de cierre del estudio.
# Se muestra tras finalizar el test y confirmar que las respuestas han sido registradas.
# -------------------------------------------------
SAVE_TEXT = """
Tu participación contribuirá a un proyecto de investigación sobre cómo las personas interpretan correos electrónicos engañosos.

El estudio se encuentra en fase de desarrollo, por lo que los datos se analizarán de forma agregada con fines exclusivamente científicos.

Si has facilitado tu correo electrónico, podrás recibir información general sobre el estudio o sobre los resultados globales en el futuro.
"""
