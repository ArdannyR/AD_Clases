import xmlrpc.client

# Crea el proxy que apunta a la dirección del servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:5000")

# Llama a la función remota "sumar"
resultado = proxy.sumar(10, 5)

print(f"El resultado de la suma remota es: {resultado}")