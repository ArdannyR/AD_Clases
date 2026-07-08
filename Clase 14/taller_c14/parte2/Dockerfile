FROM python:3.9-slim

WORKDIR /app

# Copiar el script principal
COPY mapReduce.py .

# Copiar la carpeta con los archivos de texto
COPY textos/ ./textos/

# Ejecutar el script por defecto al iniciar el contenedor
CMD ["python", "mapReduce.py"]
