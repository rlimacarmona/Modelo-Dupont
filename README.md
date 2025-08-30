# 📊 Modelo Dupont - Análisis de Rentabilidad de Negocios

Este proyecto implementa un modelo **Dupont** en **Python con Streamlit**, que permite analizar la rentabilidad de negocios cargando bases de datos en formato Excel o CSV.

## 🚀 Funcionalidades

- Cargar archivos Excel o CSV con información financiera.
- Calcular automáticamente los siguientes indicadores:
  - **Margen Neto (%)**
  - **ROE (%)**
  - **ROA (%)**
  - **Rotación (veces)**
  - **Apalancamiento (veces)**
  - **Pay Back Capital (veces)**
  - **Pay Back Activos (veces)**
- Generar un reporte con periodos en columnas y conceptos en filas.
- Descargar el reporte en Excel.

## 📂 Estructura del Proyecto

```
├── modelo_dupont.py   # Código principal en Streamlit
├── README.md          # Instrucciones de uso
```

## 📦 Instalación

Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/modelo-dupont.git
cd modelo-dupont
```

Crea un entorno virtual e instala dependencias:

```bash
python -m venv venv
source venv/bin/activate   # En Mac/Linux
venv\Scripts\activate    # En Windows

pip install -r requirements.txt
```

## 📋 Dependencias

Las principales librerías necesarias son:

- streamlit
- pandas
- openpyxl (para archivos Excel)

Puedes instalarlas con:

```bash
pip install streamlit pandas openpyxl
```

## ▶️ Uso

Ejecuta la aplicación con:

```bash
streamlit run modelo_dupont.py
```

Esto abrirá automáticamente la aplicación en tu navegador.

## ☁️ Despliegue en Streamlit Cloud

1. Sube este repositorio a tu cuenta de GitHub.
2. Ve a [Streamlit Cloud](https://share.streamlit.io/).
3. Conecta tu repositorio y selecciona `modelo_dupont.py` como archivo principal.
4. La app quedará disponible con un link público.

---
✍️ Autor: *Tu nombre aquí*
