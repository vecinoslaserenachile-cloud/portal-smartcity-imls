import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y FAVICON INSTITUCIONAL (🏛️)
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🏛️", layout="wide")

# ==========================================
# 2. ESTILOS DETALLADOS: EFECTO GLASEADO (GLASSMORPHISM)
# ==========================================
st.markdown("""
    <style>
    /* Fondo de la aplicación */
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Contenedor principal del mosaico */
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 25px;
        padding: 30px 0;
    }
    
    /* Estilo base de la tarjeta (Mosaico Glaseado) */
    .mosaico-card {
        border-radius: 20px;
        padding: 30px;
        color: white !important;
        text-decoration: none !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 200px;
        position: relative;
        overflow: hidden;
        
        /* Efecto Vidrioso */
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.1); /* Fondo translúcido */
        border: 1px solid rgba(255, 255, 255, 0.2); /* Borde suave */
        
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    /* Efecto hover solo para tarjetas activas */
    .card-activa:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.15); /* Aclarar un poco al hover */
    }
    
    /* Estilo para tarjetas EN DESARROLLO (Grises y bloqueadas) */
    .card-desactivada {
        background-color: rgba(233, 236, 239, 0.7) !important;
        color: #ADB5BD !important;
        border: 2px dashed #CED4DA;
        box-shadow: none !important;
        cursor: not-allowed !important;
        backdrop-filter: blur(5px);
    }
    .card-desactivada .card-title, .card-desactivada .card-desc {
        color: #ADB5BD !important;
    }

    /* Detalles de contenido de tarjeta */
    .card-icon { font-size: 3.8em; margin-bottom: 15px; }
    .card-title { font-size: 1.6em; font-weight: bold; margin-bottom: 10px; line-height: 1.1; }
    .card-desc { font-size: 1.05em; opacity: 0.95; line-height: 1.4; }
    
    /* Ajuste para equilibrar logos */
    .header-logo {
        max-height: 80px; /* Forzamos altura máxima para equilibrar */
        width: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Filtro para el logo de Innovación (Pela el fondo blanco) */
    .logo-blend {
        mix-blend-mode: multiply;
        filter: contrast(110%);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA CON LOGOS EQUILIBRADOS
# ==========================================
col_titulo, col_logos = st.columns([2, 1.2]) # Ajuste de columnas para dar más aire a los logos

with col_titulo:
    st.markdown("<h1 style='color: #003366; margin-bottom: 0px;'>🏛️ La Serena SmartCity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 1.25em;'>Portal de Servicios Integrados | Ilustre Municipalidad de La Serena</p>", unsafe_allow_html=True)

with col_logos:
    # Contenedor para logos equilibrados
    c1, c2 = st.columns(2)
    with c1:
        # Se asume que subió logo_muni.png a la raíz
        # Usamos HTML para aplicar la clase header-logo y equilibrar tamaño
        html_logo_muni = '<img src="app/static/logo_muni.png" class="header-logo">'
        # st.image("logo_muni.png", use_container_width=True) # Versión streamlit si el CSS falla
        st.markdown(html_logo_muni, unsafe_allow_html=True)
        
    with c2:
        # Logo Innovación con filtro de mezcla y clase header-logo
        # Usamos HTML para aplicar la clase y el filtro
        html_logo_innova = '<img src="app/static/logo_innovacion.png" class="header-logo logo-blend">'
        st.markdown(html_logo_innova, unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. RADIO SIMPLIFICADA (BOTÓN PLAY ESTABLE)
# ==========================================
# Se elimina el reproductor grande. La radio principal es el botón naranja.
# Pero dejamos un control discreto aquí por si acaso, usando el stream MP3 directo.
st.markdown("<p style='color: #D62828; font-weight: bold; margin-bottom: 5px;'>📻 Señal en Vivo (Stream Directo):</p>", unsafe_allow_html=True)
st.audio("https://az11.yesstreaming.net/radio/8010/radio.mp3", format="audio/mp3") 
st.write("") # Espaciado

# ==========================================
# 5. ESTRUCTURA DE LA BOTONERA (GRILLA)
# ==========================================
# El orden refleja las prioridades de la I.M. La Serena.
servicios = [
    {"icon": "🏢", "title": "Acceso Edificio Consistorial", "desc": "Seguridad y bitácora digital de visitas para el recinto municipal.", "bg": "linear-gradient(135deg, #1E6091 0%, #114871 100%)", "link": "https://puertaserena.streamlit.app", "dev": False},
    {"icon": "🌐", "title": "Portal RDMLS Integral", "desc": "Plataforma ciudadana interactiva con radio y georeferenciación.", "bg": "linear-gradient(135deg, #D62828 0%, #A31B1B 100%)", "link": "#", "dev": False},
    {"icon": "📡", "title": "Sentinel Faro", "desc": "Sistema inteligente de Social Listening comunal.", "bg": "linear-gradient(135deg, #7209B7 0%, #5A0693 100%)", "link": "#", "dev": False},
    {"icon": "📻", "title": "Radio Digital RDMLS", "desc": "Señal en vivo de la Radio Digital Municipal La Serena.", "bg": "linear-gradient(135deg, #F77F00 0%, #C66600 100%)", "link": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena", "dev": False},
    {"icon": "🎭", "title": "Protocolo y Eventos", "desc": "Gestión institucional y coordinación de eventos municipales.", "bg": "linear-gradient(135deg, #2A9D8F 0%, #1F796E 100%)", "link": "#", "dev": False},
    {"icon": "🎓", "title": "Inducción E-Learning", "desc": "Capacitación digital para funcionarios.", "bg": "linear-gradient(135deg, #184E77 0%, #0E3655 100%)", "link": "#", "dev": False},
    {"icon": "📄", "title": "Informes Honorarios", "desc": "Generador automático de reportes de gestión.", "bg": "linear-gradient(135deg, #38B000 0%, #2A8700 100%)", "link": "#", "dev": False},
    {"icon": "⛱️", "title": "Playas y Humedales", "desc": "MONITOREO AMBIENTAL EN DESARROLLO.", "bg": "linear-gradient(135deg, #0077B6 0%, #005A8D 100%)", "link": "#", "dev": True},
    {"icon": "🚦", "title": "Monitoreo Urbano", "desc": "TRÁNSITO Y LUMINARIAS EN DESARROLLO.", "bg": "linear-gradient(135deg, #457B9D 0%, #355F7A 100%)", "link": "#", "dev": True}
]

# Renderizado de la grilla
html_final = "<div class='smart-grid'>"
for s in servicios:
    clase = "card-desactivada" if s["dev"] else "card-activa"
    url = s["link"] if not s["dev"] else "#"
    target = "_blank" if not s["dev"] else "_self"
    
    # Solo las activas son enlaces clicables
    if not s["dev"]:
        html_final += f"""
        <a href='{url}' target='{target}' style='text-decoration: none;'>
            <div class='mosaico-card {clase}' style='background: {s["bg"]};'>
                <div>
                    <div class='card-icon'>{s["icon"]}</div>
                    <div class='card-title'>{s["title"]}</div>
                    <div class='card-desc'>{s["desc"]}</div>
                </div>
            </div>
        </a>
        """
    else:
        # Las desactivadas son solo un div sin enlace
        html_final += f"""
        <div class='mosaico-card {clase}'>
            <div>
                <div class='card-icon'>{s["icon"]}</div>
                <div class='card-title'>{s["title"]}</div>
                <div class='card-desc'>{s["desc"]}</div>
            </div>
        </div>
        """
html_final += "</div>"

# Renderizado final de todo el bloque
st.markdown(html_final, unsafe_allow_html=True)
