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
servidor_socket.bind(("172.31.115.134", 5000))

clientes = {}
datos = []
datos_de_cliente = []

estado_clientes = {}

preguntas = [
    "Ingrese cedula: ",
    "Ingrese nombre: ",
    "Ingrese correo: ", 
    "Ingrese telefono: ",
    "Ingrese preferencial (si/no): "
]


def responder_cliente(mensaje, cliente_addr):

    if mensaje == "1":
        print(f"Nuevo usuario conectado: {cliente_addr}")

        for n in len(preguntas):
            servidor_socket.sendto(f"{preguntas[n]}".encode(), cliente_addr)
            respuesta_cliente = data.decode()
            datos.append(respuesta_cliente)

        datos_de_cliente.append(datos)
        clientes[cliente_addr] = datos_de_cliente
    
    elif mensaje == "2":
        bd_clientes = clientes
        servidor_socket.sendto(bd_clientes.encode(), cliente_addr)
    
    elif mensaje == "inicio":
        print(f"Cliente conectado en {cliente_addr} - Msg: {mensaje}")
        respuesta = "--- Menu --- \n 1. Registar Usuario\n 2. Consultar Usuario \n 3. Salir"
        servidor_socket.sendto(respuesta.encode(), cliente_addr)
        


print("Servidor esperando clientes...")
while True:
    data, cliente_addr = servidor_socket.recvfrom(1024)
    mensaje = data.decode().strip().lower()
    
    hilo = threading.Thread(target=responder_cliente, args=(mensaje, cliente_addr))
    hilo.start()






