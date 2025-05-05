# 📊 Telecom Data Analysis

## 📝 Descripción

Este proyecto analiza datos del sector de telecomunicaciones en **Argentina**, con foco en:

- 🧹 Limpieza y transformación de datos.  
- 📊 Análisis Exploratorio de Datos (EDA).  
- 📈 Creación de indicadores clave (KPI) y conclusiones estratégicas.  
- 📊 Desarrollo de un **panel interactivo en Power BI**.  

El objetivo principal es generar insights relevantes sobre el acceso a **Internet, telefonía fija/móvil, TV por suscripción** y otros servicios de telecomunicaciones.

---

## 📁 Estructura del Proyecto

telecom_data_analysis/
│
├── docker-compose.yml # Configuración de Docker

├── dockerfile # Instrucciones para construir la imagen Docker

├── README.md # Documentación del proyecto

├── requisitos.txt # Librerías necesarias

├── data/ # Datos originales y limpios
│ ├── Internet.xlsx
│ ├── Telefonia_movil.xlsx
│ └── ...

├── notebooks/ # Análisis exploratorio
│ └── eda.ipynb

├── guiones/ # Scripts para procesamiento de datos
│ ├── clean_data.py
│ └── analyze_data.py

└── dashboards/
└── powerbi.pbix # Archivo del panel de Power BI

## 🛠 Requerimientos

Para ejecutar este proyecto necesitas tener instalado:

- Docker  
- Python 3.10 o superior  
- Librerías de Python:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `openpyxl`
  - `jupyter`

Si no tienes Docker, puedes descargarlo desde [https://www.docker.com/](https://www.docker.com/).

---

## 🚀 Ejecución con Docker

Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/telecom_data_analysis.git
cd telecom_data_analysis
Construye y ejecuta el contenedor:

docker-compose up
Abre tu navegador y accede a:

arduino
http://localhost:8888
Ahí encontrarás el entorno Jupyter Notebook para explorar y ejecutar el análisis.

📂 Scripts y Notebooks
notebooks/eda.ipynb: Análisis exploratorio con gráficos y visualizaciones.

guiones/clean_data.py: Limpieza de datos (valores nulos, duplicados, etc.).

guiones/analyze_data.py: Cálculo de KPIs y análisis de resultados.

📈 Panel Interactivo
El archivo dashboards/powerbi.pbix contiene:

Visualizaciones sobre comportamiento de servicios de telecomunicaciones.

KPIs estratégicos como el aumento en el acceso a Internet por cada 100 hogares.

🎯 KPIs del Proyecto
Indicadores clave analizados:

Aumento del acceso a Internet por cada 100 hogares.

Fórmula:

KPI = ((Nuevo acceso - Acceso actual) / Acceso actual) * 100
Penetración de telefonía móvil por provincia.

Variación trimestral en accesos a TV por suscripción.

📥 Fuente de Datos
Los archivos .xlsx están ubicados en la carpeta data/ y provienen de fuentes oficiales del sector de telecomunicaciones en Argentina.

👤 Autor
Carlos Alfredo Sierra Alarcón
📧 alfredosierraalarcon@gmail.com
🔗 LinkedIn
🌐 GitHub
📱 +(34) 613 436 460

⚖️ Licencia
Este proyecto tiene fines educativos y no debe ser utilizado para la toma de decisiones reales en entornos productivos o comerciales.
