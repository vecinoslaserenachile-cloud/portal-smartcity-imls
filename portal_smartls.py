import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN E ICONO SMART CITY
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏙️", layout="wide")

# ==========================================
# 2. CABECERA INSTITUCIONAL (2 LOGOS)
# ==========================================
col_titulo, col_espacio, col_logos = st.columns([2, 0.5, 1.5])

with col_titulo:
    st.markdown("""
        <h1 style='color: #003366; margin-bottom: 0px;'>🏙️ La Serena SmartCity</h1>
        <p style='color: #666; font-size: 1.1em; margin-top: -5px;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>
    """, unsafe_allow_html=True)

with col_logos:
    c_logo1, c_logo2 = st.columns(2)
    with c_logo1:
        # Logo Institucional IMLS
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Escudo_de_La_Serena.svg/800px-Escudo_de_La_Serena.svg.png", use_container_width=True) 
    with c_logo2:
        # Logo Innovación Mundial (Espacio de reserva)
        st.image("https://via.placeholder.com/300x100/FFFFFF/003366?text=Ciudad+Innovacion+Mundial", use_container_width=True)

st.divider()

# ==========================================
# 3. ENRUTADOR LATERAL (DETERMINA SI SE APAGA LA RADIO)
# ==========================================
st.sidebar.title("Navegación Smart")
vista_actual = st.sidebar.selectbox("Seleccione un Servicio", ["🏠 Inicio (Portal General)", "🏢 Acceso Consistorial", "🌐 Portal RDMLS", "📡 Sentinel Faro"])

# ==========================================
# 4. REPRODUCTOR RDMLS (SOLO EN EL INICIO)
# ==========================================
# Si el usuario navega a otra solución, el reproductor desaparece automáticamente
if vista_actual == "🏠 Inicio (Portal General)":
    st.markdown("<h3 style='color: #D62828;'>📻 Señal en Vivo: Radio Digital Municipal La Serena</h3>", unsafe_allow_html=True)
    
    iframe_radio = """
    <iframe src="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena/embed" 
            frameborder="0" allowtransparency="true" 
            style="width: 100%; min-height: 150px; border: 0; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 30px;">
    </iframe>
    """
    st.markdown(iframe_radio, unsafe_allow_html=True)

# ==========================================
# 5. GRILLA CSS INTELIGENTE (SIN HUECOS)
# ==========================================
st.markdown("""
    <style>
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding-bottom: 40px;
    }
    .smart-card {
        border-radius: 15px; padding: 25px; color: white; text-decoration: none;
        display: flex; flex-direction: column; justify-content: space-between;
        min-height: 180px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .smart-card:hover { transform: scale(1.02); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
    .card-icon { font-size: 3em; margin-bottom: 10px; }
    .card-title { font-size: 1.3em; font-weight: bold; margin-bottom: 8px; }
    .card-desc { font-size: 0.9em; opacity: 0.85; line-height: 1.4; }
    .card-proximo { background-color: #E9ECEF !important; color: #ADB5BD !important; border: 2px dashed #CED4DA; cursor: default; }
    </style>
""", unsafe_allow_html=True)

# Solo mostramos las tarjetas si estamos en el Inicio
if vista_actual == "🏠 Inicio (Portal General)":
    servicios = [
        {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Control de seguridad y bitácora digital de visitas.", "bg": "#1E6091", "link": "https://puertaserena.streamlit.app", "prox": False},
        {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana interactiva y georeferenciación.", "bg": "#D62828", "link": "#", "prox": False},
        {"icon": "📡", "title": "Sentinel Faro", "desc": "Social Listening y monitoreo de datos comunales.", "bg": "#7209B7", "link": "#", "prox": False},
        {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y eventos municipales.", "bg": "#2A9D8F", "link": "#", "prox": False},
        {"icon": "📄", "title": "Informes Honorarios", "desc": "Generación automática de reportes de gestión.", "bg": "#38B000", "link": "#", "prox": False},
        {"icon": "🚌", "title": "Smart Tránsito LS", "desc": "Monitoreo de flujo vehicular y rutas inteligentes.", "bg": "#FFF", "link": "#", "prox": True}
    ]

    html_cards = "<div class='smart-grid'>"
    for s in servicios:
        clase = "card-proximo" if s["prox"] else ""
        link = "#" if s["prox"] else s["link"]
        html_cards += f"""
        <a href='{link}' target='_blank' style='text-decoration: none;'>
            <div class='smart-card {clase}' style='background-color: {s["bg"]};'>
                <div>
                    <div class='card-icon'>{s["icon"]}</div>
                    <div class='card-title'>{s["title"]}</div>
                    <div class='card-desc'>{s["desc"]}</div>
                </div>
            </div>
        </a>
        """
    html_cards += "</div>"
    st.markdown(html_cards, unsafe_allow_html=True)

# ==========================================
# 6. LÓGICA DE SUB-PÁGINAS (Contenedores vacíos para futuro)
# ==========================================
elif vista_actual == "🏢 Acceso Consistorial":
    st.info("Esta sección se abre en una pestaña externa, pero si decides integrarla aquí, el reproductor de arriba se mantendrá apagado.")
    st.markdown("[Abrir Sistema de Acceso](https://puertaserena.streamlit.app)")

elif vista_actual == "🌐 Portal RDMLS":
    st.warning("⚠️ Al entrar aquí, la radio del portal se apaga para que escuches la radio propia de este servicio.")
