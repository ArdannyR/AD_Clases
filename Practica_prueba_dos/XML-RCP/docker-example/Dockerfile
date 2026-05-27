# Usar imagen ligera de Python
FROM python:3.9-slim

# Definir directorio de trabajo
WORKDIR /app

# Copiar el script
COPY servidor.py .

# Exponer el puerto
EXPOSE 5000

# Comando de ejecución
CMD ["python", "servidor.py"]