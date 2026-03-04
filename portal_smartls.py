import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DEL PORTAL
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🌐", layout="wide")

# ==========================================
# 2. MOTOR GRÁFICO TIPO METRO (MOSAICO CORREGIDO)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F4F6F9; }
    
    /* Ocultar subrayados de enlaces por defecto del navegador */
    a { text-decoration: none !important; }
    
    .metro-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        grid-auto-rows: 150px;
        grid-auto-flow: dense; /* EL SECRETO: Hace que los bloques encajen como Tetris sin dejar huecos */
        gap: 15px;
        padding: 20px 0;
    }
    
    .metro-tile {
        color: white !important;
        text-decoration: none !important;
        padding: 20px;
        border-radius: 8px;
        font-family: 'Segoe UI', sans-serif;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        cursor: pointer;
        height: 100%;
        border: none;
    }
    
    .metro-tile * {
        text-decoration: none !important;
        color: white !important;
    }
    
    .metro-tile:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    .tile-wide { grid-column: span 2; }
    .tile-large { grid-column: span 2; grid-row: span 2; }
    
    .tile-icon { font-size: 2.2em; margin-bottom: 5px; }
    .tile-title { font-weight: 700; font-size: 1.2em; line-height: 1.2; margin-bottom: 5px; }
    .tile-subtitle { font-size: 0.85em; opacity: 0.95; font-weight: 400; }
    
    .bg-alcaldia { background-color: #1A365D; } 
    .bg-radio { background-color: #E53E3E; } 
    .bg-turismo { background-color: #DD6B20; } 
    .bg-educacion { background-color: #3182CE; } 
    .bg-transito { background-color: #38B2AC; } 
    .bg-vecinos { background-color: #38A169; } 
    .bg-orange { background-color: #DD6B20; }
    .bg-purple { background-color: #805AD5; }
    .bg-teal { background-color: #319795; }
    .bg-darkred { background-color: #9B2C2C; }
    .bg-eco { background-color: #2F855A; } 
    
    @media (max-width: 768px) {
        .tile-wide, .tile-large { grid-column: span 1; grid-row: span 1; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON LOGOS Y QR RESTAURADOS
# ==========================================
col_logo1, col_texto, col_qr = st.columns([1.5, 6, 1.5])

with col_logo1:
    # AQUÍ VAN TUS LOGOS INSTITUCIONALES (Puedes reemplazar el link por tus imágenes reales)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Escudo_de_La_Serena.svg/800px-Escudo_de_La_Serena.svg.png", width=90)

with col_texto:
    st.markdown("<h1 style='color: #2D3748; margin-bottom: 0; text-align: center;'>La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #718096; margin-top: 0; text-align: center;'>Portal de Servicios Integrados | I.M. La Serena</h4>", unsafe_allow_html=True)

with col_qr:
    # AQUÍ VA TU CÓDIGO QR (Reemplaza el link por tu imagen de QR)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png", width=90)
    st.caption("Escanear Portal")

st.divider()

# ==========================================
# 4. CONSTRUCCIÓN DEL MOSAICO HTML (Sin Subrayados)
# ==========================================
mosaico_html = """
<div class="metro-grid">

<a href="https://puertaserena.streamlit.app/" target="_blank" class="metro-tile tile-wide bg-alcaldia">
<div><div class="tile-icon">🏛️</div><div class="tile-title">Control Edificio Consistorial</div></div>
<div class="tile-subtitle">Seguridad, registro de visitas y panel de guardia.</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/serenito-app/" target="_blank" class="metro-tile bg-turismo">
<div><div class="tile-icon">🏰</div><div class="tile-title">Paseo 3D Serenito</div></div>
<div class="tile-subtitle">Explora los tesoros históricos y personajes de la ciudad.</div>
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

<a href="#" class="metro-tile tile-wide bg-orange">
<div><div class="tile-icon">🚧</div><div class="tile-title">Monitor Vial y Tránsito</div></div>
<div class="tile-subtitle">🚧 En Desarrollo: Georeferenciación de baches, luminarias, vehículos en pana y abandonados.</div>
</a>

<a href="#" class="metro-tile bg-eco">
<div><div class="tile-icon">🌱</div><div class="tile-title">Cuidado Ambiental</div></div>
<div class="tile-subtitle">🚧 En Desarrollo: Reporte y protección de humedales, playas, ríos y entorno ecológico.</div>
</a>

</div>
"""

# ==========================================
# 5. RENDERIZADO DEL PORTAL
# ==========================================
st.markdown(mosaico_html, unsafe_allow_html=True)

st.write("")
st.divider()
st.caption("Seleccione un servicio para ingresar. Plataforma centralizada de la Ilustre Municipalidad de La Serena.")
