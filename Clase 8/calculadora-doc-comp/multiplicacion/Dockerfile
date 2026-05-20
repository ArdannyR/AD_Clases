# seleccionar una imagen 
FROM python:latest

# copia el archivo del contenedor (archivo y luego ruta del contenedor)
COPY multiplicacion.py .

# para ejecutar comandos 
RUN pip install flask

# indicar purto donde trabajar la aplicacion
EXPOSE 5003

# ejecutar la aplicacion
CMD ["python", "multiplicacion.py"]