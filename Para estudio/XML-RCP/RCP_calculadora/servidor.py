from xmlrpc.server import SimpleXMLRPCServer

# Funciones que llamaran el cliente
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# Aqui se crea el servidor y se define su direccion y puerto. 
servidor = SimpleXMLRPCServer(("localhost", 5000)) # 172.31.115.134 o localhost

# Aqui registramos la funcion que debe hacer referencia el cliente para llamar a la funcion en este servidor
servidor.register_function(sumar, "sumar") # Cuando el cliente llame a "sumar" aqui se activara sumar
servidor.register_function(restar, "restar") # No necesariamente debe tener el mismo nombre 
servidor.register_function(multiplicar, "multiplicar")
servidor.register_function(dividir, "dividir")

# Activar por siempre el servidor (para escuchar peticiones) (Ya no necesitas el while True para mantener activo)
print("Servidor esuchando...")
servidor.serve_forever() 
