from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/suma", methods=["POST"])
def sumar():
    data = request.json
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    # La suma corre en el puerto 5001
    app.run(host="0.0.0.0", port=5001)