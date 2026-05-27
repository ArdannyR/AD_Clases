from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICIOS = {
    "suma": "http://suma:5001/suma",
    "resta": "http://resta:5002/resta",
    "multiplicacion": "http://multiplicacion:5003/multiplicacion",
    "division": "http://division:5004/division"
}

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    operacion = data.get("operacion")
    a = data.get("a")
    b = data.get("b")

    if operacion not in SERVICIOS:
        return jsonify({
            "error": "Operación no válida"
        }), 400

    respuesta = requests.post(
        SERVICIOS[operacion],
        json={"a": a, "b": b}
    )

    return jsonify(respuesta.json()), respuesta.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)