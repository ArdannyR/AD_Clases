# Implementar un sistema cliente-servidor en Python usando UDP donde:
# • el servidor maneja un banco de 5 preguntas 
# • cada cliente recibe una pregunta a la vez 
# • el cliente responde 
# • el servidor valida la respuesta 
# • el servidor envía si es correcta o incorrecta 
# • luego envía la siguiente pregunta 
# • al terminar las 5 preguntas, finaliza la sesión del cliente 
# • el servidor usa hilos para atender múltiples clientes 
# Lógica general
# El cliente:
# • envía un mensaje inicial al servidor
# • recibe una pregunta
# • envía la respuesta
# • recibe retroalimentación
# • repite hasta terminar
# • cierra su socket

import socket
import time
import threading

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_socket.bind(("localhost",0))
direccion_servidor = ("localhost", 5000)

def responder_servidor(mensaje, direccion_servidor):
    cliente_socket.sendto(mensaje.encode(), direccion_servidor)
    respuesta, addres = cliente_socket.recvfrom(1024)
    print(respuesta.decode())


while True:
    time.sleep(1)
    mensaje = input("Mensaje: ")
    if mensaje != "cierre":
        hilo = threading.Thread(target=responder_servidor, args=(mensaje,direccion_servidor))
        hilo.start()
    else:
        print("Cerrando secion")
        cliente_socket.sendto(mensaje.encode(), direccion_servidor)
        time.sleep(1)
        cliente_socket.close()
        break

    

