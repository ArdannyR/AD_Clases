FROM python:latest

# Copia el archivo de la aplicación y los requisitos al directorio de trabajo
COPY servidor1.py .

# Instala las dependencias necesarias
RUN pip install flask

EXPOSE 5000

# Define el comando por defecto para ejecutar la aplicación
CMD [ "python", "servidor1.py" ]