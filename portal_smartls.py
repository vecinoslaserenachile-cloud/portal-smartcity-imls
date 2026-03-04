import streamlit as st
import urllib.parse

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON (🔴)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="logo_muni.png", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: ROJO, VIDRIO Y RESPONSIVO
# ==========================================
st.markdown("""
    <style>
    /* Reset básico para aprovechar toda la pantalla */
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .stApp { background-color: #FFFFFF; }
    
    /* Textos Cabecera (Sin alturas forzadas para evitar cortes) */
    .header-title { color: #D32F2F; font-size: 2.4em; font-weight: bold; margin: 0; line-height: 1.2; }
    .header-subtitle { color: #666; font-size: 1.2em; margin-bottom: 10px; line-height: 1.3; }

    /* Filtro para pelar fondo blanco de los logos */
    img[data-testid="stImage"] { mix-blend-mode: multiply; object-fit: contain; }

    /* GRILLA RESPONSIVA: 3 columnas en PC, 2 en Tablet, 1 en Celular */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding-top: 10px;
    }
    @media (max-width: 1100px) {
        .smart-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
        .smart-grid { grid-template-columns: 1fr; }
    }

    /* Blindaje de enlace en tarjetas */
    .card-enlace { display: block; text-decoration: none !important; height: 100%; }

    /* Tarjetas Rojas (Activas) */
    .mosaico-card {
        border-radius: 15px;
        padding: 25px;
        color: white !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 180px;
        height: 100%;
        backdrop-filter: blur(10px);
        background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 4px 12px rgba(211, 47, 47, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 25px rgba(211, 47, 47, 0.35);
        filter: brightness(1.15);
    }
    
    /* Tarjetas Grises (En Desarrollo) */
    .card-desactivada {
        background: rgba(233, 236, 239, 0.8) !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc, .card-desactivada .card-icon { color: #ADB5BD !important; }

    .card-icon { font-size: 3em; margin-bottom: 10px; color: white; }
    .card-title { font-size: 1.4em; font-weight: bold; margin-bottom: 6px; color: white; line-height: 1.2; }
    .card-desc { font-size: 0.95em; opacity: 0.95; line-height: 1.3; color: white; }
    
    /* Contenedor Lateral (Derecha) */
    .sidebar-box {
        background: #FFF5F5;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        border-left: 5px solid #D32F2F;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA PRINCIPAL (LOGOS RECUPERADOS)
# ==========================================
# Los logos vuelven a su posición segura arriba para que no se corten ni desaparezcan
col_titulos, col_logos = st.columns([2.5, 1.5])

with col_titulos:
    st.markdown("""
        <div class="header-title">La Serena SmartCity</div>
        <div class="header-subtitle">Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</div>
    """, unsafe_allow_html=True)

with col_logos:
    # Carga nativa para que funcione siempre en la nube y móviles
    c1, c2 = st.columns(2)
    with c1:
        st.image("logo_muni.png", use_container_width=True)
    with c2:
        st.image("logo_innovacion.png", use_container_width=True)

st.divider()

# ==========================================
# 4. LAYOUT PRINCIPAL: 75% MOSAICO | 25% QR
# ==========================================
col_mosaico, col_qr = st.columns([3, 1])

with col_mosaico:
    # Enlaces oficiales mapeados
    servicios = [
        {"icon": "🏢", "title": "Acceso Consistorial", "desc": "Seguridad y registro digital de visitas.", "dev": False, "link": "https://puertaserena.streamlit.app/"},
        {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación.", "dev": False, "link": "https://vecinoslaserenachile-cloud.github.io/RDMLS/"},
        {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo inteligente comunal.", "dev": False, "link": "https://monitor-laserena.streamlit.app/"},
        {"icon": "📻", "title": "Radio Digital RDMLS", "desc": "Señal en vivo de la Municipalidad de La Serena.", "dev": False, "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena"},
        {"icon": "🎭", "title": "App Serenito (Protocolo)", "desc": "Gestión institucional y coordinación de eventos.", "dev": False, "link": "https://vecinoslaserenachile-cloud.github.io/serenito-app/"},
        {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios.", "dev": False, "link": "https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/"},
        {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "dev": False, "link": "https://honorarios-ls-me.streamlit.app/"},
        {"icon": "⛱️", "title": "Playas y Humedales", "desc": "EN DESARROLLO - MONITOREO AMBIENTAL", "dev": True, "link": "#"},
        {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "EN DESARROLLO - TRÁNSITO Y BACHES", "dev": True, "link": "#"}
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
            <a href='{url}' target='_blank' rel='noopener noreferrer' class='card-enlace'>
                <div class='mosaico-card card-activa'>
                    <div class='card-icon'>{s["icon"]}</div>
                    <div class='card-title'>{s["title"]}</div>
                    <div class='card-desc'>{s["desc"]}</div>
                </div>
            </a>"""
    html_grid += "</div>"
    
    st.markdown(html_grid, unsafe_allow_html=True)


with col_qr:
    # Generador de código QR nativo para hipervínculos
    portal_url = "https://app-smartcity-imls.streamlit.app/"
    # Codificar la URL asegura que el lector del teléfono entienda que debe abrir un navegador
    encoded_url = urllib.parse.quote(portal_url)
    qr_api_url = f"https://quickchart.io/qr?text={encoded_url}&size=250&margin=1"
    
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <p style="color: #D32F2F; font-weight: bold; font-size: 1.2em; margin-bottom: 10px;">📲 Escanea y Accede</p>
            <img src="{qr_api_url}" width="180" style="border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
        </div>
    """, unsafe_allow_html=True)

    # Burbuja Informativa de Serenito
    st.markdown("""
        <div class="sidebar-box">
            <div style='font-size: 45px;'>🔴</div>
            <p style='color: #D32F2F; font-weight: bold; font-size: 1.1em; margin-bottom: 5px;'>Serenito SmartBot</p>
            <p style='color: #444; font-size: 0.95em; line-height: 1.4;'>
                Apunta la cámara de tu teléfono al código QR superior para abrir el <b>Portal SmartCity</b> interactivo y llevar los servicios en tu bolsillo.
            </p>
        </div>
    """, unsafe_allow_html=True)
