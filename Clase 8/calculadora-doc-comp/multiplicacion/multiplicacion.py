from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiplicacion', methods=['POST'])

def multiplicacion():
    data = request.json
    a = data['a']
    b = data['b']

    resultado = a * b

    return jsonify({
        "operacion": "multiplicacion",
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)