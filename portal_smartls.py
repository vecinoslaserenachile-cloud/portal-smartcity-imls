import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON DISTINTIVO (🌐)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🌐", layout="wide")

# ==========================================
# 2. ESTILOS: EFECTO VIDRIO (GLASSMORPHISM)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    /* Grilla simétrica 3x3 */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px 0;
    }

    @media (max-width: 800px) {
        .smart-grid { grid-template-columns: 1fr; }
    }
    
    .mosaico-card {
        border-radius: 20px;
        padding: 30px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 200px;
        
        /* Efecto Vidrio */
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.1); 
        border: 1px solid rgba(255, 255, 255, 0.2);
        
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    .card-desactivada {
        background: rgba(233, 236, 239, 0.6) !important;
        color: #ADB5BD !important;
        border: 2px dashed #CED4DA;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc { color: #ADB5BD !important; }

    .card-icon { font-size: 3.5em; margin-bottom: 12px; }
    .card-title { font-size: 1.5em; font-weight: bold; margin-bottom: 8px; color: white; }
    .card-desc { font-size: 1em; opacity: 0.9; line-height: 1.3; color: white; }
    
    /* Control de logos en cabecera */
    .header-logo {
        max-height: 90px;
        width: auto;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON LOGOS DESDE LA RAÍZ
# ==========================================
col_titulo, col_logos = st.columns([2, 1.2])

with col_titulo:
    st.markdown("<h1 style='color: #003366; margin-bottom: 0px;'>🌐 La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.2em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_logos:
    c1, c2 = st.columns(2)
    with c1:
        # Cargamos logo municipal (rojo) desde la raíz
        st.image("logo_muni.png", width=150) 
    with c2:
        # Cargamos logo innovación desde la raíz
        st.image("logo_innovacion.png", width=150)

st.divider()

# ==========================================
# 4. EL MOSAICO 3x3 (9 SERVICIOS)
# ==========================================
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y bitácora digital de visitas.", "bg": "linear-gradient(135deg, #1E6091 0%, #114871 100%)", "link": "https://puertaserena.streamlit.app", "dev": False},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación.", "bg": "linear-gradient(135deg, #D62828 0%, #A31B1B 100%)", "link": "#", "dev": False},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo comunal.", "bg": "linear-gradient(135deg, #7209B7 0%, #5A0693 100%)", "link": "#", "dev": False},
    {"icon": "📻", "title": "Radio Digital RDMLS", "desc": "Señal en vivo de la Radio Digital Municipal La Serena.", "bg": "linear-gradient(135deg, #F77F00 0%, #C66600 100%)", "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena", "dev": False},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y eventos municipales.", "bg": "linear-gradient(135deg, #2A9D8F 0%, #1F796E 100%)", "link": "#", "dev": False},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios.", "bg": "linear-gradient(135deg, #184E77 0%, #0E3655 100%)", "link": "#", "dev": False},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "bg": "linear-gradient(135deg, #38B000 0%, #2A8700 100%)", "link": "#", "dev": False},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "MONITOREO AMBIENTAL - EN DESARROLLO", "bg": "#E9ECEF", "link": "#", "dev": True},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "TRÁNSITO Y LUMINARIAS - EN DESARROLLO", "bg": "#E9ECEF", "link": "#", "dev": True}
]

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
        </div>
        """
    else:
        html_grid += f"""
        <a href='{url}' target='_blank' style='text-decoration: none;'>
            <div class='mosaico-card {clase}' style='background: {s["bg"]};'>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </a>
        """
html_grid += "</div>"

st.markdown(html_grid, unsafe_allow_html=True)
