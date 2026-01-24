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
        "title": "  ¿Serías capaz de identificar un correo phishing?"
    },
    "ITEMS": {
        "title": "¿Cómo clasificarías este mensaje?"
    },
  
  "CONTEXT": {
          "title": "Por último... ¿Cómo sueles responder a los correos?"
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
  <li>No es un examen: responde <strong>como lo harías en tu día a día. </strong></li>
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
<strong>Ya has terminado la parte principal del estudio.</strong><br>
Solo quedan una pocas preguntas muy rapidas (1 min) <br>
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
        "question": "2. Suelo leer o responder correos de la empresa desde el teléfono móvil - ",
        "type": "likert_5",
    },
    {
        "id": "CTX_03",
        "question": "3. Cuando estoy en reuniones o en llamadas, suelo responder correos electrónicos - ",
        "type": "likert_5",
    },
    {
        "id": "CTX_04",
        "question": "4. Mi organización realiza simulaciones o campañas de correos engañosos (por ejemplo, phishing).",
        "type": "choice",
        "options": ["Trimestral o más frecuente", "Anual", "Nunca",  "No sé si hacen simulaciones", "Sé que hacen simulaciones pero no con que frecuencia"]
    },
    {
        "id": "CTX_05",
        "question": "5. Si sospecho que un correo puede ser engañoso, suelo hacer lo siguiente:",
        "type": "choice",
        "options": [
            "Informarlo a la organización",
            "Borrarlo sin más",
            "Consultarlo con alguien",
            "No hago nada"
        ]
    },
    {
        "id": "CTX_06",
        "question": "6. Cuando recibo un correo de mi jefe o un correo que pide actuar con rapidez, me genera cierta inquietud - ",
        "type": "likert_5",
    },
    {
        "id": "CTX_07",
        "question": "7. Que yo sepa, he recibido alguna vez un correo engañoso (phishing).",
        "type": "choice",
        "options": ["Sí", "No", "No estoy seguro"]
    },
    {
        "id": "CTX_08",
        "question": "8. En general, me considero capaz de reconocer las señales de un correo engañoso - ",
        "type": "likert_5",
        "anchors": ["Nada capaz", "Muy capaz"]
    },
    {
        "id": "CTX_09",
        "question": "9. En este estudio, creo que he acertado al identificar si los correos eran engañosos o normales.",
        "type": "choice",
        "options": ["Todos o casi todos", "Algunos", "Aproximadamente la mitad", "No lo sé"]
    },
    {
        "id": "CTX_10",
        "question": "10. En general, me considero vulnerable frente a correos engañosos - ",
        "type": "likert_5",
        "anchors": ["Nada vulnerable", "Muy vulnerable"]
    },
]

# -------------------------------------------------
# Texto de cierre del estudio.
# Se muestra tras finalizar el test y confirmar que las respuestas han sido registradas.
# -------------------------------------------------
SAVE_TEXT = """
<strong>Gracias por tu participación.</strong><br><br>
Tus respuestas se han registrado correctamente y contribuirán a un proyecto de investigación sobre cómo las personas interpretan correos electrónicos engañosos.<br><br>
El estudio se encuentra en fase de desarrollo, por lo que los datos se analizarán de forma agregada con fines exclusivamente científicos.

Si has facilitado tu correo electrónico, podrás recibir información general sobre el estudio o sobre los resultados globales en el futuro.
"""
