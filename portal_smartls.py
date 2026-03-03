import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON SMART CITY (🏙️)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏙️", layout="wide")

# ==========================================
# 2. ESTILOS DEL MOSAICO (LIMPIEZA TOTAL)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    .mosaico-card {
        border-radius: 15px;
        padding: 25px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 190px;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        transition: transform 0.2s ease;
    }
    .mosaico-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.25);
    }
    .card-icon { font-size: 3.5em; margin-bottom: 12px; }
    .card-title { font-size: 1.5em; font-weight: bold; margin-bottom: 8px; line-height: 1.1; }
    .card-desc { font-size: 1em; opacity: 0.95; line-height: 1.3; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON LOGOS DESDE LA RAÍZ
# ==========================================
col_titulo, col_logos = st.columns([2, 1])

with col_titulo:
    st.markdown("<h1 style='color: #003366; margin-bottom: 0px;'>🏙️ La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.2em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_logos:
    # Usando los archivos que subiste a la raíz de tu GitHub
    c1, c2 = st.columns(2)
    with c1:
        st.image("logo_muni.png", use_container_width=True) 
    with c2:
        st.image("logo_innovacion.png", use_container_width=True)

st.divider()

# ==========================================
# 4. RADIO SIMPLIFICADA (BOTÓN PLAY MP3)
# ==========================================
st.markdown("<p style='color: #D62828; font-weight: bold; margin-bottom: 5px;'>📻 Radio Digital Municipal En Vivo:</p>", unsafe_allow_html=True)
# Conexión directa al stream para carga instantánea
st.audio("https://az11.yesstreaming.net/radio/8010/radio.mp3", format="audio/mp3")

# ==========================================
# 5. EL MOSAICO DE 9 SERVICIOS (GRILLA COMPLETA)
# ==========================================
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Control de seguridad y bitácora digital de visitas.", "bg": "#1E6091", "link": "https://puertaserena.streamlit.app"},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación interactiva.", "bg": "#D62828", "link": "#"},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Sistema de Social Listening y monitoreo comunal.", "bg": "#7209B7", "link": "#"},
    {"icon": "🎙️", "title": "Pódcasts IMLS", "desc": "Revive las entrevistas y programas municipales on-demand.", "bg": "#F77F00", "link": "#"},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación de eventos.", "bg": "#2A9D8F", "link": "#"},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios municipales.", "bg": "#184E77", "link": "#"},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión mensual.", "bg": "#38B000", "link": "#"},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "Monitoreo ambiental de ecosistemas y biodiversidad.", "bg": "#0077B6", "link": "#"},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "Tránsito, luminarias y reparación de baches.", "bg": "#457B9D", "link": "#"}
]

# Despliegue en 3 columnas perfectas (3x3)
cols = st.columns(3)
for i, s in enumerate(servicios):
    with cols[i % 3]:
        card_html = f"""
        <a href='{s["link"]}' target='_blank' style='text-decoration: none;'>
            <div class='mosaico-card' style='background-color: {s["bg"]};'>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </a>
        """
        st.markdown(card_html, unsafe_allow_html=True)
