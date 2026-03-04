import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURACIÓN DEL PORTAL
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🌐", layout="wide")

# ==========================================
# 2. MOTOR GRÁFICO (ELEGANCIA Y RESPONSIVIDAD)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    
    a { text-decoration: none !important; }
    
    .metro-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-auto-rows: 150px;
        gap: 18px;
        padding: 20px 0;
    }
    
    .metro-tile {
        color: white !important;
        padding: 22px;
        border-radius: 12px;
        font-family: 'Segoe UI', sans-serif;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .metro-tile * { text-decoration: none !important; color: white !important; }
    
    a.metro-tile:hover {
        transform: scale(1.02) translateY(-4px);
        box-shadow: 0 15px 25px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    .disabled-tile {
        cursor: default;
        opacity: 0.85;
        filter: grayscale(20%);
    }
    
    .tile-wide { grid-column: span 2; }
    .tile-large { grid-column: span 2; grid-row: span 2; }
    
    .tile-icon { font-size: 2.4em; margin-bottom: 5px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); }
    .tile-title { font-weight: 700; font-size: 1.25em; line-height: 1.2; margin-bottom: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }
    .tile-subtitle { font-size: 0.85em; opacity: 0.9; font-weight: 400; }
    
    .bg-alcaldia { background: linear-gradient(135deg, #1A365D 0%, #2B6CB0 100%); } 
    .bg-radio { background: linear-gradient(135deg, #C53030 0%, #E53E3E 100%); } 
    .bg-turismo { background: linear-gradient(135deg, #C05621 0%, #ED8936 100%); } 
    .bg-educacion { background: linear-gradient(135deg, #2B6CB0 0%, #4299E1 100%); } 
    .bg-transito { background: linear-gradient(135deg, #285E61 0%, #38B2AC 100%); } 
    .bg-vecinos { background: linear-gradient(135deg, #276749 0%, #48BB78 100%); } 
    .bg-orange { background: linear-gradient(135deg, #9C4221 0%, #DD6B20 100%); }
    .bg-purple { background: linear-gradient(135deg, #553C9A 0%, #805AD5 100%); }
    .bg-teal { background: linear-gradient(135deg, #234E52 0%, #319795 100%); }
    .bg-darkred { background: linear-gradient(135deg, #742A2A 0%, #9B2C2C 100%); }
    .bg-eco { background: linear-gradient(135deg, #22543D 0%, #38A169 100%); } 
    
    @media (max-width: 1024px) {
        .metro-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
        .metro-grid { grid-template-columns: 1fr; grid-auto-rows: auto; }
        .tile-wide, .tile-large { grid-column: span 1; grid-row: span 1; }
        .metro-tile { min-height: 130px; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA: ENLACES RAW CORREGIDOS
# ==========================================
col_logo1, col_logo2, col_texto, col_qr = st.columns([1.2, 1.2, 6, 1.5])

with col_logo1:
    # CORRECCIÓN: Apuntando exactamente a logo_muni.png
    url_municipal = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"
    try:
        st.image(url_municipal, use_container_width=True)
    except:
        st.error("Error")

with col_logo2:
    url_innovacion = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_innovacion.png"
    try:
        st.image(url_innovacion, use_container_width=True)
    except:
        st.error("Error")

with col_texto:
    st.markdown("<h1 style='color: #2D3748; margin-bottom: 0; text-align: center; font-size: 3.2em;'>La Serena SmartCity</h1>", unsafe_allow_html=True)
    
    reloj_html = """
    <div id="reloj_smart" style="font-family: 'Segoe UI', sans-serif; font-size: 1.15em; color: #4A5568; text-align: center; font-weight: 500; margin-top: 5px;"></div>
    <script>
    function actualizarReloj() {
        var hoy = new Date();
        var opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        var fecha = hoy.toLocaleDateString('es-CL', opciones);
        var hora = hoy.toLocaleTimeString('es-CL');
        fecha = fecha.charAt(0).toUpperCase() + fecha.slice(1);
        document.getElementById('reloj_smart').innerHTML = '📍 La Serena | ' + fecha + ' | 🕒 ' + hora;
    }
    setInterval(actualizarReloj, 1000);
    actualizarReloj();
    </script>
    """
    components.html(reloj_html, height=40)

with col_qr:
    qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://app-smartcity-imls.streamlit.app/"
    st.image(qr_url, width=120)
    st.markdown("<p style='text-align: left; font-size: 0.85em; color: #4A5568; font-weight: bold; margin-left: 5px;'>📱 Escanea y Entra</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. CONSTRUCCIÓN DEL MOSAICO HTML
# ==========================================
mosaico_html = """
<div class="metro-grid">

<a href="https://puertaserena.streamlit.app/" target="_blank" class="metro-tile tile-wide bg-alcaldia">
<div><div class="tile-icon">🏛️</div><div class="tile-title">Control Edificio Consistorial</div></div>
<div class="tile-subtitle">Seguridad, registro de visitas y panel de guardia.</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/serenito-app/" target="_blank" class="metro-tile bg-turismo">
<div><div class="tile-icon">🎭</div><div class="tile-title">Eventos y Protocolos</div></div>
<div class="tile-subtitle">Gestión interna de eventos, protocolo y relaciones públicas.</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/RDMLS/" target="_blank" class="metro-tile tile-large bg-radio">
<div><div class="tile-icon">📻</div><div class="tile-title">Plataforma RDMLS</div></div>
<div class="tile-subtitle">Portal interactivo de la Radio Digital Municipal La Serena.</div>
</a>

<a href="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena" target="_blank" class="metro-tile bg-darkred">
<div><div class="tile-icon">🎧</div><div class="tile-title">Señal Radial en Vivo</div></div>
<div class="tile-subtitle">Escucha la transmisión directa de la RDMLS.</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/" target="_blank" class="metro-tile bg-educacion">
<div><div class="tile-icon">🎓</div><div class="tile-title">Portal de Inducción</div></div>
<div class="tile-subtitle">Capacitación y recursos formativos IMLS.</div>
</a>

<a href="https://honorarios-ls-me.streamlit.app/" target="_blank" class="metro-tile tile-wide bg-teal">
<div><div class="tile-icon">💼</div><div class="tile-title">Gestión de Honorarios</div></div>
<div class="tile-subtitle">Plataforma administrativa de servicios a honorarios.</div>
</a>

<a href="https://monitor-laserena.streamlit.app/" target="_blank" class="metro-tile bg-purple">
<div><div class="tile-icon">📡</div><div class="tile-title">Sentinel: Monitor Social</div></div>
<div class="tile-subtitle">Escucha digital y tendencias en redes.</div>
</a>

<div class="metro-tile tile-wide bg-orange disabled-tile">
<div><div class="tile-icon">🚧</div><div class="tile-title">Monitor Vial y Tránsito</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 0.95em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Georeferenciación de baches, luminarias y vehículos.</div>
</div>
</div>

<div class="metro-tile bg-eco disabled-tile">
<div><div class="tile-icon">🌱</div><div class="tile-title">Cuidado Ambiental</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 0.95em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Protección de humedales y entorno ecológico.</div>
</div>
</div>

</div>
"""

# ==========================================
# 5. RENDERIZADO DEL PORTAL
# ==========================================
st.markdown(mosaico_html, unsafe_allow_html=True)

st.write("")
st.divider()
st.caption("Seleccione un servicio para ingresar. Plataforma centralizada de la Ilustre Municipalidad de La Serena.")
