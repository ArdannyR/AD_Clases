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
servidor_socket.bind(("localhost", 5000))

preguntas = ["Como estas?" , "Como te llamas?" , "Tienes pareja?"]
clientes = {}

def hablar_cliente(mensage, addres):
    print(f"Cliente conectado - {addres}")
    if mensage != "cierre":
        if addres not in clientes:
            clientes[addres] = 0 
            servidor_socket.sendto("Bienvenido usuario".encode(), addres)
        elif addres in clientes and clientes[addres] < 3:
            iteacion = clientes[addres]
            pregunta = preguntas[iteacion]
            servidor_socket.sendto(pregunta.encode(), addres)
            clientes[addres] += 1
    else:
        clientes.pop(addres)
        servidor_socket.sendto("Usuario saliendo".encode(), addres)



print("Iniciando servidor...")
while True:
    msg, addr = servidor_socket.recvfrom(1024)
    mensage = msg.decode()

    hilo = threading.Thread(target=hablar_cliente, args=(mensage, addr))
    hilo.start()


