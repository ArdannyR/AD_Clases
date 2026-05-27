# Servidor XML-RPC Dockerizado

---

# 1. Estructura del Proyecto

Primero, crea una carpeta limpia para el proyecto, por ejemplo:

```text
/Servidor_XML_Docker
├── servidor.py
├── Dockerfile
└── requirements.txt
```

## Descripción de cada archivo

- `servidor.py` → Contiene el código del servidor XML-RPC.
- `Dockerfile` → Define cómo construir el contenedor Docker.
- `requirements.txt` → Archivo opcional para dependencias externas.

---

# 2. El código del servidor (`servidor.py`)

Este servidor XML-RPC permite:

- Registrar usuarios
- Iniciar sesión
- Guardar respuestas de encuestas

> El servidor escucha en `0.0.0.0` para permitir conexiones externas desde Docker.

---

## Archivo completo `servidor.py`

```python
from xmlrpc.server import SimpleXMLRPCServer

# Almacenamiento básico en memoria
usuarios = {}
respuestas = {}

def registrar(user, pwd):

    if user in usuarios:
        return False

    usuarios[user] = pwd

    return True

def login(user, pwd):

    return usuarios.get(user) == pwd

def guardar_encuesta(user, pregunta, respuesta):

    respuestas[user] = {
        "pregunta": pregunta,
        "respuesta": respuesta
    }

    return "Guardado exitosamente"

# IMPORTANTE:
# Escuchar en 0.0.0.0 permite conexiones externas al contenedor

servidor = SimpleXMLRPCServer(("0.0.0.0", 5000))

servidor.register_function(registrar, "registrar")
servidor.register_function(login, "login")
servidor.register_function(guardar_encuesta, "guardar_encuesta")

print("Servidor XML-RPC dockerizado escuchando en puerto 5000...")

servidor.serve_forever()
```

---

# 3. El Dockerfile

Este archivo define cómo Docker construirá el contenedor de tu aplicación.

---

## Archivo `Dockerfile`

```dockerfile
# Usar imagen ligera de Python
FROM python:3.9-slim

# Definir directorio de trabajo
WORKDIR /app

# Copiar el script al contenedor
COPY servidor.py .

# Exponer el puerto del servidor
EXPOSE 5000

# Comando de ejecución
CMD ["python", "servidor.py"]
```

---

# 4. Guía de ejecución (Paso a paso)

---

## Construir la imagen Docker

Abre una terminal dentro de la carpeta `Servidor_XML_Docker` y ejecuta:

```bash
docker build -t mi_servidor_rpc_encuesta .
```

---

## Explicación

Este comando:

- Lee el `Dockerfile`
- Descarga la imagen de Python
- Copia el código
- Construye la imagen personalizada

---

# Ejecutar el contenedor

```bash
docker run -p 5000:5000 mi_servidor_rpc_encuesta
```

---

## Explicación

Este comando conecta:

```text
Puerto 5000 de tu computadora
            ↓
Puerto 5000 del contenedor
```

Gracias a esto, puedes acceder al servidor desde tu máquina local.

---

# Resultado esperado

En la terminal deberías ver:

```text
Servidor XML-RPC dockerizado escuchando en puerto 5000...
```

---

# 5. Probar el funcionamiento desde el cliente

Ahora puedes usar el mismo `cliente.py` utilizado anteriormente.

Como Docker expuso el puerto `5000`, el cliente podrá conectarse usando:

```python
proxy = ServerProxy("http://localhost:5000")
```

---

# Flujo de funcionamiento

```text
Cliente Python
       │
       ▼
localhost:5000
       │
       ▼
Docker Container
       │
       ▼
Servidor XML-RPC
```

---

# Comandos útiles adicionales

## Ver contenedores activos

```bash
docker ps
```

---

## Detener el contenedor

```bash
docker stop <id_contenedor>
```

---

## Ver imágenes Docker

```bash
docker images
```

---

# Ventajas de Dockerizar el servidor

- El servidor funciona igual en cualquier computadora.
- No necesitas instalar Python manualmente.
- El entorno queda completamente aislado.
- Facilita despliegues y pruebas.
- Permite compartir el proyecto fácilmente.