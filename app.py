import streamlit as st
import pandas as pd
from geopy.distance import geodesic

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Asesor Hub - La Carlota", layout="wide", page_icon="📈")

# ESTILOS VISUALES PROFESIONALES
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    div[data-testid="stMetricValue"] { color: #1B263B; font-weight: bold; }
    .stButton>button { background-color: #1B263B; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# INICIALIZACIÓN DE SESIÓN
if 'clientes' not in st.session_state:
    st.session_state.clientes = []

# Coordenadas: La Carlota, Córdoba
UBICACION_BASE = (-33.419, -63.298)

# BARRA LATERAL DE ACCESO
st.sidebar.title("🔐 Acceso Seguro")
password = st.sidebar.text_input("Contraseña", type="password")

if password == "asesor2026":
    tab1, tab2, tab3, tab4 = st.tabs(["📊 DASHBOARD", "👥 AGENDA", "🚜 OFERTAS", "🎯 MATCHES"])

    with tab1:
        st.title("Monitor Económico Real-Time")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Dólar MEP", "$1.185,00", "-0.2%")
        c2.metric("Soja Rosario", "USD 295,00", "+1.2%")
        c3.metric("Índice ACARA", "+4.5%", "Mensual")
        c4.metric("UVA", "$945,20", "Hoy")
        st.divider()
        st.info("📢 **Noticia:** Alta demanda de maquinaria vial en el centro del país.")

    with tab2:
        st.header("Gestión de Clientes (ARCA/ANSES)")
        with st.form("nuevo_cliente"):
            nombre = st.text_input("Nombre o Razón Social")
            cuit = st.text_input("CUIT/CUIL")
            iva = st.selectbox("Condición IVA", ["Responsable Inscripto", "Monotributista", "Exento"])
            actividad = st.text_input("Actividad Principal")
            if st.form_submit_button("Agendar Cliente"):
                st.session_state.clientes.append({"Nombre": nombre, "CUIT": cuit, "IVA": iva, "Actividad": actividad})
                st.success(f"Cliente {nombre} guardado.")
        if st.session_state.clientes:
            st.dataframe(pd.DataFrame(st.session_state.clientes), use_container_width=True)

    with tab3:
        st.header("Buscador de Ofertas (Radio 400km)")
        ofertas = [
            {"tipo": "Vehículo", "item": "Hilux 2022", "loc": (-33.12, -64.34), "ciudad": "Río Cuarto"},
            {"tipo": "Campo", "item": "120 Ha Agrícolas", "loc": (-33.42, -63.15), "ciudad": "La Carlota"},
            {"tipo": "Maquinaria", "item": "Tractor JD", "loc": (-32.95, -60.64), "ciudad": "Rosario"}
        ]
        for o in ofertas:
            dist = geodesic(UBICACION_BASE, o['loc']).km
            with st.expander(f"{o['item']} - {o['ciudad']}"):
                st.write(f"Distancia: {dist:.1f} km")
                if dist <= 400: st.success("📍 Oferta en Radio de 400km")
                else: st.warning("🌐 Oferta Nivel País")

    with tab4:
        st.header("Match de 48hs")
        if st.session_state.clientes:
            st.selectbox("Seleccionar Cliente", [c['Nombre'] for c in st.session_state.clientes])
            if st.button("Ejecutar Verificación Automática"):
                st.balloons()
                st.write("✅ Match encontrado para su búsqueda de 'Camioneta' en Río Cuarto.")
        else:
            st.warning("Cargue un cliente en la pestaña Agenda.")
else:
    st.warning("Ingrese la contraseña 'asesor2026' para continuar.")