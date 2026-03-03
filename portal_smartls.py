import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON ROJO (🔴)
# ==========================================
# Cambiamos el celeste por el rojo institucional
st.set_page_config(page_title="La Serena SmartCity", page_icon="🔴", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: ROJO Y BLANCO (GLASS)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Títulos en Rojo Municipal */
    h1, h2, h3 { color: #D32F2F !important; }
    
    /* Grilla simétrica 3x3 */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px 0;
    }

    @media (max-width: 1000px) {
        .smart-grid { grid-template-columns: 1fr; }
    }
    
    /* Tarjeta Efecto Vidrio sobre Fondo Rojo */
    .mosaico-card {
        border-radius: 20px;
        padding: 30px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 220px;
        
        /* Glassmorphism con base Roja */
        backdrop-filter: blur(10px);
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
    
    /* Servicios EN DESARROLLO (Gris suave para no desentonar) */
    .card-desactivada {
        background: rgba(233, 236, 239, 0.8) !important;
        color: #ADB5BD !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc { color: #ADB5BD !important; }

    .card-icon { font-size: 3.8em; margin-bottom: 15px; color: white !important; }
    .card-title { font-size: 1.6em; font-weight: bold; margin-bottom: 10px; line-height: 1.1; color: white !important; }
    .card-desc { font-size: 1.05em; opacity: 0.95; line-height: 1.3; color: white !important; }
    
    /* Asistente Virtual Rojo */
    .chat-bubble {
        background: #FFF5F5; padding: 20px; border-radius: 15px;
        border-left: 5px solid #D32F2F; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px; color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA (LOGOS EN RAÍZ)
# ==========================================
col_t, col_l = st.columns([1.8, 1.2])

with col_t:
    st.markdown("<h1 style='margin-bottom: 0px;'>🔴 La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.25em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_l:
    # Equilibrio de logos cargando desde la raíz
    c1, c2 = st.columns(2)
    with c1:
        st.image("logo_muni.png", width=150) # El logo que subiste en rojo
    with c2:
        st.image("logo_innovacion.png", width=150)

st.divider()

# ==========================================
# 4. ASISTENTE CIUDADANO "SERENITO"
# ==========================================
st.markdown("### 🙋‍♂️ Asistente Virtual: Guía de Servicios")

with st.container():
    col_asistente, col_pregunta = st.columns([1, 4])
    with col_asistente:
        st.markdown("<div style='font-size: 80px; text-align: center;'>🔴</div>", unsafe_allow_html=True)
        st.caption("<p style='text-align: center; color: #D32F2F; font-weight: bold;'>Serenito SmartBot</p>", unsafe_allow_html=True)

    with col_pregunta:
        pregunta = st.text_input("Escribe tu duda sobre los servicios municipales...", key="user_query")
        if pregunta:
            st.markdown(f"<div class='chat-bubble'><b>Serenito responde:</b> Estamos procesando su consulta sobre '{pregunta}'. Para una respuesta inmediata, puede contactarnos a <b>contacto@laserena.cl</b></div>", unsafe_allow_html=True)

st.write("")

# ==========================================
# 5. EL MOSAICO 3x3 (9 SERVICIOS - ROJO TOTAL)
# ==========================================
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y bitácora digital de visitas.", "dev": False, "link": "https://puertaserena.streamlit.app"},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación.", "dev": False, "link": "#"},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo inteligente.", "dev": False, "link": "#"},
    {"icon": "📻", "title": "Radio Digital RDMLS", "desc": "Señal en vivo de la Municipalidad de La Serena.", "dev": False, "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena"},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación de actos.", "dev": False, "link": "#"},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios.", "dev": False, "link": "#"},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "dev": False, "link": "#"},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "EN DESARROLLO - MONITOREO AMBIENTAL", "dev": True, "link": "#"},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "EN DESARROLLO - TRÁNSITO Y BACHES", "dev": True, "link": "#"}
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
