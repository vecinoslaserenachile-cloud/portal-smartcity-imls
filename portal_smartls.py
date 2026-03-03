import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN E ICONO SMART CITY
# ==========================================
st.set_page_config(
    page_title="La Serena SmartCity", 
    page_icon="🏙️", 
    layout="wide"
)

# ==========================================
# 2. ESTILOS CSS: GRILLA INTELIGENTE (SIN HUECOS)
# ==========================================
# Este bloque elimina el efecto Tetris y asegura que se vea bien en móviles
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    /* Grilla que se auto-ajusta para no dejar espacios vacíos a la derecha */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding: 20px 0;
    }
    
    .smart-card {
        border-radius: 15px;
        padding: 25px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 180px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .smart-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    .card-icon { font-size: 3em; margin-bottom: 10px; }
    .card-title { font-size: 1.3em; font-weight: bold; margin-bottom: 8px; color: white; }
    .card-desc { font-size: 0.95em; opacity: 0.9; line-height: 1.4; color: white; }
    
    .card-proximo {
        background-color: #E9ECEF !important;
        color: #ADB5BD !important;
        border: 2px dashed #CED4DA;
        box-shadow: none;
        cursor: default;
    }
    .card-proximo .card-title, .card-proximo .card-desc { color: #ADB5BD !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA INSTITUCIONAL (2 LOGOS)
# ==========================================
col_titulo, col_logos = st.columns([2, 1])

with col_titulo:
    st.markdown("""
        <h1 style='color: #003366; margin-bottom: 0px;'>🏙️ La Serena SmartCity</h1>
        <p style='color: #666; font-size: 1.1em; margin-top: -5px;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>
    """, unsafe_allow_html=True)

with col_logos:
    # Espacio para los dos logotipos (Muni e Innovación)
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Escudo_de_La_Serena.svg/800px-Escudo_de_La_Serena.svg.png", use_container_width=True) 
    with c2:
        st.image("https://via.placeholder.com/300x100/FFFFFF/003366?text=Innovacion+Mundial", use_container_width=True)

st.divider()

# ==========================================
# 4. ENRUTADOR LATERAL
# ==========================================
st.sidebar.title("Navegación Smart")
vista_actual = st.sidebar.selectbox(
    "Seleccione un Servicio", 
    ["🏠 Inicio (Portal General)", "🏢 Acceso Consistorial", "📡 Sentinel Faro"]
)

# ==========================================
# 5. CONTENIDO PRINCIPAL
# ==========================================
if vista_actual == "🏠 Inicio (Portal General)":
    
    # 📻 REPRODUCTOR RADIO DIGITAL (Solo en Inicio)
    st.markdown("<h3 style='color: #D62828;'>📻 Señal en Vivo: Radio Digital Municipal La Serena</h3>", unsafe_allow_html=True)
    
    iframe_radio = """
    <iframe src="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena/embed" 
            frameborder="0" allowtransparency="true" 
            style="width: 100%; min-height: 150px; border: 0; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 30px;">
    </iframe>
    """
    st.markdown(iframe_radio, unsafe_allow_html=True)

    # 🏙️ GRILLA DE SERVICIOS
    servicios = [
        {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y bitácora digital de visitas para el recinto municipal.", "bg": "#1E6091", "link": "https://puertaserena.streamlit.app", "prox": False},
        {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana interactiva con radio y georeferenciación.", "bg": "#D62828", "link": "#", "prox": False},
        {"icon": "📡", "title": "Sentinel Faro", "desc": "Sistema inteligente de Social Listening y monitoreo comunal.", "bg": "#7209B7", "link": "#", "prox": False},
        {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y eventos de la municipalidad.", "bg": "#2A9D8F", "link": "#", "prox": False},
        {"icon": "📄", "title": "Informes Honorarios", "desc": "Generación automática de reportes de gestión mensual.", "bg": "#38B000", "link": "#", "prox": False},
        {"icon": "🚌", "title": "Smart Tránsito LS", "desc": "Monitoreo de flujo vehicular y rutas inteligentes.", "bg": "#FFF", "link": "#", "prox": True}
    ]

    # Construimos el HTML de las tarjetas
    html_cards = "<div class='smart-grid'>"
    for s in servicios:
        clase_extra = "card-proximo" if s["prox"] else ""
        link = s["link"] if not s["prox"] else "#"
        target = "_blank" if not s["prox"] else "_self"
        
        html_cards += f"""
        <a href='{link}' target='{target}' style='text-decoration: none;'>
            <div class='smart-card {clase_extra}' style='background-color: {s["bg"]};'>
                <div>
                    <div class='card-icon'>{s["icon"]}</div>
                    <div class='card-title'>{s["title"]}</div>
                    <div class='card-desc'>{s["desc"]}</div>
                </div>
            </div>
        </a>
        """
    html_cards += "</div>"
    
    # RENDERIZADO FINAL (Aquí es donde estaba el error de la imagen)
    st.markdown(html_cards, unsafe_allow_html=True)

# ------------------------------------------
# Lógica para otras secciones (Apaga la radio)
# ------------------------------------------
elif vista_actual == "🏢 Acceso Consistorial":
    st.header("🏢 Control de Acceso Recinto Municipal")
    st.info("Para mayor seguridad, este sistema corre en un servidor dedicado.")
    st.link_button("Abrir Sistema de Acceso", "https://puertaserena.streamlit.app")

elif vista_actual == "📡 Sentinel Faro":
    st.header("📡 Sentinel Faro - Monitoreo")
    st.warning("Módulo en proceso de integración con la base de datos municipal.")
