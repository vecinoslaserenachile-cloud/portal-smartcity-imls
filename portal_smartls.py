import streamlit as st

# 1. CONFIGURACIÓN DEL PORTAL CON FAVICON INSTITUCIONAL
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏛️", layout="wide")

# 2. MOTOR GRÁFICO BLINDADO (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F5; }
    
    /* Contenedor Principal */
    .metro-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        grid-auto-rows: 160px;
        gap: 15px;
        padding: 20px 0;
    }
    
    /* Baldosas Operativas */
    .tile {
        color: white !important;
        text-decoration: none;
        padding: 20px;
        border-radius: 12px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.2s ease;
    }
    .tile:hover { transform: translateY(-5px); box-shadow: 0 8px 20px rgba(0,0,0,0.25); filter: brightness(1.1); }
    
    /* Baldosas en Desarrollo (Estilo Transparente) */
    .tile-dev {
        background: rgba(255, 255, 255, 0.7);
        border: 2px dashed #BDC3C7;
        color: #7F8C8D !important;
        cursor: default;
    }
    .badge-dev {
        background: #E74C3C; color: white; font-size: 0.7em;
        padding: 2px 8px; border-radius: 10px; font-weight: bold; width: fit-content;
    }

    /* Tamaños y Colores */
    .wide { grid-column: span 2; }
    .large { grid-column: span 2; grid-row: span 2; }
    .t-icon { font-size: 2.8em; }
    .t-title { font-weight: 800; font-size: 1.2em; margin-top: 10px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }
    .t-sub { font-size: 0.85em; opacity: 0.9; font-weight: 400; line-height: 1.2; }
    
    .bg-blue { background: linear-gradient(135deg, #1A365D, #2B6CB0); }
    .bg-red { background: linear-gradient(135deg, #C53030, #F56565); }
    .bg-orange { background: linear-gradient(135deg, #C05621, #ED8936); }
    .bg-teal { background: linear-gradient(135deg, #2C7A7B, #4FD1C5); }
    .bg-purple { background: linear-gradient(135deg, #553C9A, #9F7AEA); }
    .bg-green { background: linear-gradient(135deg, #276749, #48BB78); }

    @media (max-width: 768px) { .wide, .large { grid-column: span 1; } }
    </style>
""", unsafe_allow_html=True)

# 3. CABECERA INSTITUCIONAL
col1, col2 = st.columns([1, 7])
with col1:
    st.markdown("<div style='font-size: 70px; text-align: center;'>🏛️</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<h1 style='color: #1A202C; margin-bottom: 0;'>La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #4A5568; font-size: 1.2em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

st.divider()

# 4. TABLERO DE CONTROL (MOSAICO COMPRIMIDO)
mosaico = f"""<div class="metro-grid">
    <a href="https://puertaserena.streamlit.app/" target="_blank" class="tile wide bg-blue">
        <div><div class="t-icon">🏢</div><div class="t-title">Acceso Edificio Consistorial</div></div>
        <div class="t-sub">Control de seguridad y bitácora digital de visitas para el recinto municipal.</div>
    </a>
    <a href="https://vecinoslaserenachile-cloud.github.io/RDMLS/" target="_blank" class="tile large bg-red">
        <div><div class="t-icon">🌐</div><div class="t-title">Portal RDMLS Integral</div></div>
        <div class="t-sub">Plataforma ciudadana con radio, georeferenciación y herramientas interactivas.</div>
    </a>
    <a href="https://monitor-laserena.streamlit.app/" target="_blank" class="tile wide bg-purple">
        <div><div class="t-icon">📡</div><div class="t-title">Sentinel Faro</div></div>
        <div class="t-sub">Sistema inteligente de Social Listening y monitoreo de datos comunales.</div>
    </a>
    <a href="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena" target="_blank" class="tile bg-orange">
        <div><div class="t-icon">🎙️</div><div class="t-title">Señal RDMLS</div></div>
        <div class="t-sub">Streaming oficial en vivo.</div>
    </a>
    <a href="https://vecinoslaserenachile-cloud.github.io/serenito-app/" target="_blank" class="tile bg-teal">
        <div><div class="t-icon">🎭</div><div class="t-title">Protocolo y Eventos</div></div>
        <div class="t-sub">Gestión institucional y eventos.</div>
    </a>
    <a href="https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/" target="_blank" class="tile bg-blue">
        <div><div class="t-icon">🎓</div><div class="t-title">Inducción E-Learning</div></div>
        <div class="t-sub">Capacitación para funcionarios.</div>
    </a>
    <a href="https://honorarios-ls-me.streamlit.app/" target="_blank" class="tile bg-green">
        <div><div class="t-icon">📄</div><div class="t-title">Informes Honorarios</div></div>
        <div class="t-sub">Generador automático de reportes.</div>
    </a>
    <div class="tile tile-dev">
        <div class="badge-dev">PRÓXIMAMENTE</div>
        <div><div class="t-icon" style="filter: grayscale(1);">🏗️</div><div class="t-title">Portal de Pagos Online</div></div>
        <div class="t-sub">Módulo de Rentas y Patentes en desarrollo.</div>
    </div>
    <div class="tile tile-dev">
        <div class="badge-dev">PRÓXIMAMENTE</div>
        <div><div class="t-icon" style="filter: grayscale(1);">🚍</div><div class="t-title">Smart Transito LS</div></div>
        <div class="t-sub">Monitoreo de flujo vehicular.</div>
    </div>
</div>"""

st.markdown(mosaico, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Ilustre Municipalidad de La Serena | Transformación Digital")
