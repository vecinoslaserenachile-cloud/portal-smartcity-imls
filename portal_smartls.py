import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DEL PORTAL
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🌐", layout="wide")

# ==========================================
# 2. MOTOR GRÁFICO TIPO METRO (MOSAICO)
# ==========================================
st.markdown("""
    <style>
    /* Fondo limpio y moderno */
    .stApp { background-color: #F4F6F9; }
    
    /* Contenedor del Mosaico */
    .metro-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        grid-auto-rows: 150px;
        gap: 15px;
        padding: 20px 0;
    }
    
    /* Diseño de la baldosa (Tile) */
    .metro-tile {
        color: white !important;
        text-decoration: none;
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
    }
    
    .metro-tile:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    /* Tamaños especiales */
    .tile-wide { grid-column: span 2; }
    .tile-large { grid-column: span 2; grid-row: span 2; }
    
    /* Textos internos */
    .tile-icon { font-size: 3em; margin-bottom: 10px; }
    .tile-title { font-weight: 700; font-size: 1.3em; line-height: 1.2; margin-bottom: 5px; }
    .tile-subtitle { font-size: 0.9em; opacity: 0.95; font-weight: 400; }
    
    /* Paleta de Colores Institucionales */
    .bg-alcaldia { background-color: #1A365D; } /* Azul oscuro */
    .bg-radio { background-color: #E53E3E; } /* Rojo */
    .bg-turismo { background-color: #DD6B20; } /* Naranja */
    .bg-educacion { background-color: #3182CE; } /* Azul claro */
    .bg-transito { background-color: #38B2AC; } /* Turquesa */
    .bg-vecinos { background-color: #38A169; } /* Verde */
    .bg-purple { background-color: #805AD5; } /* Morado tecnológico */
    .bg-orange { background-color: #ED8936; } /* Naranja claro */
    
    /* Ajuste responsivo para móviles */
    @media (max-width: 768px) {
        .tile-wide, .tile-large { grid-column: span 1; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA DEL PORTAL
# ==========================================
col_logo, col_texto = st.columns([1, 8])
with col_logo:
    st.markdown("<div style='font-size: 65px; text-align: center; margin-top: -10px;'>🌐</div>", unsafe_allow_html=True)
with col_texto:
    st.markdown("<h1 style='color: #2D3748; margin-bottom: 0;'>La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #718096; margin-top: 0;'>Portal de Servicios Integrados | I.M. La Serena</h4>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. CONSTRUCCIÓN DEL MOSAICO (SERVICIOS REALES)
# ==========================================
mosaico_html = """
<div class="metro-grid">

    <a href="https://puertaserena.streamlit.app/" target="_blank" class="metro-tile tile-wide bg-alcaldia">
        <div>
            <div class="tile-icon">🏛️</div>
            <div class="tile-title">Piloto Acceso Edificio Consistorial</div>
        </div>
        <div class="tile-subtitle">Sistema de seguridad, registro de visitas y panel de guardia.</div>
    </a>

    <a href="https://vecinoslaserenachile-cloud.github.io/RDMLS/" target="_blank" class="metro-tile tile-large bg-radio">
        <div>
            <div class="tile-icon">🌐</div>
            <div class="tile-title">Portal RDMLS Integral</div>
        </div>
        <div class="tile-subtitle">Radio, georeferenciación y herramientas multimedia para interactuar con los vecinos de la comuna.</div>
    </a>

    <a href="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena" target="_blank" class="metro-tile bg-orange">
        <div>
            <div class="tile-icon">🎙️</div>
            <div class="tile-title">Señal Radial RDMLS</div>
        </div>
        <div class="tile-subtitle">Escucha la transmisión en vivo y directo.</div>
    </a>

    <a href="https://monitor-laserena.streamlit.app/" target="_blank" class="metro-tile tile-wide bg-purple">
        <div>
            <div class="tile-icon">📡</div>
            <div class="tile-title">Sentinel Faro</div>
        </div>
        <div class="tile-subtitle">Monitor de Social Listening e inteligencia de datos comunal.</div>
    </a>

    <a href="https://vecinoslaserenachile-cloud.github.io/serenito-app/" target="_blank" class="metro-tile bg-turismo">
        <div>
            <div class="tile-icon">🎭</div>
            <div class="tile-title">Protocolo y Eventos</div>
        </div>
        <div class="tile-subtitle">Plataforma oficial de gestión de eventos con Serenito.</div>
    </a>

    <a href="https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/" target="_blank" class="metro-tile bg-educacion">
        <div>
            <div class="tile-icon">🎓</div>
            <div class="tile-title">Inducción E-Learning</div>
        </div>
        <div class="tile-subtitle">Plataforma de capacitación para funcionarios nuevos.</div>
    </a>

    <a href="https://honorarios-ls-me.streamlit.app/" target="_blank" class="metro-tile bg-transito">
        <div>
            <div class="tile-icon">📄</div>
            <div class="tile-title">Informes Honorarios</div>
        </div>
        <div class="tile-subtitle">Generador automático de reportes para prestadores de servicios.</div>
    </a>

</div>
"""

# Renderizar el HTML en Streamlit
st.markdown(mosaico_html, unsafe_allow_html=True)

st.write("")
st.divider()
st.caption("Seleccione un servicio para ingresar. Plataforma centralizada de la Ilustre Municipalidad de La Serena.")
