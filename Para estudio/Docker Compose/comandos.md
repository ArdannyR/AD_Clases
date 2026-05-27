# Comandos básicos de Docker para imágenes

---

# Descargar ("Instalar") una imagen pre-hecha de internet

```bash
docker pull <nombre_imagen>
```

## Explicación

Se conecta a Docker Hub (la tienda oficial de imágenes de Docker) y descarga la imagen a tu computadora.

## Ejemplo real

Si necesitas levantar rápidamente una base de datos PostgreSQL, puedes usar:

```bash
docker pull postgres
```

Esto descargará la imagen oficial de PostgreSQL sin necesidad de instalar PostgreSQL directamente en tu sistema operativo.

---

# Crear (Construir) tu propia imagen

```bash
docker build -t <nombre_imagen> .
```

## Explicación

Lee el archivo `Dockerfile` y empaqueta tu código fuente en una imagen nueva.

> El `.` al final es obligatorio porque le indica a Docker que debe buscar el `Dockerfile` en la carpeta actual.

## Ejemplo real

Si estás desarrollando un backend con FastAPI, podrías usar:

```bash
docker build -t backend_fastapi .
```

Esto creará una imagen personalizada llamada `backend_fastapi`.

---

# Ver las imágenes disponibles

```bash
docker images
```

## Explicación

Muestra una lista con todas las imágenes descargadas o construidas en tu computadora.

La lista incluye:

- Nombre de la imagen
- Versión (`tag`)
- ID de la imagen
- Fecha de creación
- Espacio ocupado

## Ejemplo de salida

```bash
REPOSITORY         TAG       IMAGE ID       CREATED         SIZE
backend_fastapi   latest    a1b2c3d4e5f6   2 minutes ago   320MB
postgres          latest    f6e5d4c3b2a1   5 days ago      380MB
```

---

# Borrar una imagen

```bash
docker rmi <id_imagen>
```

## Explicación

Elimina imágenes viejas o innecesarias para liberar espacio en el disco.

> Docker no permitirá borrar una imagen si existe un contenedor que dependa de ella, incluso si el contenedor está apagado.

## Ejemplo real

```bash
docker rmi a1b2c3d4e5f6
```

Esto eliminaría la imagen con ese ID.

---

# Consejo útil

Antes de borrar imágenes, puedes revisar qué contenedores existen usando:

```bash
docker ps -a
```

Así evitarás errores por dependencias activas.