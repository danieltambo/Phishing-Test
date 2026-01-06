# Arquitectura del instrumento Phishing Identification Instrument

## 1. Modelo mental general

La aplicación es un test experimental implementado en Streamlit,
organizado como una máquina de estados secuencial.

El flujo experimental es:
1. Intro
2. Evaluación de ítems (phishing vs legítimo)
3. Preguntas de contexto
4. Guardado de respuestas y eventos

## 2. Flujo de estados

El estado actual de la aplicación se guarda en `st.session_state["state"]`.

La transición entre estados es estrictamente secuencial.
No se permite avanzar si no se cumplen las condiciones del estado actual.

## 3. Gestión de ítems

Los ítems P/L se cargan una sola vez por sesión.
Cada ítem es un HTML renderizado en un iframe controlado.

La lógica de avance se basa en un índice interno:
- `_items`
- `_item_index`

## 4. Captura de comportamiento (event_logger)

Las interacciones del usuario se capturan mediante un componente
custom de Streamlit (event_logger).

Los eventos se almacenan como secuencias temporales
para análisis posterior (RT, patrones, HMM, etc.).

## 5. Persistencia de datos

Los datos se almacenan en Google Sheets:
- responses: decisiones del usuario
- events: eventos de interacción
- contact_info: datos opcionales del participante

## 6. Convenciones importantes

- Todos los timestamps se almacenan como Unix time en milisegundos (UTC)
- No se usan fechas en formato legible en persistencia
- Las conversiones a formato humano se hacen a posteriori
