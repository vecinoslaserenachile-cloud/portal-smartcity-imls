"""
=============================================================================
SISTEMA CENTRAL DE OPERACIONES - LA SERENA SMARTCITY
=============================================================================
Cliente: Ilustre Municipalidad de La Serena
Desarrollo: Vecinos La Serena Spa
Rol: Director de Proyecto / Arquitectura
Versión: 2.0.0 (Enterprise Edition)
Descripción: Portal unificado de servicios municipales integrados.
Arquitectura escalable basada en Streamlit con renderizado HTML/CSS/JS nativo.

Este módulo gestiona la capa de presentación (Frontend) y la lógica de
enrutamiento hacia las distintas aplicaciones del ecosistema SmartCity.
=============================================================================
"""

import streamlit as st
import streamlit.components.v1 as components

# =============================================================================
# VARIABLES GLOBALES Y CONFIGURACIÓN DE RUTAS
# =============================================================================
# Direcciones base para recursos estáticos (Logos)
URL_LOGO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"
URL_LOGO_INNO = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_innovacion.png"
URL_QR_BASE = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="
URL_PORTAL_APP = "https://app-smartcity-imls.streamlit.app/"

# =============================================================================
# BASE DE DATOS DE APLICACIONES (DICCIONARIOS)
# =============================================================================
# Módulos actualmente operativos al 100% en el ecosistema
ACTIVE_SERVICES = [
    {
        "icon": "🏛️",
        "title": "Control Acceso Visitas",
        "subtitle": "Red de Recintos Municipales | I.M. La Serena",
        "url": "https://puertaserena.streamlit.app/",
        "css_class": "bg-alcaldia"
    },
    {
        "icon": "🎭",
        "title": "Eventos y Protocolos",
        "subtitle": "Gestión interna de eventos, protocolo y relaciones públicas.",
        "url": "https://vecinoslaserenachile-cloud.github.io/serenito-app/",
        "css_class": "bg-turismo"
    },
    {
        "icon": "📻",
        "title": "Plataforma RDMLS",
        "subtitle": "Portal interactivo de la Radio Digital Municipal La Serena.",
        "url": "https://vecinoslaserenachile-cloud.github.io/RDMLS/",
        "css_class": "bg-radio"
    },
    {
        "icon": "🎧",
        "title": "Señal Radial en Vivo",
        "subtitle": "Escucha la transmisión directa de la RDMLS.",
        "url": "https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena",
        "css_class": "bg-darkred"
    },
    {
        "icon": "🎓",
        "title": "Portal de Inducción",
        "subtitle": "Capacitación y recursos formativos IMLS.",
        "url": "https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/",
        "css_class": "bg-educacion"
    },
    {
        "icon": "💼",
        "title": "Gestión de Honorarios",
        "subtitle": "Plataforma administrativa de servicios a honorarios.",
        "url": "https://honorarios-ls-me.streamlit.app/",
        "css_class": "bg-teal"
    },
    {
        "icon": "📡",
        "title": "Sentinel: Monitor Social",
        "subtitle": "Escucha digital y tendencias en redes.",
        "url": "https://monitor-laserena.streamlit.app/",
        "css_class": "bg-purple"
    },
    {
        "icon": "🛡️",
        "title": "Acceso Municipal - Fiscalización",
        "subtitle": "Portal exclusivo para funcionarios y Centro de Gestión.",
        "url": "https://redvecinos-smart-imls.web.app/",
        "css_class": "bg-blue-neon"
    },
    {
        "icon": "📱",
        "title": "Nueva Alerta de Seguridad",
        "subtitle": "Formulario de reporte in situ para recintos privados.",
        "url": "https://redvecinos-smart-imls.web.app/#/fiscalizacion",
        "css_class": "bg-vecinos"
    }
]

# Módulos en fase de desarrollo (Próximamente integrados)
DEVELOPMENT_SERVICES = [
    {
        "icon": "🚧",
        "title": "Monitor Vial y Tránsito",
        "subtitle": "Georeferenciación de baches, luminarias y vehículos.",
        "css_class": "bg-orange"
    },
    {
        "icon": "🌱",
        "title": "Cuidado Ambiental",
        "subtitle": "Protección de humedales y entorno ecológico.",
        "css_class": "bg-eco"
    },
    {
        "icon": "🚰",
        "title": "Servicios Básicos",
        "subtitle": "Control de agua, alcantarillado, redes eléctricas y telecomunicaciones.",
        "css_class": "bg-transito"
    },
    {
        "icon": "🎨",
        "title": "Cultura y Arte Urbano",
        "subtitle": "Música, artes escénicas, grafiti y expresiones urbanas.",
        "css_class": "bg-art"
    },
    {
        "icon": "🧘‍♀️",
        "title": "Deportes y Bienestar",
        "subtitle": "Plataforma interactiva de yoga, fitness, wellness y actividades deportivas.",
        "css_class": "bg-turismo"
    }
]


# =============================================================================
# FUNCIONES DE RENDERIZADO DE ESTILOS (CSS)
# =============================================================================
def load_enterprise_css():
    """
    Inyecta el código CSS crítico para el motor gráfico tipo 'Metro'.
    Gestiona la responsividad (Desktop, Tablet, Mobile) y los degradados premium.
    """
    css_code = """
    <style>
    /* =======================================================
       ESTILOS BASE DEL SISTEMA
       ======================================================= */
    .stApp { background-color: #F8FAFC; }
    
    a { text-decoration: none !important; }
    
    /* =======================================================
       GRILLA METRO (MOSAICO PRINCIPAL)
       ======================================================= */
    .metro-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-auto-rows: minmax(180px, auto); 
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
        height: 100%; 
    }
    
    .metro-tile * { text-decoration: none !important; color: white !important; }
    
    /* Interacciones activas */
    a.metro-tile:hover {
        transform: scale(1.02) translateY(-4px);
        box-shadow: 0 15px 25px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    /* =======================================================
       ESTADO: EN DESARROLLO (OPACIDAD Y ESCALA DE GRISES)
       ======================================================= */
    .disabled-tile {
        cursor: default;
        opacity: 0.5; 
        filter: grayscale(50%); 
    }
    
    /* =======================================================
       TIPOGRAFÍA DE BALDOSAS
       ======================================================= */
    .tile-icon { 
        font-size: 2.6em; 
        margin-bottom: 5px; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2); 
    }
    .tile-title { 
        font-weight: 700; 
        font-size: 1.4em; 
        line-height: 1.2; 
        margin-bottom: 5px; 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2); 
    }
    .tile-subtitle { 
        font-size: 0.95em; 
        opacity: 0.95; 
        font-weight: 400; 
        line-height: 1.3; 
    }
    
    /* =======================================================
       PALETA DE COLORES (DEGRADADOS PREMIUM)
       ======================================================= */
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
    .bg-blue-neon { background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); border: 1px solid #00ffcc;}
    .bg-art { background: linear-gradient(135deg, #D53F8C 0%, #B83280 100%); }
    
    /* =======================================================
       CLASES ESTRUCTURALES DE ESCRITORIO
       ======================================================= */
    .logo-muni { width: 100%; object-fit: contain; }
    .logo-inno-desktop { width: 100%; object-fit: contain; }
    .logo-inno-mobile { display: none; } 
    .qr-wrapper { display: flex; flex-direction: column; align-items: flex-start; }
    .qr-wrapper img { width: 120px; }
    
    .main-title {
        color: #2D3748; 
        margin-bottom: 0; 
        text-align: center; 
        font-size: 3.2em;
    }

    /* =======================================================
       MEDIA QUERIES - TABLETS
       ======================================================= */
    @media (max-width: 1024px) {
        .metro-grid { grid-template-columns: repeat(2, 1fr); }
    }
    
    /* =======================================================
       MEDIA QUERIES - MOBILE (CIRUGÍA DE PRECISIÓN)
       ======================================================= */
    @media (max-width: 768px) {
        .metro-grid { grid-template-columns: 1fr; grid-auto-rows: auto; }
        .metro-tile { min-height: 160px; } 
        
        /* Ajuste de escudo */
        .logo-muni { width: 45%; display: block; margin: 0 auto; }
        
        /* Ajuste de Título Principal */
        .main-title {
            color: #E53E3E !important; 
            font-size: 1.7em !important; 
            white-space: nowrap !important; 
            margin-top: 15px !important;
        }
        
        /* Reubicación de Logo Innovación */
        .logo-inno-desktop { display: none; }
        .logo-inno-mobile { 
            display: block; 
            width: 360px !important; 
            max-width: 90%; 
            margin: 40px auto 20px auto; 
            object-fit: contain; 
        }
        
        /* Ajuste de QR */
        .qr-wrapper { 
            align-items: center; 
            margin-top: 10px; 
            margin-bottom: 25px; 
            width: 100%; 
            text-align: center; 
        }
        .qr-wrapper img { width: 170px !important; }
    }
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)


# =============================================================================
# FUNCIONES DE COMPONENTES DE LA INTERFAZ
# =============================================================================
def render_header():
    """
    Genera la cabecera del portal.
    Distribuye columnas para escudos, títulos, reloj dinámico y QR de acceso.
    """
    col_logo1, col_logo2, col_texto, col_qr = st.columns([1.2, 1.2, 6, 1.5])

    # Columna 1: Logo Ilustre Municipalidad
    with col_logo1:
        img_muni = f'<img src="{URL_LOGO_MUNI}" class="logo-muni">'
        st.markdown(img_muni, unsafe_allow_html=True)

    # Columna 2: Logo Innovación (Oculto en móvil desde CSS)
    with col_logo2:
        img_inno = f'<img src="{URL_LOGO_INNO}" class="logo-inno-desktop">'
        st.markdown(img_inno, unsafe_allow_html=True)

    # Columna 3: Título Central y Reloj Inteligente
    with col_texto:
        st.markdown("<h1 class='main-title'>La Serena SmartCity</h1>", unsafe_allow_html=True)
        
        # Script de JS inyectado para reloj en tiempo real
        reloj_html = """
        <div id="reloj_smart" style="font-family: 'Segoe UI', sans-serif; font-size: 1.1em; color: #4A5568; text-align: center; font-weight: 500; margin-top: 5px;"></div>
        <script>
        function actualizarReloj() {
            var hoy = new Date();
            var opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            var fecha = hoy.toLocaleDateString('es-CL', opciones);
            var hora = hoy.toLocaleTimeString('es-CL');
            fecha = fecha.charAt(0).toUpperCase() + fecha.slice(1);
            document.getElementById('reloj_smart').innerHTML = '📍 La Serena | ' + fecha + '<br>🕒 ' + hora;
        }
        setInterval(actualizarReloj, 1000);
        actualizarReloj();
        </script>
        """
        components.html(reloj_html, height=75)

    # Columna 4: Código QR generado dinámicamente
    with col_qr:
        qr_html = f"""
        <div class="qr-wrapper">
            <img src="{URL_QR_BASE}{URL_PORTAL_APP}">
            <p style='font-size: 0.85em; color: #4A5568; font-weight: bold; margin-top: 5px; margin-bottom: 0;'>📱 Escanea y Entra</p>
        </div>
        """
        st.markdown(qr_html, unsafe_allow_html=True)

    st.divider()


def build_tile_active(service: dict) -> str:
    """
    Construye el bloque HTML para una aplicación ACTIVA.
    Genera un enlace clickeable (etiqueta <a>).
    """
    html = f"""
    <a href="{service['url']}" target="_blank" class="metro-tile {service['css_class']}">
        <div>
            <div class="tile-icon">{service['icon']}</div>
            <div class="tile-title">{service['title']}</div>
        </div>
        <div class="tile-subtitle">{service['subtitle']}</div>
    </a>
    """
    return html


def build_tile_development(service: dict) -> str:
    """
    Construye el bloque HTML para una aplicación EN DESARROLLO.
    Genera un bloque estático no clickeable (etiqueta <div>) con advertencia.
    """
    html = f"""
    <div class="metro-tile {service['css_class']} disabled-tile">
        <div>
            <div class="tile-icon">{service['icon']}</div>
            <div class="tile-title">{service['title']}</div>
        </div>
        <div>
            <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 1.05em;">
                ⏳ Próximamente integrado...
            </div>
            <div class="tile-subtitle" style="margin-top: 4px;">{service['subtitle']}</div>
        </div>
    </div>
    """
    return html


def render_mosaico():
    """
    Itera sobre las bases de datos de aplicaciones y renderiza la grilla.
    Agrupa primero las activas y luego las que están en desarrollo.
    """
    grid_html = '<div class="metro-grid">\n'
    
    # Renderizar Módulos Operativos (Enlaces Activos)
    grid_html += "\n"
    for srv in ACTIVE_SERVICES:
        grid_html += build_tile_active(srv)
        
    # Renderizar Módulos en Desarrollo (Opacos)
    grid_html += "\n\n"
    for dev_srv in DEVELOPMENT_SERVICES:
        grid_html += build_tile_development(dev_srv)
        
    grid_html += '\n</div>'
    
    # Inyectar la grilla completa en la interfaz de Streamlit
    st.markdown(grid_html, unsafe_allow_html=True)


def render_footer():
    """
    Genera el pie de página del sistema.
    Incluye el texto legal y el logotipo de Innovación para la versión móvil.
    """
    st.write("")
    st.divider()
    
    # Mensaje de información
    st.caption("Seleccione un servicio para ingresar. Plataforma centralizada de la Ilustre Municipalidad de La Serena.")
    
    # Logo de Innovación (Solo visible en pantallas pequeñas mediante CSS)
    img_inno_mobile = f'<img src="{URL_LOGO_INNO}" class="logo-inno-mobile">'
    st.markdown(img_inno_mobile, unsafe_allow_html=True)


# =============================================================================
# BUCLE PRINCIPAL DE EJECUCIÓN (MAIN)
# =============================================================================
def main():
    """
    Punto de entrada principal de la aplicación.
    Orquesta la carga de estilos y componentes estructurales.
    """
    # 1. Configuración de página (debe ser el primer comando de Streamlit)
    st.set_page_config(
        page_title="La Serena SmartCity | Portal Central", 
        page_icon="🌐", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # 2. Cargar motor CSS
    load_enterprise_css()
    
    # 3. Construir Cabecera
    render_header()
    
    # 4. Construir Grilla de Aplicaciones
    render_mosaico()
    
    # 5. Construir Pie de Página
    render_footer()


# =============================================================================
# EJECUCIÓN DEL SCRIPT
# =============================================================================
if __name__ == "__main__":
    main()
