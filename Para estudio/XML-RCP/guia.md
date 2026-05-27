# XML-RPC en Python

## ¿Qué es?

Es un protocolo de comunicación que permite a un programa (cliente) ejecutar funciones o métodos que están alojados en otra computadora (servidor) a través de una red. Utiliza el formato XML para empaquetar los datos de la petición y el protocolo HTTP para transportarlos.

---

## Ejemplo básico aplicado a la vida real

Imagina que estás en un restaurante. Tú (el cliente) no entras a la cocina a preparar tu comida; en su lugar, le das tu orden al mesero (la llamada remota). El mesero lleva la orden a la cocina (el servidor), el chef prepara el plato (ejecuta la función) y el mesero te trae tu comida lista (el resultado). Tú solo pediste el plato, sin importarte cómo se cocinó internamente.

---

# Parte práctica (Paso a paso desde 0)

## 1. Crear el archivo del servidor (`servidor.py`)

Importas `SimpleXMLRPCServer` desde la librería nativa `xmlrpc.server`.

```python
from xmlrpc.server import SimpleXMLRPCServer
```

---

## 2. Definir la función

Creas una función normal en Python.

```python
def calcular_descuento(precio):
    return precio * 0.90
```

---

## 3. Configurar y registrar el servidor

Instancias el servidor definiendo IP y puerto, y luego registras la función.

```python
from xmlrpc.server import SimpleXMLRPCServer

def calcular_descuento(precio):
    return precio * 0.90

servidor = SimpleXMLRPCServer(("localhost", 5000))

servidor.register_function(calcular_descuento)

print("Servidor escuchando en el puerto 5000...")
```

---

## 4. Encender el servidor

Añades `serve_forever()` para que el servidor permanezca escuchando solicitudes.

```python
servidor.serve_forever()
```

---

# Código completo del servidor

```python
from xmlrpc.server import SimpleXMLRPCServer

def calcular_descuento(precio):
    return precio * 0.90

servidor = SimpleXMLRPCServer(("localhost", 5000))

servidor.register_function(calcular_descuento)

print("Servidor escuchando en el puerto 5000...")

servidor.serve_forever()
```

---

# Crear el archivo del cliente (`cliente.py`)

## 1. Importar `ServerProxy`

```python
from xmlrpc.client import ServerProxy
```

---

## 2. Conectar y llamar la función

Creas la conexión utilizando la URL del servidor y llamas a la función como si fuera local.

```python
from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:5000")

resultado = proxy.calcular_descuento(100)

print("Precio con descuento:", resultado)
```

---

# Comandos útiles

## Ejecutar el servidor

```bash
python servidor.py
```

### Explicación

Inicia el servidor de escucha.

### Cuándo usarlo

Es el primer comando que debes ejecutar. Si el servidor no está encendido, el cliente mostrará un error de conexión rechazada.

---

## Ejecutar el cliente

```bash
python cliente.py
```

### Explicación

Ejecuta el script del cliente para consumir la función remota.

### Cuándo usarlo

Se ejecuta en una terminal completamente nueva, únicamente después de que el servidor ya esté mostrando que está escuchando.

---

# Resultado esperado

```bash
Precio con descuento: 90.0
```