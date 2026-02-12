import streamlit as st
from helpers.browser_restrictions import require_desktop  # o el nombre final que hayas elegido

st.set_page_config(layout="wide")

st.title("Test de restricción por viewport")

# Llamada al helper (solo una vez, al inicio)
require_desktop(min_width=900)

st.success("✅ Si ves este mensaje en pantalla completa, estás en modo desktop.")

st.write("Reduce el ancho de la ventana por debajo de 1000px y recarga.")

st.write("Ancho actual del viewport según CSS media query")

st.markdown("""
<style>
body::after {
    content: "Viewport width: " attr(data-width);
}
</style>
""", unsafe_allow_html=True)
