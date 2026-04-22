# Sistema de preguntas-respuestas UDP
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
# El servidor:
# • espera un mensaje de un cliente
# • identifica al cliente por su dirección (ip, puerto)
# • crea o actualiza su estado
# • envía la pregunta correspondiente
# • recibe la respuesta
# • valida
# • informa si es correcta o no
# • pasa a la siguiente hasta finalizar con las 5 preguntas.

import socket
import threading

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind(('localhost', 12345))

preguntas = [
    "Saludos usuario",
    "¿Tienes edad suficiente?",
    "¿Tienes una cuenta en el banco?", 
    "¿Tienes tarjeta de debito?",
    "¿Tienes tarjeta de credito?",
    "¿Tienes una fuente estable de ingresos?"
]

clientes = {} 
lock = threading.Lock() 

def procesar_mensaje(mensaje_texto, cliente_addr):
    with lock: 
        if mensaje_texto == "inicio":
            if cliente_addr not in clientes:
                clientes[cliente_addr] = 0 
                print(f"Nuevo usuario conectado: {cliente_addr}")
                pregunta_actual = preguntas[0]
                servidor_socket.sendto(f"{pregunta_actual}".encode(), cliente_addr)
            else:
                servidor_socket.sendto("Ya iniciaste el cuestionario.".encode(), cliente_addr)
        elif cliente_addr in clientes:
            clientes[cliente_addr] += 1
            indice = clientes[cliente_addr]

            if mensaje_texto == "si":
                feedback = "¡Correcto!"
            else:
                feedback = "¡Incorrecto!"

            if indice < len(preguntas):
                siguiente_pregunta = preguntas[indice]
                respuesta_final = f"{feedback} \nSiguiente pregunta: {siguiente_pregunta}"
                servidor_socket.sendto(respuesta_final.encode(), cliente_addr)
            else:
                servidor_socket.sendto(f"{feedback} Has terminado las 5 preguntas. Gracias por participar. ('salir')".encode(), cliente_addr)
                clientes.pop(cliente_addr)
        else:
            servidor_socket.sendto("Escribe 'inicio' para comenzar.".encode(), cliente_addr)

print("Servidor esperando clientes...")
while True:
    data, cliente_addr = servidor_socket.recvfrom(1024)
    mensaje = data.decode().strip().lower()
    
    hilo = threading.Thread(target=procesar_mensaje, args=(mensaje, cliente_addr))
    hilo.start()
