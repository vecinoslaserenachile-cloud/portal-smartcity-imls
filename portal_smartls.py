import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON (🔴)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="logo_muni.png", layout="wide")

# ==========================================
# 2. MOTOR ESTÉTICO: ROJO, VIDRIO Y RESPONSIVO
# ==========================================
st.markdown("""
    <style>
    /* Reset básico y fondo */
    .block-container { padding-top: 1.5rem; padding-bottom: 1rem; max-width: 95%; }
    .stApp { background-color: #FFFFFF; }
    
    /* Textos Cabecera */
    .header-title { color: #D32F2F; font-size: 2.2em; font-weight: bold; margin: 0; line-height: 1.1; }
    .header-subtitle { color: #666; font-size: 1.1em; margin-bottom: 20px; line-height: 1.2; }

    /* Filtro para logos */
    .logo-img { width: 100%; object-fit: contain; mix-blend-mode: multiply; max-height: 80px; }

    /* GRILLA RESPONSIVA: 3x3 en PC, 2x2 en Tablet, 1x1 en Celular */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
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
        padding: 20px;
        color: white !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 150px;
        height: 100%;
        backdrop-filter: blur(10px);
        background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 4px 10px rgba(211, 47, 47, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
    }
    
    .card-activa:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(211, 47, 47, 0.3);
        filter: brightness(1.15);
    }
    
    /* Tarjetas Grises (En Desarrollo) */
    .card-desactivada {
        background: rgba(233, 236, 239, 0.6) !important;
        border: 2px dashed #D32F2F;
        cursor: not-allowed !important;
        box-shadow: none !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc, .card-desactivada .card-icon { color: #ADB5BD !important; }

    /* Tipografía de las tarjetas ajustada para ahorrar espacio */
    .card-icon { font-size: 2.5em; margin-bottom: 8px; color: white; }
    .card-title { font-size: 1.25em; font-weight: bold; margin-bottom: 5px; color: white; line-height: 1.1; }
    .card-desc { font-size: 0.9em; opacity: 0.9; line-height: 1.2; color: white; }
    
    /* Contenedor Lateral (Derecha) */
    .sidebar-box {
        background: #FFF5F5;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border-left: 5px solid #D32F2F;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. LAYOUT: DIVISIÓN DE PANTALLA (75% IZQ - 25% DER)
# ==========================================
col_izq, col_der = st.columns([2.8, 1.2])

with col_izq:
    # --- ZONA IZQUIERDA: CABECERA Y MOSAICO ---
    st.markdown("""
        <div class="header-title">La Serena SmartCity</div>
        <div class="header-subtitle">Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</div>
    """, unsafe_allow_html=True)

    # Enlaces proporcionados por el Director
    servicios = [
        {"icon": "🏢", "title": "Acceso Consistorial", "desc": "Seguridad y registro de visitas.", "dev": False, "link": "https://puertaserena.streamlit.app/"},
        {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación.", "dev": False, "link": "https://vecinoslaserenachile-cloud.github.io/RDMLS/"},
        {"icon": "📡", "title": "Sentinel Faro", "desc": "Monitoreo inteligente comunal.", "dev": False, "link": "https://monitor-laserena.streamlit.app/"},
        {"icon": "📻", "title": "Radio Digital RDMLS", "desc": "Señal en vivo de la Municipalidad.", "dev": False, "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena"},
        {"icon": "🎭", "title": "App Serenito (Protocolo)", "desc": "Gestión y eventos institucionales.", "dev": False, "link": "https://vecinoslaserenachile-cloud.github.io/serenito-app/"},
        {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación para funcionarios.", "dev": False, "link": "https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/"},
        {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador de reportes de gestión.", "dev": False, "link": "https://honorarios-ls-me.streamlit.app/"},
        {"icon": "⛱️", "title": "Playas y Humedales", "desc": "EN DESARROLLO - MONITOREO", "dev": True, "link": "#"},
        {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "EN DESARROLLO - TRÁNSITO", "dev": True, "link": "#"}
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


with col_der:
    # --- ZONA DERECHA: LOGOS, QR Y SERENITO ---
    
    # Logos proporcionados
    c_logo1, c_logo2 = st.columns(2, vertical_alignment="center")
    with c_logo1:
        st.markdown('<img src="app/static/logo_muni.png" class="logo-img">', unsafe_allow_html=True)
    with c_logo2:
        st.markdown('<img src="app/static/logo_innovacion.png" class="logo-img">', unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    
    # Código QR Funcional (Puro URL web, sin codificar en texto)
    portal_url = "https://app-smartcity-imls.streamlit.app/"
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={portal_url}"
    
    st.markdown(f"""
        <div style="text-align: center;">
            <p style="color: #D32F2F; font-weight: bold; font-size: 1.1em; margin-bottom: 5px;">📲 Escanea y Accede</p>
            <img src="{qr_api_url}" width="150" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        </div>
    """, unsafe_allow_html=True)

    # Burbuja de Serenito
    st.markdown("""
        <div class="sidebar-box">
            <div style='font-size: 50px;'>🔴</div>
            <p style='color: #D32F2F; font-weight: bold; margin-bottom: 5px;'>Serenito SmartBot</p>
            <p style='color: #444; font-size: 0.95em; line-height: 1.3;'>
                Apunta tu cámara al código QR para llevar todos nuestros servicios municipales interactivos en tu bolsillo.
            </p>
        </div>
    """, unsafe_allow_html=True)
