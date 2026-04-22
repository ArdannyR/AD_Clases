# Servidor: Escucha en el puerto 5050 dentro de un bucle infinito while True.
# Si un cliente le envía la palabra "vip", el servidor responde "Bienvenido al club".
# Si envía la palabra "cierre", el servidor le responde "Cerrando puertas", rompe el bucle con un break y cierra su propio socket (.close()).
# Si envía cualquier otra cosa, responde "Contraseña incorrecta".
# Cliente: En un bucle while True, usa un input() para pedir una contraseña. Envía la contraseña al servidor y escucha la respuesta.
# Si el cliente escribe "cierre", después de enviar el mensaje y escuchar el "Cerrando puertas", debe cerrar su propio socket y terminar el programa.

import socket

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(('localhost', 5000))

print("Servidor escuchando en el puerto 5000...")
while True:
    data, address = socket_servidor.recvfrom(1024)
    mensaje = data.decode()
    print(f"Recibí: '{mensaje}' de {address}")
    if mensaje == "vip":
        respuesta = "Bienvenido al club".encode()
        socket_servidor.sendto(respuesta, address)
    elif mensaje == "cierre":
        respuesta = "Cerrando puertas".encode()
        socket_servidor.sendto(respuesta, address)
        print("Cerrando servidor...")
        break
    else:
        respuesta = "Contraseña incorrecta".encode()
        socket_servidor.sendto(respuesta, address)

socket_servidor.close()