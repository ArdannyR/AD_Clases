# Docker Compose

## ¿Qué es?

Es una herramienta de Docker que permite definir y ejecutar aplicaciones complejas que requieren varios servicios (contenedores) trabajando al mismo tiempo. Todo se configura de manera centralizada en un único archivo con formato YAML.

---

## Ejemplo básico aplicado a la vida real

Imagina al director de una orquesta sinfónica. Si tienes 50 músicos (contenedores), sería un caos ir uno por uno diciéndoles qué partitura tocar y cuándo empezar. El director (Docker Compose) utiliza una partitura maestra (el archivo YAML) para levantar su batuta y hacer que todos los músicos comiencen a tocar al mismo tiempo, en armonía y comunicándose entre ellos.

---

# Parte práctica (Paso a paso desde 0)

## 1. Preparar la estructura del proyecto

Organiza carpetas separadas para cada servicio.

```text
mi_proyecto/
│
├── backend/
│   ├── app.py
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
└── docker-compose.yml
```

Cada servicio tendrá su propio código y su propio `Dockerfile`.

---

## 2. Crear la partitura maestra

En la raíz del proyecto crea el archivo:

```text
docker-compose.yml
```

---

## 3. Definir la versión y los servicios

Comienza definiendo la versión y la sección de servicios.

```yaml
version: '3'

services:
```

---

## 4. Configurar el backend

Define el primer servicio indicando dónde está su `Dockerfile` y qué puerto utilizará.

```yaml
version: '3'

services:
  mi_backend:
    build: ./backend
    ports:
      - "5000:5000"
```

---

## 5. Configurar el frontend

Haz lo mismo para el segundo servicio.

```yaml
version: '3'

services:
  mi_backend:
    build: ./backend
    ports:
      - "5000:5000"

  mi_frontend:
    build: ./frontend
    ports:
      - "3000:3000"
```

---

# Archivo completo `docker-compose.yml`

```yaml
version: '3'

services:
  mi_backend:
    build: ./backend
    ports:
      - "5000:5000"

  mi_frontend:
    build: ./frontend
    ports:
      - "3000:3000"
```

---

## 6. Ejecutar el entorno

Abre una terminal en la carpeta donde está el archivo `docker-compose.yml` y ejecuta los comandos correspondientes.

---

# Comandos útiles

## Levantar todos los servicios

```bash
docker-compose up
```

### Explicación

Lee el archivo YAML, construye las imágenes necesarias, crea una red interna y levanta todos los contenedores al mismo tiempo.

### Cuándo usarlo

Cuando quieres iniciar toda tu arquitectura de una sola vez.

---

## Levantar en segundo plano

```bash
docker-compose up -d
```

### Explicación

Hace exactamente lo mismo que el comando anterior, pero en modo desacoplado (`detached`), dejando libre la terminal.

### Cuándo usarlo

Cuando necesitas seguir utilizando esa misma ventana de terminal para ejecutar otros comandos.

---

## Reconstruir las imágenes

```bash
docker-compose build
```

### Explicación

Reconstruye las imágenes de los servicios definidos en el YAML sin iniciarlos.

### Cuándo usarlo

Cuando modificaste el código fuente de algún servicio y necesitas actualizar la imagen antes de volver a levantar el proyecto.

---

## Apagar y limpiar el entorno

```bash
docker-compose down
```

### Explicación

Detiene los contenedores y elimina tanto los contenedores como la red interna creada automáticamente.

### Cuándo usarlo

Cuando terminaste de trabajar o estudiar y deseas apagar completamente todo el entorno.

---

# Resultado esperado

Si todo funciona correctamente:

- El backend estará disponible en:

```text
http://localhost:5000
```

- El frontend estará disponible en:

```text
http://localhost:3000
```

Y ambos servicios podrán comunicarse entre sí dentro de la red creada por Docker Compose.