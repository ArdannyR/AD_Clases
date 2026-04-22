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
cliente_socket.bind(('localhost', 0)) 
direccion_servidor = ('localhost', 12345)

def enviar_respuesta():
    while True:
        pregunta, _ = cliente_socket.recvfrom(1024)
        print("Servidor:", pregunta.decode())
        respuesta = input("Tu respuesta (si/no/salir): ")
        if respuesta.lower().strip() == 'salir':
            print("Saliendo del cuestionario.")
            time.sleep(1) 
            break
        else:
            cliente_socket.sendto(respuesta.encode(), direccion_servidor)



while True:
    mensaje_de_inicio = input("Escribe 'inicio' para comenzar el cuestionario o 'salir' para terminar: ")
    if mensaje_de_inicio.lower().strip() == 'inicio':
        cliente_socket.sendto(mensaje_de_inicio.encode(), direccion_servidor)
        hilo = threading.Thread(target=enviar_respuesta)
        hilo.start()
        break
    elif mensaje_de_inicio.lower().strip() == 'salir':
        print("Saliendo sistema.")
        time.sleep(2) 
        cliente_socket.close()
        break
    else:
        print("Opción no válida. Por favor, escribe 'inicio' o 'salir'.")