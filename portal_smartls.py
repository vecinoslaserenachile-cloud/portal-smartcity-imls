import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON INSTITUCIONAL
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="logo_muni.png", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: ROJO, BLANCO Y BLINDAJE
# ==========================================
st.markdown("""
    <style>
    /* Fondo de la app */
    .stApp { background-color: #FFFFFF; }
    
    /* Cabecera alineada manualmente sin romper el servidor */
    .header-title { color: #D32F2F; font-size: 2.2em; font-weight: bold; margin: 0; line-height: 1.1; padding-top: 15px; }
    .header-subtitle { color: #666; font-size: 1.1em; margin: 0; line-height: 1.2; }

    /* Aplica el filtro para eliminar fondos blancos de los logos */
    img[data-testid="stImage"] { mix-blend-mode: multiply; }

    /* Grilla 3x3 */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px 0;
    }

    /* Enlaces seguros para toda la tarjeta */
    a.card-enlace {
        display: block;
        text-decoration: none !important;
        height: 100%;
    }

    /* Tarjetas Activas (Rojas) */
    .mosaico-card {
        border-radius: 15px;
        padding: 25px;
        color: white !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
        min-height: 180px; 
        
        background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(211, 47, 47, 0.35);
        filter: brightness(1.15);
    }
    
    /* Tarjetas en Desarrollo (Grises) */
    .card-desactivada {
        background: #F8F9FA !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc, .card-desactivada .card-icon { 
        color: #ADB5BD !important; 
    }

    .card-icon { font-size: 3em; margin-bottom: 12px; color: white; }
    .card-title { font-size: 1.5em; font-weight: bold; margin-bottom: 6px; color: white; line-height: 1.2; }
    .card-desc { font-size: 1em; opacity: 0.95; line-height: 1.3; color: white; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA SEGURA Y PROPORCIONAL
# ==========================================
# Se quita el parámetro problemático que causó el pantallazo blanco
col_info, col_logo1, col_logo2 = st.columns([2, 0.5, 0.5])

with col_info:
    st.markdown("""
        <div class="header-title">La Serena SmartCity</div>
        <div class="header-subtitle">Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</div>
    """, unsafe_allow_html=True)

with col_logo1:
    # Carga nativa para evitar problemas de rutas HTML
    st.image("logo_muni.png", use_container_width=True)

with col_logo2:
    # Carga nativa
    st.image("logo_innovacion.png", use_container_width=True)

st.divider()

# ==========================================
# 4. MOSAICO 3x3 CON DIRECCIONES CONECTADAS
# ==========================================
servicios = [
    {
        "icon": "🏢", 
        "title": "Acceso Consistorial", 
        "desc": "Seguridad y registro digital de visitas municipales.", 
        "dev": False, 
        "link": "https://puertaserena.streamlit.app"
    },
    {
        "icon": "🌐", 
        "title": "Portal RDMLS", 
        "desc": "Plataforma ciudadana y georeferenciación interactiva.", 
        "dev": False, 
        "link": "#" 
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
        "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena"
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
    url = s["link"]
    
    if s["dev"]:
        html_grid += f"""
        <div class='mosaico-card card-desactivada'>
            <div class='card-icon'>{s["icon"]}</div>
            <div class='card-title'>{s["title"]}</div>
            <div class='card-desc'>{s["desc"]}</div>
        </div>"""
    else:
        html_grid += f"""
        <a href='{url}' target='_blank' class='card-enlace'>
            <div class='mosaico-card card-activa'>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </a>"""
html_grid += "</div>"

st.markdown(html_grid, unsafe_allow_html=True)
