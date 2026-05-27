from xmlrpc.server import SimpleXMLRPCServer

# Define la función que el cliente podrá ejecutar remotamente
def sumar(a, b):
    return a + b

# Crea el servidor en localhost, puerto 5000
servidor = SimpleXMLRPCServer(("localhost", 5000))

# Registra la función para que sea accesible bajo el nombre "sumar"
servidor.register_function(sumar, "sumar")

print("Servidor escuchando en el puerto 5000...")
servidor.serve_forever() # Mantiene el servidor activo permanentemente