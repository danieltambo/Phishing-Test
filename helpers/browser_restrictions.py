# 
# Deteccion que se ejecuta el Test desde un ordenador y no desde un movil
# Se hace con el ancho de pantalla (es la forma mas facil que permite Streamlit)
#
# Fuerza un ancho mínimo de viewport para garantizar condiciones homogéneas de visualización.
# Si la pantalla es inferior al umbral indicado, se muestra un overlay que bloquea la interacción.

import streamlit as st

def require_desktop(min_width: int = 1000):

    st.markdown(
        f"""
        <style>

        .desktop-block-overlay {{
            display: none;
        }}

        @media (max-width: {min_width}px) {{
            .desktop-block-overlay {{
                position: fixed;
                inset: 0;
                background: white;
                z-index: 999999;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                font-size: 22px;
                font-weight: 600;
                padding: 40px;
            }}
        }}

        </style>

        <div class="desktop-block-overlay">
        ⚠️ No es posible realizar este test desde un móvil o tablet.
        <br>
        Por favor, accede desde un ordenador.
        </div>
        """,
        unsafe_allow_html=True,
    )



