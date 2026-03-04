import streamlit as st
import qrcode
from io import BytesIO

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON (🔴)
# ==========================================
# Usamos el escudo municipal como favicon institucional
st.set_page_config(page_title="La Serena SmartCity", page_icon="logo_muni.png", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: VIDRIO Y ROJO
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Cabecera compacta y alineada */
    .header-text { display: flex; flex-direction: column; justify-content: center; height: 90px; }
    .header-title { color: #D32F2F; font-size: 2.2em; font-weight: bold; margin: 0; line-height: 1.1; }
    .header-subtitle { color: #666; font-size: 1.2em; margin: 0; line-height: 1.2; }

    /* Logos equilibrados y proporcionales */
    img[data-testid="stImage"] { max-height: 90px; width: auto; object-fit: contain; mix-blend-mode: multiply; }

    /* Grilla 3x3 sin huecos */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px 0;
    }

    /* Tarjeta Efecto Vidrio Glaseado */
    .mosaico-card {
        border-radius: 20px;
        padding: 25px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 200px;
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
    
    /* Servicios EN DESARROLLO (Grises) */
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
    
    /* Módulo QR */
    .qr-container { text-align: center; padding: 20px; background: #FFF5F5; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA ALINEADA (90px de altura)
# ==========================================
# Forzamos proporciones y alturas en el header
col_info, col_logo1, col_logo2 = st.columns([2, 0.6, 0.6])

with col_info:
    st.markdown("""
        <div class="header-text">
            <div class="header-title">La Serena SmartCity</div>
            <div class="header-subtitle">Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</div>
        </div>
    """, unsafe_allow_html=True)

with col_logo1:
    # Se cargan proporcionalmente desde la raíz
    st.image("logo_muni.png", use_container_width=True) 

with col_logo2:
    st.image("logo_innovacion.png", use_container_width=True)

st.divider()

# ==========================================
# 4. MÓDULO QR CENTRAL Y ORGÁNICO
# ==========================================
st.markdown("### 📲 Acceso Rápido: Escanee para interactuar con el portal")

col_asistente, col_qr, col_mensaje = st.columns([1, 1, 3], vertical_alignment="center")

with col_asistente:
    st.markdown("<div style='font-size: 80px; text-align: center;'>🔴</div>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center; color: #D32F2F; font-weight: bold;'>Serenito SmartBot</p>", unsafe_allow_html=True)

with col_qr:
    # Generamos el QR de forma nativa para el portal interactivo
    portal_url = "https://rdmls.streamlit.app" # URL pública del portal
    qr_image = qrcode.make(portal_url)
    
    # Lo convertimos a bytes para Streamlit
    buf = BytesIO()
    qr_image.save(buf)
    
    # Desplegamos el QR orgánico
    st.image(buf.getvalue(), width=150)

with col_mensaje:
    st.markdown(f"""
        <div class="chat-bubble">
            <b>Serenito dice:</b> ¡Bienvenido al portal inteligente! Escanee el código de su izquierda para acceder directamente a todos los servicios desde su teléfono móvil y <b style='color: #D32F2F;'>llevar la SmartCity en su bolsillo.</b>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================
# 5. EL MOSAICO 3x3 (9 SERVICIOS)
# ==========================================
# El mosaico de 9 piezas con los servicios 8 y 9 desactivados
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y registro digital de visitas municipales.", "dev": False, "link": "https://puertaserena.streamlit.app"},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación interactiva.", "dev": False, "link": "https://rdmls.cl"}, # CONECTADO
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo inteligente comunal.", "dev": False, "link": "#"},
    {"icon": "📻", "title": "Radio Digital RDMLS", "desc": "Señal en vivo y programación de la Municipalidad.", "dev": False, "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena"}, # CONECTADO
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación de actos.", "dev": False, "link": "#"},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios municipales.", "dev": False, "link": "#"},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "dev": False, "link": "#"},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "EN DESARROLLO - MONITOREO AMBIENTAL", "dev": True, "link": "#"}, # DESACTIVADO
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "EN DESARROLLO - TRÁNSITO Y BACHES", "dev": True, "link": "#"} # DESACTIVADO
]

# Construcción de la grilla HTML sin fugas de código
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
