# Taller Semana 13 - Selecciones mundialistas con Docker

Aplicación Flask contenerizada que consulta `http://172.31.118.15:3000/selecciones`, normaliza la respuesta y guarda una copia local en SQLite. La interfaz permite agregar y actualizar selecciones.

## Ejecutar

```powershell
docker compose config
docker compose up --build
```

Abrir: `http://localhost:8080`

Comprobaciones:
- `http://localhost:8080/health`
- `http://localhost:8080/api/selecciones`

## Nota sobre el endpoint

La aplicación consume el endpoint con GET. Los cambios realizados desde la interfaz se guardan en la base local del contenedor mediante un volumen Docker; no modifican el servidor remoto porque no se ha proporcionado documentación de operaciones POST o PUT.

## Contingencia sin acceso al endpoint

Cambie `DEMO_MODE` a `"true"` en `compose.yaml` y reconstruya:

```powershell
docker compose down
docker compose up --build
```
