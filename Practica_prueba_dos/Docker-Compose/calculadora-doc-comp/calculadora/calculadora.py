from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Fíjate cómo llama al contenedor "suma" por su nombre en la red interna
URL_SUMA = "http://suma:5001/suma"

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    operacion = data.get("operacion")
    a = data.get("a")
    b = data.get("b")

    if operacion == "suma":
        respuesta = requests.post(URL_SUMA, json={"a": a, "b": b})
        return jsonify(respuesta.json()), respuesta.status_code
    else:
        return jsonify({"error": "Operación no soportada aún"}), 400

if __name__ == "__main__":
    # La calculadora principal expone el puerto 5000 al exterior
    app.run(host="0.0.0.0", port=5000)

# el comando docker-compose up --build va desde la carpeta a nivel de docker-compose.yml
# en postman esto se prueba como http://localhost:5000/calcular 

# {
#     "operacion": "suma",
#     "a": 10,
#     "b": 5
# }
