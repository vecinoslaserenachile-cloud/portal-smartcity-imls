import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON (🏙️ Smart City)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏙️", layout="wide")

# ==========================================
# 2. ESTILOS DE LAS TARJETAS (MOSAICO)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    /* Diseño de tarjeta tipo mosaico */
    .mosaico-card {
        border-radius: 15px;
        padding: 20px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 180px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .mosaico-card:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .card-icon { font-size: 3em; margin-bottom: 10px; }
    .card-title { font-size: 1.4em; font-weight: bold; margin-bottom: 5px; }
    .card-desc { font-size: 0.9em; opacity: 0.9; line-height: 1.2; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON ESPACIO PARA 2 LOGOS
# ==========================================
col_titulo, col_logos = st.columns([2, 1])

with col_titulo:
    st.markdown("<h1 style='color: #003366; margin-bottom: 0px;'>🏙️ La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.1em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_logos:
    # Espacio lateral derecho para los dos logotipos solicitados
    c1, c2 = st.columns(2)
    with c1:
        # Logo 1: Escudo Municipal
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Escudo_de_La_Serena.svg/800px-Escudo_de_La_Serena.svg.png", use_container_width=True) 
    with c2:
        # Logo 2: Innovación Municipal Clase Mundial
        st.image("https://via.placeholder.com/300x100/FFFFFF/003366?text=Innovacion+Clase+Mundial", use_container_width=True)

st.divider()

# ==========================================
# 4. RADIO SIMPLIFICADA (BOTÓN PLAY)
# ==========================================
# Solo un reproductor pequeño y limpio para no romper el mosaico
st.markdown("<p style='color: #D62828; font-weight: bold; margin-bottom: 5px;'>📻 Radio Digital Municipal En Vivo:</p>", unsafe_allow_html=True)
st.audio("https://az11.yesstreaming.net/radio/8010/radio.mp3") 

# ==========================================
# 5. EL MOSAICO DE SERVICIOS (SIN HUECOS)
# ==========================================
# Definición de los servicios con sus colores originales
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Control de seguridad y bitácora digital.", "bg": "#1E6091", "link": "https://puertaserena.streamlit.app"},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación.", "bg": "#D62828", "link": "#"},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo comunal.", "bg": "#7209B7", "link": "#"},
    {"icon": "🎙️", "title": "Pódcasts IMLS", "desc": "Entrevistas y programas municipales.", "bg": "#F77F00", "link": "#"},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y eventos.", "bg": "#2A9D8F", "link": "#"},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación para funcionarios.", "bg": "#184E77", "link": "#"},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador de reportes mensuales.", "bg": "#38B000", "link": "#"}
]

# Despliegue en 3 columnas para mantener el equilibrio visual
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
