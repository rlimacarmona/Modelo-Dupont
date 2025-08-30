import streamlit as st
import pandas as pd

# Título de la app
st.title("Modelo Dupont - Análisis de Rentabilidad de Negocios")

# Subir archivo
uploaded_file = st.file_uploader("Carga tu base de datos (Excel o CSV)", type=["xlsx", "csv"])

if uploaded_file is not None:
    # Leer archivo
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Datos cargados")
    st.dataframe(df)

    # Se espera que el archivo tenga al menos estas columnas:
    # "Periodo", "Ventas Netas", "Utilidad Neta", "Activos Totales", "Capital Contable"
    
    # Agrupar por periodo
    periodos = df["Periodo"].unique()
    resultados = {}

    for periodo in periodos:
        data = df[df["Periodo"] == periodo]

        ventas = data["Ventas Netas"].sum()
        utilidad = data["Utilidad Neta"].sum()
        activos = data["Activos Totales"].sum()
        capital = data["Capital Contable"].sum()

        # Fórmulas Dupont
        margen = utilidad / ventas if ventas != 0 else 0
        rotacion = ventas / activos if activos != 0 else 0
        apalancamiento = activos / capital if capital != 0 else 0
        roe = margen * rotacion
        roa = rotacion * apalancamiento
        payback_capital = 1 / roe if roe != 0 else 0
        payback_activos = 1 / roa if roa != 0 else 0

        resultados[periodo] = {
            "Margen (%)": round(margen * 100, 1),
            "ROE (%)": round(roe * 100, 1),
            "ROA (%)": round(roa * 100, 1),
            "Rotación (veces)": round(rotacion, 1),
            "Apalancamiento (veces)": round(apalancamiento, 1),
            "Pay Back Capital (veces)": round(payback_capital, 1),
            "Pay Back Activos (veces)": round(payback_activos, 1),
        }

    # Convertir a DataFrame para mostrar como tabla de reporte
    reporte = pd.DataFrame(resultados)
    st.subheader("Reporte Financiero - Modelo Dupont")
    st.dataframe(reporte)

    # Descargar reporte en Excel
    st.download_button(
        label="Descargar reporte en Excel",
        data=reporte.to_excel("reporte_dupont.xlsx"),
        file_name="reporte_dupont.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
