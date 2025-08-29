# Usa una imagen base de Python oficial
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto que usa Flask
EXPOSE 8080

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]