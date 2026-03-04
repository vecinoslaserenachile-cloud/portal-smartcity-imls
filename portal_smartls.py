import streamlit as st
import urllib.parse

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON (🔴)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="logo_muni.png", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: VIDRIO Y ROJO INSTITUCIONAL
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    .header-text { display: flex; flex-direction: column; justify-content: center; height: 90px; }
    .header-title { color: #D32F2F; font-size: 2.2em; font-weight: bold; margin: 0; line-height: 1.1; }
    .header-subtitle { color: #666; font-size: 1.2em; margin: 0; line-height: 1.2; }

    img[data-testid="stImage"] { max-height: 90px; width: auto; object-fit: contain; mix-blend-mode: multiply; }

    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px 0;
    }

    /* Blindaje para que toda la tarjeta sea clicable */
    .card-enlace { display: block; text-decoration: none !important; height: 100%; }

    .mosaico-card {
        border-radius: 20px;
        padding: 25px;
        color: white !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 200px;
        height: 100%;
        backdrop-filter: blur(10px);
        background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(211, 47, 47, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(211, 47, 47, 0.3);
        filter: brightness(1.2);
    }
    
    .card-desactivada {
        background: rgba(233, 236, 239, 0.7) !important;
        color: #ADB5BD !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc, .card-desactivada .card-icon { color: #ADB5BD !important; }

    .card-icon { font-size: 3.5em; margin-bottom: 12px; color: white; }
    .card-title { font-size: 1.5em; font-weight: bold; margin-bottom: 8px; color: white; line-height: 1.2; }
    .card-desc { font-size: 1em; opacity: 0.95; line-height: 1.3; color: white; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA ALINEADA
# ==========================================
col_info, col_logo1, col_logo2 = st.columns([2, 0.6, 0.6])

with col_info:
    st.markdown("""
        <div class="header-text">
            <div class="header-title">La Serena SmartCity</div>
            <div class="header-subtitle">Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</div>
        </div>
    """, unsafe_allow_html=True)

with col_logo1:
    st.image("logo_muni.png", use_container_width=True) 

with col_logo2:
    st.image("logo_innovacion.png", use_container_width=True)

st.divider()

# ==========================================
# 4. MÓDULO QR (CODIFICADO PARA CELULARES)
# ==========================================
st.markdown("### 📲 Acceso Rápido: Escanee para interactuar con el portal")

col_asistente, col_qr, col_mensaje = st.columns([1, 1, 3], vertical_alignment="center")

with col_asistente:
    st.markdown("<div style='font-size: 80px; text-align: center;'>🔴</div>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center; color: #D32F2F; font-weight: bold;'>Serenito SmartBot</p>", unsafe_allow_html=True)

with col_qr:
    # URL de su portal en Streamlit Cloud
    portal_url = "https://app-smartcity-imls.streamlit.app/" 
    # Codificamos la URL para forzar al celular a abrir el navegador
    encoded_url = urllib.parse.quote(portal_url)
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encoded_url}"
    st.image(qr_api_url, width=150)

with col_mensaje:
    st.markdown(f"""
        <div class="chat-bubble" style="background: #FFF5F5; padding: 20px; border-radius: 15px; border-left: 5px solid #D32F2F;">
            <b>Serenito dice:</b> ¡Bienvenido al portal inteligente! Escanee el código de su izquierda para acceder directamente a todos los servicios desde su teléfono móvil y <b style='color: #D32F2F;'>llevar la SmartCity en su bolsillo.</b>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================
# 5. EL MOSAICO 3x3 (ENLACES BLINDADOS)
# ==========================================
servicios = [
    {
        "icon": "🏢", 
        "title": "Acceso Edificio Consistorial", 
        "desc": "Seguridad y registro digital de visitas municipales.", 
        "dev": False, 
        "link": "https://puertaserena.streamlit.app"
    },
    {
        "icon": "🌐", 
        "title": "Portal RDMLS Integral", 
        "desc": "Plataforma ciudadana y georeferenciación interactiva.", 
        "dev": False, 
        "link": "#" # <-- ¡DIRECTOR: PEGUE SU LINK REAL AQUÍ!
    },
    {
        "icon": "📡", 
        "title": "Sentinel Faro", 
        "desc": "Social Listening y monitoreo inteligente comunal.", 
        "dev": False, 
        "link": "#" # <-- ¡DIRECTOR: PEGUE SU LINK REAL AQUÍ!
    },
    {
        "icon": "📻", 
        "title": "Radio Digital RDMLS", 
        "desc": "Señal en vivo y programación de la Municipalidad.", 
        "dev": False, 
        "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena" # RESTAURADO A PÁGINA PÚBLICA
    },
    {
        "icon": "🎭", 
        "title": "Protocolo y Eventos", 
        "desc": "Gestión institucional y coordinación de actos.", 
        "dev": False, 
        "link": "#" # <-- ¡DIRECTOR: PEGUE SU LINK REAL AQUÍ!
    },
    {
        "icon": "🎓", 
        "title": "Inducción E-Learning", 
        "desc": "Capacitación digital para funcionarios municipales.", 
        "dev": False, 
        "link": "#" # <-- ¡DIRECTOR: PEGUE SU LINK REAL AQUÍ!
    },
    {
        "icon": "📄", 
        "title": "Informes Honorarios", 
        "desc": "Generador automático de reportes de gestión.", 
        "dev": False, 
        "link": "#" # <-- ¡DIRECTOR: PEGUE SU LINK REAL AQUÍ!
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
        # Se agrega rel='noopener noreferrer' y clase card-enlace para máxima compatibilidad
        html_grid += f"""
        <a href='{url}' target='_blank' rel='noopener noreferrer' class='card-enlace'>
            <div class='mosaico-card card-activa'>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </a>"""
html_grid += "</div>"

st.markdown(html_grid, unsafe_allow_html=True)
