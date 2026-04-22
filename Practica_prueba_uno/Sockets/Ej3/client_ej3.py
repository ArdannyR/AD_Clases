# Servidor: Escucha en el puerto 5050 dentro de un bucle infinito while True.
# Si un cliente le envía la palabra "vip", el servidor responde "Bienvenido al club".
# Si envía la palabra "cierre", el servidor le responde "Cerrando puertas", rompe el bucle con un break y cierra su propio socket (.close()).
# Si envía cualquier otra cosa, responde "Contraseña incorrecta".
# Cliente: En un bucle while True, usa un input() para pedir una contraseña. Envía la contraseña al servidor y escucha la respuesta.
# Si el cliente escribe "cierre", después de enviar el mensaje y escuchar el "Cerrando puertas", debe cerrar su propio socket y terminar el programa.

import socket
import time

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion_servidor = ('localhost', 5000)

while True:
    contraseña = input("Ingrese la contraseña: ")
    socket_cliente.sendto(contraseña.encode(), direccion_servidor)

    data, address = socket_cliente.recvfrom(1024)
    respuesta = data.decode()
    print(f"Respuesta del servidor: {respuesta}")

    if contraseña == "cierre":
        print("Cerrando cliente...")
        break

time.sleep(2) 
socket_cliente.close()