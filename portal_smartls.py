import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON (🏛️ Institucional)
# ==========================================
# Cambiamos el icono por uno más serio y elegante
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏛️", layout="wide")

# ==========================================
# 2. ESTILOS DEL MOSAICO Y BOTONES DESACTIVADOS
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    .mosaico-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding-bottom: 30px;
    }

    .mosaico-card {
        border-radius: 15px;
        padding: 25px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 190px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        transition: transform 0.2s ease;
    }

    /* Efecto hover solo para botones activos */
    .card-activa:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.25);
    }

    /* Estilo para botones EN DESARROLLO (Desactivados) */
    .card-desactivada {
        background-color: #E9ECEF !important;
        color: #ADB5BD !important;
        border: 2px dashed #CED4DA;
        box-shadow: none !important;
        cursor: not-allowed !important;
    }
    .card-desactivada .card-title, .card-desactivada .card-desc { color: #ADB5BD !important; }

    .card-icon { font-size: 3.5em; margin-bottom: 12px; }
    .card-title { font-size: 1.5em; font-weight: bold; margin-bottom: 8px; line-height: 1.1; }
    .card-desc { font-size: 1em; opacity: 0.95; line-height: 1.3; }
    
    /* Ajuste para el logo con fondo */
    .logo-blend {
        mix-blend-mode: multiply; /* Esto ayuda a "quitar" fondos blancos de PNGs */
        filter: contrast(110%);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON LOGOS (RAÍZ)
# ==========================================
col_titulo, col_logos = st.columns([2, 1])

with col_titulo:
    st.markdown("<h1 style='color: #003366; margin-bottom: 0px;'>🏛️ La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.2em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_logos:
    c1, c2 = st.columns(2)
    with c1:
        # Aquí cargará tu nuevo logo municipal en rojo
        st.image("logo_muni.png", use_container_width=True) 
    with c2:
        # Aplicamos el filtro para disimular el fondo del logo de innovación
        st.image("logo_innovacion.png", use_container_width=True)

st.divider()

# ==========================================
# 4. REPRODUCTOR DE RADIO (CONEXIÓN SEGURA)
# ==========================================
st.markdown("<p style='color: #D62828; font-weight: bold; margin-bottom: 5px;'>📻 Radio Digital Municipal En Vivo:</p>", unsafe_allow_html=True)
# He actualizado la fuente del audio para asegurar compatibilidad
st.audio("https://az11.yesstreaming.net/radio/8010/radio.mp3", format="audio/mpeg")

# ==========================================
# 5. MOSAICO DE SERVICIOS (LÓGICA DE DESARROLLO)
# ==========================================
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Control de seguridad y bitácora digital.", "bg": "#1E6091", "link": "https://puertaserena.streamlit.app", "dev": False},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana y georeferenciación.", "bg": "#D62828", "link": "#", "dev": False},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo comunal.", "bg": "#7209B7", "link": "#", "dev": False},
    {"icon": "🎙️", "title": "Pódcasts IMLS", "desc": "Entrevistas y programas municipales.", "bg": "#F77F00", "link": "#", "dev": False},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación.", "bg": "#2A9D8F", "link": "#", "dev": False},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios.", "bg": "#184E77", "link": "#", "dev": False},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes.", "bg": "#38B000", "link": "#", "dev": False},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "[EN DESARROLLO] Monitoreo ambiental costero.", "bg": "#0077B6", "link": "#", "dev": True},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "[EN DESARROLLO] Tránsito, luminarias y baches.", "bg": "#457B9D", "link": "#", "dev": True}
]

# Renderizado del mosaico con detección de estado
cols = st.columns(3)
for i, s in enumerate(servicios):
    with cols[i % 3]:
        if s["dev"]:
            # Si está en desarrollo, se muestra el cuadro pero sin enlace
            card_html = f"""
            <div class='mosaico-card card-desactivada'>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
            """
        else:
            # Si está activo, funciona normalmente como enlace
            card_html = f"""
            <a href='{s["link"]}' target='_blank' style='text-decoration: none;'>
                <div class='mosaico-card card-activa' style='background-color: {s["bg"]};'>
                    <div class='card-icon'>{s["icon"]}</div>
                    <div class='card-title'>{s["title"]}</div>
                    <div class='card-desc'>{s["desc"]}</div>
                </div>
            </a>
            """
        st.markdown(card_html, unsafe_allow_html=True)
