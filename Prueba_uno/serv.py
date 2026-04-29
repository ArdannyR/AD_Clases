# Debe implementar un servidor que gestione la información de los usuarios.
#• Cada usuario debe tener los siguientes datos: cédula, correo, teléfono, nombre y
#preferencial (verdadero o falso) y saldo.
#• Los usuarios deben almacenarse en una lista de diccionarios.
#El servidor debe procesar solicitudes enviadas por el cliente:
#1. Registrar usuario
#2. Consultar usuario por cédula
#3. Recargar saldo

import socket
import threading

# 172.31.115.134 servidor
# 172.31.115.139 cliente 

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind(('172.31.115.134', 5000))

preguntas = [
    "Ingrese cedula: ",
    "Ingrese nombre: ",
    "Ingrese correo: ", 
    "Ingrese telefono: ",
    "Ingrese preferencial (si/no): "
]


clientes = {} 
lock = threading.Lock() 

def procesar_mensaje(mensaje_texto, cliente_addr):
    with lock: 
        if mensaje_texto == "inicio":
            respuesta = "--- Menu --- \n 1. Registar Usuario\n 2. Consultar Usuario \n 3. Salir"
            servidor_socket.sendto(respuesta.encode(), cliente_addr)
        elif cliente_addr not in clientes and mensaje_texto != "incio":
                clientes[cliente_addr] = 0 
                print(f"Nuevo usuario conectado: {cliente_addr}")
                pregunta_actual = preguntas[0]
                servidor_socket.sendto(f"{pregunta_actual}".encode(), cliente_addr)

        elif cliente_addr in clientes:
            clientes[cliente_addr] += 1
            indice = clientes[cliente_addr]

            if indice < len(preguntas):
                siguiente_pregunta = preguntas[indice]
                respuesta_final = f"{siguiente_pregunta}"
                servidor_socket.sendto(respuesta_final.encode(), cliente_addr)
            else:
                servidor_socket.sendto(f"Has terminado las 5 preguntas.".encode(), cliente_addr)
                clientes.pop(cliente_addr)
        else:
            servidor_socket.sendto("Escribe 'inicio' para comenzar.".encode(), cliente_addr)

print("Servidor esperando clientes...")
while True:
    data, cliente_addr = servidor_socket.recvfrom(1024)
    mensaje = data.decode().strip().lower()
    
    hilo = threading.Thread(target=procesar_mensaje, args=(mensaje, cliente_addr))
    hilo.start()
