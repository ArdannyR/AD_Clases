# Docker

## ¿Qué es?

Es una plataforma que permite empaquetar tu código fuente, junto con todas sus librerías, dependencias y configuraciones, en una unidad portátil llamada **contenedor**. Esto garantiza que tu aplicación funcionará exactamente igual en tu laptop, en la computadora de un compañero o en un servidor de producción.

---

## Ejemplo básico aplicado a la vida real

Piensa en Docker como una fiambrera o tupper hermético con tu almuerzo. No importa a qué comedor, parque o cocina vayas (diferentes sistemas operativos o computadoras), la comida dentro del tupper tiene exactamente los mismos ingredientes y va a saber exactamente igual, porque ya viene pre-empaquetada y aislada del exterior.

---

# Parte práctica (Paso a paso desde 0)

## 1. Tener una aplicación

Crea un archivo sencillo, por ejemplo un servidor web en Flask llamado `app.py`.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola desde Docker"

app.run(host="0.0.0.0", port=5000)
```

---

## 2. Crear el archivo de instrucciones

En la misma carpeta, crea un archivo llamado exactamente:

```text
Dockerfile
```

> El archivo no lleva extensión.

---

## 3. Definir la imagen base

Usa una imagen de Python ya preparada.

```dockerfile
FROM python:latest
```

---

## 4. Copiar los archivos al contenedor

```dockerfile
COPY . /app
WORKDIR /app
```

Esto mueve tu proyecto dentro del contenedor y define la carpeta de trabajo.

---

## 5. Instalar dependencias

```dockerfile
RUN pip install flask
```

Instala Flask dentro del contenedor.

---

## 6. Exponer el puerto y arrancar la aplicación

```dockerfile
EXPOSE 5000

CMD ["python", "app.py"]
```

- `EXPOSE 5000` indica el puerto usado por la aplicación.
- `CMD` define el comando que se ejecutará al iniciar el contenedor.

---

# Dockerfile completo

```dockerfile
FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
```

---

# Comandos útiles

## Construir la imagen

```bash
docker build -t mi_aplicacion .
```

### Explicación

Lee el `Dockerfile` y construye la imagen empaquetada asignándole el nombre `mi_aplicacion`.

### Cuándo usarlo

Se usa una sola vez después de programar tu app, o cada vez que modifiques tu código y necesites actualizar el empaquetado.

---

## Ejecutar el contenedor

```bash
docker run -p 5000:5000 mi_aplicacion
```

### Explicación

Inicia un contenedor basado en tu imagen y conecta el puerto `5000` de tu computadora con el puerto `5000` del contenedor.

### Cuándo usarlo

Cuando ya tienes la imagen construida y deseas utilizar tu aplicación.

---

## Ver contenedores activos

```bash
docker ps
```

### Explicación

Muestra una lista de los contenedores que están ejecutándose actualmente junto con sus IDs.

### Cuándo usarlo

Para verificar si tu contenedor sigue funcionando o si se detuvo por algún error.

---

## Detener un contenedor

```bash
docker stop <id_contenedor>
```

### Explicación

Apaga un contenedor que se encuentra en ejecución.

### Cuándo usarlo

Cuando terminaste de hacer pruebas y quieres liberar recursos o puertos de tu computadora.

---

# Resultado esperado

Si todo funciona correctamente, al abrir:

```text
http://localhost:5000
```

Verás algo como:

```text
Hola desde Docker
```