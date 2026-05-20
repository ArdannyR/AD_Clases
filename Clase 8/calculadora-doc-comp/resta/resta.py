from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/resta', methods=['POST'])

def resta():
    data = request.json
    a = data['a']
    b = data['b']

    resultado = a - b

    return jsonify({
        "operacion": "resta",
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)