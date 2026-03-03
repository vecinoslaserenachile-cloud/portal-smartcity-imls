import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON ROJO (🔴)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🔴", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: ROJO, BLANCO Y VIDRIO
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Grilla simétrica 3x3 para evitar huecos */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
        padding: 30px 0;
    }

    @media (max-width: 1000px) {
        .smart-grid { grid-template-columns: 1fr; }
    }
    
    /* Tarjeta Efecto Vidrio (Glassmorphism) */
    .mosaico-card {
        border-radius: 20px;
        padding: 30px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 220px;
        
        /* Glassmorphism sobre Rojo Municipal */
        backdrop-filter: blur(12px);
        background: linear-gradient(135deg, #D32F2F 0%, #9A1B1B 100%);
        border: 1px solid rgba(255, 255, 255, 0.3);
        
        box-shadow: 0 8px 32px 0 rgba(211, 47, 47, 0.2);
        transition: all 0.4s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(211, 47, 47, 0.4);
        filter: brightness(1.2);
    }
    
    /* Servicios EN DESARROLLO */
    .card-desactivada {
        background: rgba(233, 236, 239, 0.8) !important;
        color: #ADB5BD !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc { color: #ADB5BD !important; }

    .card-icon { font-size: 3.8em; margin-bottom: 15px; color: white !important; }
    .card-title { font-size: 1.6em; font-weight: bold; margin-bottom: 10px; line-height: 1.1; color: white !important; }
    .card-desc { font-size: 1.05em; opacity: 0.95; line-height: 1.3; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA (LOGOS EN RAÍZ)
# ==========================================
col_t, col_l = st.columns([1.8, 1.2])

with col_t:
    st.markdown("<h1 style='color: #D32F2F; margin-bottom: 0px;'>🔴 La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.25em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_l:
    # Equilibrio de logos cargando desde la raíz
    c1, c2 = st.columns(2)
    with c1:
        st.image("logo_muni.png", width=150) 
    with c2:
        st.image("logo_innovacion.png", width=150)

st.divider()

# ==========================================
# 4. EL MOSAICO 3x3 (9 SERVICIOS)
# ==========================================
# Se organiza la botonera completa para que nada se pierda.
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y registro digital de visitas municipales.", "dev": False, "link": "https://puertaserena.streamlit.app"},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación interactiva.", "dev": False, "link": "#"},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Sistema inteligente de Social Listening comunal.", "dev": False, "link": "#"},
    {"icon": "🎙️", "title": "Radio Digital RDMLS", "desc": "Señal en vivo y programación de la Municipalidad.", "dev": False, "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena"},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación de actos.", "dev": False, "link": "#"},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios municipales.", "dev": False, "link": "#"},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "dev": False, "link": "#"},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "EN DESARROLLO - MONITOREO AMBIENTAL", "dev": True, "link": "#"},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "EN DESARROLLO - TRÁNSITO Y BACHES", "dev": True, "link": "#"}
]

# Construcción de la grilla visual blindada
html_grid = "<div class='smart-grid'>"
for s in servicios:
    clase = "card-desactivada" if s["dev"] else "card-activa"
    url = s["link"] if not s["dev"] else "#"
    
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
