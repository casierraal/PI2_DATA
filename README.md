📊 Telecom Data Analysis
📝 Descripción
Este proyecto analiza los datos del sector de telecomunicaciones en Argentina, enfocado en:

Limpieza de datos.
Análisis Exploratorio de Datos (EDA).
Creación de indicadores clave (KPIs) y generación de conclusiones.
Creación de un dashboard interactivo en Power BI.
El objetivo es brindar insights importantes sobre el acceso a Internet, telefonía fija/móvil, TV y otros servicios de telecomunicaciones.

📂 Estructura del proyecto
La estructura del proyecto es la siguiente:

plaintext
Copy code
telecom_data_analysis/
│
├── docker-compose.yml   # Configuración para ejecutar Docker
├── dockerfile           # Instrucciones de Docker
├── README.md            # Documentación del proyecto
├── requirements.txt     # Librerías necesarias
│
├── data/                # Datos originales y limpios
│   ├── Internet.xlsx
│   ├── Telefonia_movil.xlsx
│   ├── ...
│
├── notebooks/           # Notebooks para el EDA
│   ├── eda.ipynb        # Exploratory Data Analysis
│
├── scripts/             # Scripts Python para procesamiento
│   ├── clean_data.py    # Script para limpieza de datos
│   ├── analyze_data.py  # Script para análisis de KPIs
│
└── dashboards/          # Dashboards interactivos
    ├── powerbi.pbix     # Archivo del dashboard de Power BI
🛠 Requerimientos
Para ejecutar este proyecto, necesitas tener instalados:

Docker
Python 3.10 o superior
Librerías Python: pandas, numpy, matplotlib, openpyxl, jupyter
Si no tienes Docker instalado, puedes descargarlo aquí.

🚀 Cómo ejecutar el proyecto con Docker
Clona el repositorio:

bash
Copy code
git clone <URL-del-repositorio>
cd telecom_data_analysis
Construye y ejecuta el contenedor Docker:

bash
Copy code
docker-compose up
Abre el navegador y ve a:

text
Copy code
http://localhost:8888
Allí encontrarás el entorno Jupyter Notebook para explorar los datos.

📊 Scripts y Notebooks
notebooks/eda.ipynb:
Contiene el Análisis Exploratorio de Datos (EDA) con gráficos y visualizaciones.

scripts/clean_data.py:
Limpia los datos eliminando valores nulos y duplicados.

scripts/analyze_data.py:
Realiza cálculos de KPIs y otros análisis.

📈 Dashboards
El dashboard de Power BI se encuentra en la carpeta dashboards/. Contiene:

Visualizaciones interactivas del comportamiento de los servicios de telecomunicaciones.
Indicadores clave (KPIs), como el aumento en el acceso a Internet.
🎯 KPIs del Proyecto
Se analizaron y calcularon los siguientes KPIs:

Aumento del 2% en el acceso a Internet por cada 100 hogares:

Fórmula:
text
Copy code
KPI = ((Nuevo acceso - Acceso actual) / Acceso actual) * 100
KPIs adicionales:

(Ejemplo) Penetración de telefonía móvil por provincia.
(Ejemplo) Variación trimestral en accesos a TV por suscripción.
📥 Datos
Los datos utilizados en este proyecto provienen de archivos Excel ubicados en la carpeta data/.

🧑‍💻 Autor
Carlos Alfredo Sierra Alarcon


⚙️ Licencia
Este proyecto es de uso educativo y no debe utilizarse para toma de decisiones reales.

