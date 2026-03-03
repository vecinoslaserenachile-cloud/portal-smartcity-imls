import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON CIUDAD (🏙️)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏙️", layout="wide")

# ==========================================
# 2. ESTILOS CSS: GRILLA INTELIGENTE TOTAL
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    /* Grilla fluida que elimina huecos a la derecha */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 25px;
        padding: 20px 0;
    }
    
    .smart-card {
        border-radius: 15px;
        padding: 25px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 190px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: none;
    }
    
    .smart-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    .card-icon { font-size: 3.5em; margin-bottom: 12px; }
    .card-title { font-size: 1.4em; font-weight: bold; margin-bottom: 10px; color: white !important; }
    .card-desc { font-size: 1em; opacity: 0.95; line-height: 1.5; color: white !important; }
    
    .card-proximo {
        background-color: #E9ECEF !important;
        color: #ADB5BD !important;
        border: 2px dashed #CED4DA;
        box-shadow: none !important;
        cursor: default;
    }
    .card-proximo .card-title, .card-proximo .card-desc { color: #ADB5BD !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON ESPACIO PARA 2 LOGOS
# ==========================================
col_t, col_l = st.columns([2, 1])

with col_t:
    st.markdown("""
        <h1 style='color: #003366; margin-bottom: 0px;'>🏙️ La Serena SmartCity</h1>
        <p style='color: #666; font-size: 1.1em; margin-top: -5px;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>
    """, unsafe_allow_html=True)

with col_l:
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Escudo_de_La_Serena.svg/800px-Escudo_de_La_Serena.svg.png", use_container_width=True) 
    with c2:
        st.image("https://via.placeholder.com/300x100/FFFFFF/003366?text=Innovacion+Mundial", use_container_width=True)

st.divider()

# ==========================================
# 4. REPRODUCTOR RADIO RDMLS (ZONA SUPERIOR)
# ==========================================
st.markdown("<h3 style='color: #D62828;'>📻 Señal en Vivo: Radio Digital Municipal La Serena</h3>", unsafe_allow_html=True)

iframe_radio = """
<iframe src="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena/embed" 
        frameborder="0" allowtransparency="true" 
        style="width: 100%; min-height: 150px; border: 0; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 30px;">
</iframe>
"""
st.markdown(iframe_radio, unsafe_allow_html=True)

# ==========================================
# 5. ESTRUCTURA DE DATOS (SERVICIOS)
# ==========================================
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y bitácora digital de visitas para el recinto municipal.", "bg": "#1E6091", "link": "https://puertaserena.streamlit.app", "prox": False},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana interactiva con radio y georeferenciación.", "bg": "#D62828", "link": "#", "prox": False},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Sistema inteligente de Social Listening y monitoreo comunal.", "bg": "#7209B7", "link": "#", "prox": False},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y eventos de la municipalidad.", "bg": "#2A9D8F", "link": "#", "prox": False},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generación automática de reportes de gestión mensual.", "bg": "#38B000", "link": "#", "prox": False},
    {"icon": "🚌", "title": "Smart Tránsito LS", "desc": "Monitoreo de flujo vehicular y rutas inteligentes.", "bg": "#FFF", "link": "#", "prox": True}
]

# ==========================================
# 6. RENDERIZADO DE LA GRILLA (SOLUCIÓN WTF)
# ==========================================
# Construimos toda la grilla en un solo bloque para evitar fugas de código
html_final = "<div class='smart-grid'>"
for s in servicios:
    clase = "card-proximo" if s["prox"] else ""
    url = s["link"] if not s["prox"] else "#"
    
    html_final += f"""
    <a href='{url}' target='_blank' style='text-decoration: none;'>
        <div class='smart-card {clase}' style='background-color: {s["bg"]};'>
            <div>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </div>
    </a>
    """
html_final += "</div>"

# El secreto está en este comando: unsafe_allow_html=True
st.markdown(html_final, unsafe_allow_html=True)
