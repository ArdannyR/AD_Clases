from xmlrpc.server import SimpleXMLRPCServer

# Almacenamiento básico en memoria
usuarios = {} 
respuestas = {}

def registrar(user, pwd):
    if user in usuarios: return False
    usuarios[user] = pwd
    return True

def login(user, pwd):
    return usuarios.get(user) == pwd

def guardar_encuesta(user, pregunta, respuesta):
    respuestas[user] = {"pregunta": pregunta, "respuesta": respuesta}
    return "Guardado exitosamente"

# IMPORTANTE: Escuchar en 0.0.0.0 permite conexiones externas al contenedor
servidor = SimpleXMLRPCServer(("0.0.0.0", 5000))
servidor.register_function(registrar, "registrar")
servidor.register_function(login, "login")
servidor.register_function(guardar_encuesta, "guardar_encuesta")

print("Servidor XML-RPC dockerizado escuchando en puerto 5000...")
servidor.serve_forever()