# seleccionar una imagen 
FROM python:latest

# copia el archivo del contenedor (archivo y luego ruta del contenedor)
COPY division.py .

# para ejecutar comandos 
RUN pip install flask

# indicar purto donde trabajar la aplicacion
EXPOSE 5004

# ejecutar la aplicacion
CMD ["python", "division.py"]