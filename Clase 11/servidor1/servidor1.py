from flask import Flask

servidor1 = Flask(__name__)

@servidor1.route('/')
def hola():
    return "Hola desde servidor 1"

if __name__ == '__main__':
    servidor1.run(host='0.0.0.0')