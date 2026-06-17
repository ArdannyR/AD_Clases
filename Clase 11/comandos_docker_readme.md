# Comandos Útiles de Docker y Docker Compose

## 1. Comandos de Docker Compose (Herramienta Principal)

### Levantar los servicios

```bash
docker-compose up -d
```

**¿Qué hace?**  
Levanta todos los servicios definidos en el archivo `docker-compose.yml` en segundo plano (*detached mode*).

**¿Cuándo usarlo?**  
Cuando las imágenes ya fueron construidas y solo necesitas iniciar el proyecto.

---

### Reconstruir y levantar los servicios ⭐

```bash
docker-compose up --build -d
```

**¿Qué hace?**  
Fuerza a Docker a reconstruir las imágenes antes de iniciar los contenedores.

**¿Cuándo usarlo?**  
Siempre que modifiques:

- Archivos Python (`app.py`)
- Archivos HTML
- `Dockerfile`
- Dependencias del proyecto

Si no utilizas `--build`, Docker podría ejecutar una versión antigua del código.

---

### Detener el proyecto

```bash
docker-compose down
```

**¿Qué hace?**  
Detiene y elimina los contenedores y la red creada por Docker Compose.

**¿Cuándo usarlo?**  
Cuando necesites apagar el proyecto de forma limpia.

---

### Eliminar contenedores y volúmenes ⭐

```bash
docker-compose down -v
```

**¿Qué hace?**  
Detiene los contenedores y elimina también los volúmenes asociados.

**¿Cuándo usarlo?**  
Si la replicación Maestro-Esclavo de MySQL presenta errores, problemas de sincronización o fallos relacionados con binlogs.

> **Advertencia:** Este comando elimina toda la información almacenada en la base de datos.

---

### Ver el estado de los contenedores

```bash
docker-compose ps
```

**¿Qué hace?**  
Muestra el estado actual de los contenedores (`Up`, `Exited`, etc.) y los puertos utilizados.

---

### Ver logs en tiempo real

```bash
docker-compose logs -f
```

**¿Qué hace?**  
Muestra los registros de todos los servicios en tiempo real.

**¿Cuándo usarlo?**  
Cuando la aplicación presenta errores o no responde correctamente.

Para ver únicamente los logs de un servicio específico:

```bash
docker-compose logs -f nodo1
```

---

## 2. Comandos para Interactuar con los Contenedores

### Acceder a la terminal de un contenedor

```bash
docker exec -it <nombre_del_contenedor> /bin/bash
```

o

```bash
docker exec -it <nombre_del_contenedor> /bin/sh
```

**¿Qué hace?**  
Abre una terminal dentro del contenedor en ejecución.

**¿Cuándo usarlo?**  

- Verificar archivos dentro del contenedor.
- Probar conectividad entre contenedores.
- Ejecutar comandos de diagnóstico.

---

### Acceder directamente a MySQL

```bash
docker exec -it <nombre_del_contenedor_mysql> mysql -uroot -proot
```

**¿Qué hace?**  
Abre la consola de MySQL dentro del contenedor.

**¿Cuándo usarlo?**  
Para ejecutar consultas SQL y comandos de replicación sin utilizar phpMyAdmin.

Ejemplos:

```sql
SHOW MASTER STATUS;
SHOW SLAVE STATUS;
```

---

### Listar contenedores en ejecución

```bash
docker ps
```

**¿Qué hace?**  
Muestra todos los contenedores actualmente activos.

---

### Listar todos los contenedores

```bash
docker ps -a
```

**¿Qué hace?**  
Muestra todos los contenedores, incluidos los detenidos o con errores.

**¿Cuándo usarlo?**  
Para localizar nombres o identificadores de contenedores.

---

## 3. Comandos de Limpieza y Recuperación

### Detener todos los contenedores

```bash
docker stop $(docker ps -aq)
```

**¿Qué hace?**  
Detiene todos los contenedores que se encuentran ejecutándose.

---

### Eliminar todos los contenedores

```bash
docker rm $(docker ps -aq)
```

**¿Qué hace?**  
Elimina todos los contenedores detenidos.

**Recomendación:**  
Ejecutar primero el comando `docker stop` y luego este.

---

### Limpieza completa del sistema Docker

```bash
docker system prune -a
```

**¿Qué hace?**

Elimina:

- Contenedores detenidos.
- Redes sin utilizar.
- Caché de compilación.
- Imágenes que no están siendo utilizadas.

**¿Cuándo usarlo?**

- Cuando Docker presenta errores inesperados.
- Cuando falta espacio en disco.
- Cuando se necesita reiniciar completamente el entorno.

> **Nota:** Después de ejecutar este comando, Docker deberá descargar nuevamente las imágenes necesarias durante la próxima compilación.