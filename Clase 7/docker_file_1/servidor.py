from flask import Flask

servidor = Flask(__name__)

@servidor.route("/")
def hola():
    return "Hola desde el Servidor"

if __name__ == "__main__":
    servidor.run(host="0.0.0.0", debug=True)