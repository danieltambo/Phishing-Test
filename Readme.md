# Phishing Identification Instrument

Instrumento experimental implementado en **Streamlit** para evaluar la
capacidad de identificación de correos de phishing frente a correos legítimos,
así como el comportamiento de decisión asociado.

El test presenta estímulos HTML realistas y registra tanto la decisión final
del participante como eventos de interacción (event_logger).

---

## Descripción general

La aplicación implementa un flujo secuencial con cuatro fases:

1. Introducción
2. Evaluación de ítems (Phishing / Legítimo)
3. Preguntas de contexto
4. Guardado de respuestas y eventos

El estado de la aplicación se gestiona mediante una máquina de estados
explícita sobre `st.session_state`.

---

## Captura de comportamiento

Durante la evaluación de ítems, la interacción del usuario se registra
mediante un componente custom de Streamlit (event_logger), permitiendo
el análisis posterior de:

- tiempos de reacción
- patrones de exploración
- secuencias de decisión

---

## Persistencia de datos

Los datos se almacenan en Google Sheets, separados en:

- respuestas
- eventos de interacción
- información de contacto (opcional)

Todos los timestamps se guardan como **Unix time en milisegundos (UTC)**.

---

## Documentación técnica

Para una descripción detallada del diseño, flujo y decisiones de arquitectura,
ver:

➡️ **`ARCHITECTURE.md`**

---

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py
