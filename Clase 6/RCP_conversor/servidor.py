from xmlrpc.server import SimpleXMLRPCServer

# Funciones que llamaran el cliente
def C_a_F(temp):
    res_F = (temp * (9/5)) + 32
    return res_F

def F_a_C(temp):
    res_C = (temp - 32) / 1.8
    return res_C


# Aqui se crea el servidor y se define su direccion y puerto. 
servidor = SimpleXMLRPCServer(("localhost", 5000)) # 172.31.115.134 o localhost

# Aqui registramos la funcion que debe hacer referencia el cliente para llamar a la funcion en este servidor
servidor.register_function(C_a_F, "F") # Cuando el cliente llame a "sumar" aqui se activara sumar
servidor.register_function(F_a_C, "C") # No necesariamente debe tener el mismo nombre 

# Activar por siempre el servidor (para escuchar peticiones) (Ya no necesitas el while True para mantener activo)
print("Servidor esuchando...")
servidor.serve_forever() 
