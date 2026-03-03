import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON DISTINTIVO (🌐)
# ==========================================
# Se utiliza el globo terráqueo para representar la red SmartCity
# y diferenciarlo del icono de edificio (🏛️) del sistema de acceso.
st.set_page_config(page_title="La Serena SmartCity", page_icon="🌐", layout="wide")

# ==========================================
# 2. ESTILOS: GLASSMORPHISM (EFECTO VIDRIOSO)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    /* Contenedor de la grilla */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 25px;
        padding: 30px 0;
    }
    
    /* Tarjeta Mosaico con efecto de vidrio */
    .mosaico-card {
        border-radius: 20px;
        padding: 30px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 210px;
        
        /* Glassmorphism */
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.1); 
        border: 1px solid rgba(255, 255, 255, 0.25);
        
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .card-activa:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.2);
    }
    
    /* Estilo para botones EN DESARROLLO */
    .card-desactivada {
        background: rgba(200, 200, 200, 0.4) !important;
        color: #888 !important;
        border: 2px dashed #AAA;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc {
        color: #888 !important;
    }

    /* Tipografía de las tarjetas */
    .card-icon { font-size: 3.8em; margin-bottom: 15px; }
    .card-title { font-size: 1.6em; font-weight: bold; margin-bottom: 10px; line-height: 1.1; color: white; }
    .card-desc { font-size: 1.05em; opacity: 0.9; line-height: 1.3; color: white; }
    
    /* Logos equilibrados y filtro para Innovación */
    .img-header {
        max-height: 90px;
        width: auto;
    }
    .logo-innovacion {
        mix-blend-mode: multiply;
        filter: contrast(105%);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA INSTITUCIONAL
# ==========================================
col_titulo, col_logos = st.columns([2, 1.3])

with col_titulo:
    st.markdown("<h1 style='color: #003366; margin-bottom: 0px;'>🌐 La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.2em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_logos:
    # Mostramos los logos lado a lado con equilibrio de tamaño
    c1, c2 = st.columns(2)
    with c1:
        # Cargado desde la raíz de GitHub
        st.image("logo_muni.png", width=160) 
    with c2:
        # Cargado desde la raíz con ajuste visual
        st.image("logo_innovacion.png", width=160)

st.divider()

# ==========================================
# 4. RADIO DIGITAL RDMLS (STREAM MP3)
# ==========================================
st.markdown("<p style='color: #D62828; font-weight: bold; margin-bottom: 5px;'>📻 Señal en Vivo (Radio Digital Municipal):</p>", unsafe_allow_html=True)
# Se utiliza el stream directo para garantizar la carga en todos los navegadores
st.audio("https://az11.yesstreaming.net/radio/8010/radio.mp3", format="audio/mp3")

# ==========================================
# 5. EL MOSAICO DE 9 SERVICIOS
# ==========================================
# La botonera se organiza en una grilla de 3x3.
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y bitácora digital de visitas municipales.", "bg": "linear-gradient(135deg, #1E6091 0%, #114871 100%)", "link": "https://puertaserena.streamlit.app", "dev": False},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana con radio e interactividad.", "bg": "linear-gradient(135deg, #D62828 0%, #A31B1B 100%)", "link": "#", "dev": False},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Sistema inteligente de Social Listening comunal.", "bg": "linear-gradient(135deg, #7209B7 0%, #5A0693 100%)", "link": "#", "dev": False},
    {"icon": "🎙️", "title": "Radio Digital RDMLS", "desc": "Acceso a la programación oficial y pódcasts.", "bg": "linear-gradient(135deg, #F77F00 0%, #C66600 100%)", "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena", "dev": False},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación de actos.", "bg": "linear-gradient(135deg, #2A9D8F 0%, #1F796E 100%)", "link": "#", "dev": False},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para el equipo municipal.", "bg": "linear-gradient(135deg, #184E77 0%, #0E3655 100%)", "link": "#", "dev": False},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "bg": "linear-gradient(135deg, #38B000 0%, #2A8700 100%)", "link": "#", "dev": False},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "MONITOREO AMBIENTAL EN DESARROLLO.", "bg": "#E9ECEF", "link": "#", "dev": True},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "TRÁNSITO Y LUMINARIAS EN DESARROLLO.", "bg": "#E9ECEF", "link": "#", "dev": True}
]

# Construcción de la grilla visual
html_grid = "<div class='smart-grid'>"
for s in servicios:
    tipo_clase = "card-desactivada" if s["dev"] else "card-activa"
    
    if s["dev"]:
        # Tarjeta inactiva para servicios en desarrollo
        html_grid += f"""
        <div class='mosaico-card {tipo_clase}'>
            <div>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </div>
        """
    else:
        # Tarjeta activa con enlace externo
        html_grid += f"""
        <a href='{s["link"]}' target='_blank' style='text-decoration: none;'>
            <div class='mosaico-card {tipo_clase}' style='background: {s["bg"]};'>
                <div>
                    <div class='card-icon'>{s["icon"]}</div>
                    <div class='card-title'>{s["title"]}</div>
                    <div class='card-desc'>{s["desc"]}</div>
                </div>
            </div>
        </a>
        """
html_grid += "</div>"

# Renderizado final del mosaico
st.markdown(html_grid, unsafe_allow_html=True)
