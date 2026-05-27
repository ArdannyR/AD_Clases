from xmlrpc.server import SimpleXMLRPCServer

usuarios = {}  # {username: password}
respuestas = {} # {username: encuesta_data}

def registrar(user, pssword):
    if user in usuarios:
        return False
    usuarios[user] = pssword
    return True

def login(user, pssword):
    return usuarios.get(user) == pssword

def guardar_encuesta(user, pregunta, respuesta):
    respuestas[user] = {"pregunta": pregunta, "respuesta": respuesta}
    return "Encuesta guardada con éxito"

servidor = SimpleXMLRPCServer(("localhost", 5000))
servidor.register_function(registrar, "registrar")
servidor.register_function(login, "login")
servidor.register_function(guardar_encuesta, "guardar_encuesta")

print("Servidor listo...")
servidor.serve_forever()