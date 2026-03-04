import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON INSTITUCIONAL
# ==========================================
# Usamos el escudo municipal como identidad en la pestaña del navegador
st.set_page_config(page_title="La Serena SmartCity", page_icon="logo_muni.png", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: COMPRESIÓN Y VIDRIO
# ==========================================
st.markdown("""
    <style>
    .block-container { padding-top: 1.5rem; padding-bottom: 0rem; }
    .stApp { background-color: #FFFFFF; }
    
    /* Cabecera sincronizada a 80px */
    .header-text-container { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    .header-title { color: #D32F2F; font-size: 2.1em; font-weight: bold; margin: 0; line-height: 1.1; }
    .header-subtitle { color: #666; font-size: 1.1em; margin: 0; line-height: 1.2; }

    /* Logos equilibrados */
    .logo-img { height: 80px; width: auto; object-fit: contain; }
    .logo-innovacion { mix-blend-mode: multiply; filter: contrast(110%); }

    /* Grilla 3x3 Ultra-Compacta */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        padding: 10px 0;
    }

    .mosaico-card {
        border-radius: 15px;
        padding: 20px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 165px; 
        backdrop-filter: blur(10px);
        background: linear-gradient(135deg, #D32F2F 0%, #9A1B1B 100%);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.15);
        transition: all 0.3s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(211, 47, 47, 0.35);
        filter: brightness(1.2);
    }
    
    .card-desactivada {
        background: rgba(233, 236, 239, 0.95) !important;
        color: #ADB5BD !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc { color: #ADB5BD !important; }

    .card-icon { font-size: 3em; margin-bottom: 8px; color: white !important; }
    .card-title { font-size: 1.4em; font-weight: bold; margin-bottom: 5px; color: white !important; }
    .card-desc { font-size: 0.95em; opacity: 0.9; line-height: 1.2; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA COMPRIMIDA (PROPORCIÓN 80px)
# ==========================================
col_info, col_logo1, col_logo2 = st.columns([1.8, 0.6, 0.6])

with col_info:
    st.markdown("""
        <div class="header-text-container">
            <div class="header-title">La Serena SmartCity</div>
            <div class="header-subtitle">Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</div>
        </div>
    """, unsafe_allow_html=True)

with col_logo1:
    # Logo Municipal cargado desde la raíz de GitHub
    st.image("logo_muni.png", width=130)

with col_logo2:
    # Logo Innovación cargado desde la raíz de GitHub
    st.image("logo_innovacion.png", width=130)

st.divider()

# ==========================================
# 4. EL MOSAICO 3x3 (DIRECCIONES REALES)
# ==========================================
servicios = [
    {
        "icon": "🏢", 
        "title": "Acceso Consistorial", 
        "desc": "Seguridad y registro digital de visitas municipales.", 
        "dev": False, 
        "link": "https://puertaserena.streamlit.app" # CONECTADO
    },
    {
        "icon": "🌐", 
        "title": "Portal RDMLS", 
        "desc": "Plataforma ciudadana y georeferenciación interactiva.", 
        "dev": False, 
        "link": "https://rdmls.cl" # Placeholder: Cambiar por la real si es distinta
    },
    {
        "icon": "📡", 
        "title": "Sentinel Faro", 
        "desc": "Social Listening y monitoreo inteligente comunal.", 
        "dev": False, 
        "link": "#"
    },
    {
        "icon": "🎙️", 
        "title": "Radio Digital RDMLS", 
        "desc": "Señal en vivo y programación de la Municipalidad.", 
        "dev": False, 
        "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena" # CONECTADO
    },
    {
        "icon": "🎭", 
        "title": "Protocolo y Eventos", 
        "desc": "Gestión institucional y coordinación de actos.", 
        "dev": False, 
        "link": "#"
    },
    {
        "icon": "🎓", 
        "title": "Inducción E-Learning", 
        "desc": "Capacitación digital para funcionarios municipales.", 
        "dev": False, 
        "link": "#"
    },
    {
        "icon": "📄", 
        "title": "Informes Honorarios", 
        "desc": "Generador automático de reportes de gestión.", 
        "dev": False, 
        "link": "#"
    },
    {
        "icon": "⛱️", 
        "title": "Playas y Humedales", 
        "desc": "EN DESARROLLO - MONITOREO AMBIENTAL", 
        "dev": True, 
        "link": "#"
    },
    {
        "icon": "🚦", 
        "title": "Monitoreo Urbano", 
        "desc": "EN DESARROLLO - TRÁNSITO Y BACHES", 
        "dev": True, 
        "link": "#"
    }
]

html_grid = "<div class='smart-grid'>"
for s in servicios:
    clase = "card-desactivada" if s["dev"] else "card-activa"
    url = s["link"]
    
    if s["dev"]:
        html_grid += f"""
        <div class='mosaico-card {clase}'>
            <div class='card-icon'>{s["icon"]}</div>
            <div class='card-title'>{s["title"]}</div>
            <div class='card-desc'>{s["desc"]}</div>
        </div>"""
    else:
        html_grid += f"""
        <a href='{url}' target='_blank' style='text-decoration: none;'>
            <div class='mosaico-card {clase}'>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </a>"""
html_grid += "</div>"

st.markdown(html_grid, unsafe_allow_html=True)
