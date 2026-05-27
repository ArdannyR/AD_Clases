# Proyecto de Microservicios con Docker Compose

---

# Paso 1: Crear la estructura de carpetas

Docker Compose necesita que todo esté bien organizado. Debes crear una carpeta principal para tu proyecto y, dentro de ella, una subcarpeta para cada microservicio.

La estructura debe quedar así:

```text
/calculadora-doc-comp
│── docker-compose.yml
│
├── calculadora/
│   ├── calculadora.py
│   └── Dockerfile
│
├── suma/
│   ├── suma.py
│   └── Dockerfile
│
├── resta/
│   ├── resta.py
│   └── Dockerfile
│
├── multiplicacion/
│   ├── multiplicacion.py
│   └── Dockerfile
│
└── division/
    ├── division.py
    └── Dockerfile
```

---

# Paso 2: Programar los microservicios y sus Dockerfiles

Dentro de cada subcarpeta debes crear el código que ejecutará la operación matemática y su respectivo `Dockerfile`.

---

## Ejemplo del microservicio de suma

### Archivo `suma/suma.py`

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/suma", methods=["POST"])
def sumar():
    data = request.json
    a = data.get("a", 0)
    b = data.get("b", 0)

    return jsonify({
        "resultado": a + b
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
```

---

## Archivo `suma/Dockerfile`

```dockerfile
FROM python:latest

COPY suma.py .

RUN pip install flask requests

EXPOSE 5001

CMD ["python", "suma.py"]
```

> Debes repetir este mismo proceso para:
>
> - `resta`
> - `multiplicacion`
> - `division`
>
> Cambiando nombres y puertos:
>
> - `5002`
> - `5003`
> - `5004`

---

# Paso 3: Programar el API Gateway (La calculadora principal)

En la carpeta `calculadora/` crearás el archivo principal `calculadora.py`.

La ventaja de Docker Compose es que los contenedores pueden comunicarse entre sí usando sus nombres como si fueran direcciones web internas.

Por eso las URLs no usan `localhost`, sino el nombre del servicio:

```python
SERVICIOS = {
    "suma": "http://suma:5001/suma",
    "resta": "http://resta:5002/resta"
}
```

---

## Archivo `calculadora/calculadora.py`

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

URL_SUMA = "http://suma:5001/suma"

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json

    operacion = data.get("operacion")
    a = data.get("a")
    b = data.get("b")

    if operacion == "suma":

        respuesta = requests.post(
            URL_SUMA,
            json={
                "a": a,
                "b": b
            }
        )

        return jsonify(respuesta.json()), respuesta.status_code

    return jsonify({
        "error": "Operación no soportada aún"
    }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Archivo `calculadora/Dockerfile`

```dockerfile
FROM python:latest

COPY calculadora.py .

RUN pip install flask requests

EXPOSE 5000

CMD ["python", "calculadora.py"]
```

---

# Paso 4: Crear la partitura maestra (`docker-compose.yml`)

En la raíz del proyecto crea el archivo:

```text
docker-compose.yml
```

---

## Archivo completo `docker-compose.yml`

```yaml
version: '3.8'

services:

  calculadora:
    build:
      context: ./calculadora
      dockerfile: Dockerfile

    container_name: calculadora_principal

    ports:
      - "5000:5000"

    depends_on:
      - suma

    networks:
      - red_calculadora

  suma:
    build:
      context: ./suma
      dockerfile: Dockerfile

    container_name: servicio_suma

    networks:
      - red_calculadora

networks:
  red_calculadora:
    driver: bridge
```

---

# Paso 5: Levantar toda la arquitectura

Abre una terminal dentro de la carpeta principal del proyecto y ejecuta:

```bash
docker-compose up --build
```

---

## ¿Qué hace este comando?

La bandera `--build` le indica a Docker que:

1. Entre a cada carpeta.
2. Lea cada `Dockerfile`.
3. Construya las imágenes necesarias.
4. Cree la red interna `red_calculadora`.
5. Inicie todos los contenedores en el orden correcto.

---

# Paso 6: Probar el funcionamiento

Una vez que los contenedores estén ejecutándose, abre otra terminal y realiza una petición usando `curl`.

```bash
curl -X POST http://localhost:5000/calcular \
-H "Content-Type: application/json" \
-d '{"operacion":"suma","a":10,"b":5}'
```

---

# Resultado esperado

```json
{
  "resultado": 15
}
```

La petición ingresará por el puerto `5000`, será procesada por la calculadora principal y luego reenviada internamente al microservicio `suma` usando la red creada por Docker Compose.

---

# Crear rápidamente las carpetas desde terminal

Si ya estás dentro de la carpeta del proyecto, puedes crear todas las subcarpetas ejecutando:

```bash
mkdir calculadora suma resta multiplicacion division
```

---

# Flujo completo del proyecto

```text
Cliente/Postman/curl
        │
        ▼
Calculadora Principal (Puerto 5000)
        │
        ▼
Red Interna Docker Compose
        │
        ▼
Microservicio de Suma (Puerto 5001)
```