# Utiliza la imagen oficial de Python
FROM python:3.10

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt


# Copia todos los archivos del proyecto dentro del contenedor
COPY . .

# Abre automáticamente Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
