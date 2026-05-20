# seleccionar una imagen 
FROM python:latest

# copia el archivo del contenedor (archivo y luego ruta del contenedor)
COPY calculadora.py .

# para ejecutar comandos 
RUN pip install flask
RUN pip install requests

# indicar purto donde trabajar la aplicacion
EXPOSE 5000

# ejecutar la aplicacion
CMD ["python", "calculadora.py"]