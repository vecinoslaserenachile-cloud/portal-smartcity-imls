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
        border: none;
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
    .bg-alcaldia { background-color: #1A365D; } 
    .bg-radio { background-color: #E53E3E; } 
    .bg-turismo { background-color: #DD6B20; } 
    .bg-educacion { background-color: #3182CE; } 
    .bg-transito { background-color: #38B2AC; } 
    .bg-vecinos { background-color: #38A169; } 
    .bg-orange { background-color: #DD6B20; }
    .bg-purple { background-color: #805AD5; }
    .bg-teal { background-color: #319795; }
    .bg-blue { background-color: #2B6CB0; }
    
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
# 4. CONSTRUCCIÓN DEL MOSAICO (10 SERVICIOS)
# ==========================================
mosaico_html = """
<div class="metro-grid">

    <a href="https://puertaserena.streamlit.app" target="_blank" class="metro-tile tile-wide bg-alcaldia">
        <div>
            <div class="tile-icon">🏛️</div>
            <div class="tile-title">Control Edificio Consistorial</div>
        </div>
        <div class="tile-subtitle">Seguridad, registro de visitas y panel de guardia en tiempo real.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile tile-large bg-radio">
        <div>
            <div class="tile-icon">🎙️</div>
            <div class="tile-title">Radio Digital Municipal (RDMLS)</div>
        </div>
        <div class="tile-subtitle">La voz oficial de la comuna: noticias, música e identidad serenense.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile bg-turismo">
        <div>
            <div class="tile-icon">🏰</div>
            <div class="tile-title">Paseo Patrimonial 3D</div>
        </div>
        <div class="tile-subtitle">Explora los tesoros históricos de La Serena con Serenito.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile bg-transito">
        <div>
            <div class="tile-icon">🌊</div>
            <div class="tile-title">Monitor de Costa</div>
        </div>
        <div class="tile-subtitle">Estado de playas, marejadas e incidencias en el borde costero.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile bg-educacion">
        <div>
            <div class="tile-icon">📅</div>
            <div class="tile-title">Planificador de Viajes</div>
        </div>
        <div class="tile-subtitle">Organiza tus traslados y tiempos de viaje por la región.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile tile-wide bg-orange">
        <div>
            <div class="tile-icon">🚧</div>
            <div class="tile-title">Baches, Luminarias y Tránsito</div>
        </div>
        <div class="tile-subtitle">Reporte ciudadano de accidentes, fallas eléctricas y estado de calles.</div>
    </a>

    <a href="https://monitor-laserena.streamlit.app" target="_blank" class="metro-tile bg-purple">
        <div>
            <div class="tile-icon">📡</div>
            <div class="tile-title">Sentinel: Monitor Social</div>
        </div>
        <div class="tile-subtitle">Escucha digital y tendencias de la comunidad en redes.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile bg-teal">
        <div>
            <div class="tile-icon">🗺️</div>
            <div class="tile-title">Rutas Regionales</div>
        </div>
        <div class="tile-subtitle">Cálculo de distancias a Vicuña, Ovalle, Coquimbo y más.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile bg-blue">
        <div>
            <div class="tile-icon">🇬🇧</div>
            <div class="tile-title">Cursos de Inglés</div>
        </div>
        <div class="tile-subtitle">Plataforma educativa para el desarrollo de la comunidad.</div>
    </a>

    <a href="#" target="_blank" class="metro-tile bg-vecinos">
        <div>
            <div class="tile-icon">🤝</div>
            <div class="tile-title">Atención Vecinos</div>
        </div>
        <div class="tile-subtitle">Portal de servicios y solicitudes directas a la Municipalidad.</div>
    </a>

</div>
"""

# ==========================================
# 5. RENDERIZADO DEL PORTAL (ESENCIAL)
# ==========================================
st.markdown(mosaico_html, unsafe_allow_html=True)

st.write("")
st.divider()
st.caption("Seleccione un servicio para ingresar. Plataforma centralizada de la Ilustre Municipalidad de La Serena.")
