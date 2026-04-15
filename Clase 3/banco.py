import socket

# crea el socket
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# asignar id y puerto
servidor_socket.bind(("localhost", 5000))
print("Esperando conexiones al banco...")

def preguntar_al_cliente(data, origen_addr, ser_socket):
    for n in range(1, 6):
        match n:
            case 1:
                Pregunta = "Eres mayor de edad (si o no)? "
                ser_socket.sendto(Pregunta.encode(), origen_addr)
                data, origen_addr = ser_socket.recvfrom(1024)
                respuesta_cliente = data.decode().strip().lower()
                
                if respuesta_cliente == "si":
                    respuesta_servidor = "Perfecto siguiente"
                else:
                    respuesta_servidor = "Error siguiente"
                ser_socket.sendto(respuesta_servidor.encode(), origen_addr)
                
            case 2:
                Pregunta = "Tienes fuentes de ingresos (si o no)? "
                ser_socket.sendto(Pregunta.encode(), origen_addr)
                data, origen_addr = ser_socket.recvfrom(1024)
                respuesta_cliente = data.decode().strip().lower()
                
                if respuesta_cliente == "si":
                    respuesta_servidor = "Perfecto siguiente"
                else:
                    respuesta_servidor = "Error siguiente"
                ser_socket.sendto(respuesta_servidor.encode(), origen_addr)
                
            case 3:
                Pregunta = "Tienes titulo academico (si o no)? "
                ser_socket.sendto(Pregunta.encode(), origen_addr)
                data, origen_addr = ser_socket.recvfrom(1024)
                respuesta_cliente = data.decode().strip().lower()
                
                if respuesta_cliente == "si":
                    respuesta_servidor = "Perfecto siguiente"
                else:
                    respuesta_servidor = "Error siguiente"
                ser_socket.sendto(respuesta_servidor.encode(), origen_addr)
                
            case 4:
                Pregunta = "Posees una tarjeta de debito (si o no)? "
                ser_socket.sendto(Pregunta.encode(), origen_addr)
                data, origen_addr = ser_socket.recvfrom(1024)
                respuesta_cliente = data.decode().strip().lower()
                
                if respuesta_cliente == "si":
                    respuesta_servidor = "Perfecto siguiente"
                else:
                    respuesta_servidor = "Error siguiente"
                ser_socket.sendto(respuesta_servidor.encode(), origen_addr)
                
            case 5:
                Pregunta = "Posees una tarjeta de credito (si o no)? "
                ser_socket.sendto(Pregunta.encode(), origen_addr)
                data, origen_addr = ser_socket.recvfrom(1024)
                respuesta_cliente = data.decode().strip().lower()
                
                if respuesta_cliente == "si":
                    respuesta_servidor = "Perfecto fin de las preguntas (ingrese cierre para cerrar su sesion)"
                else:
                    respuesta_servidor = "Error fin de las preguntas (ingrese cierre para cerrar su sesion)"
                ser_socket.sendto(respuesta_servidor.encode(), origen_addr)

def iniciar_con_cliente(data, origen_addr, ser_socket):
    mensaje = data.decode().strip().lower()
    if mensaje == "inicio":
        print(f"Usuario ha declarado {mensaje}")
        respuesta = "Saludos cliente \nPor favor responda a las siguientes preguntas"
        ser_socket.sendto(respuesta.encode(), origen_addr)
        preguntar_al_cliente(data, origen_addr, ser_socket)
    else:
        respuesta = "Recuerde poner 'inicio' para seguir o 'cierre' para abandonar"
        ser_socket.sendto(respuesta.encode(), origen_addr)

while True:
    # recibir mensaje de cliente
    data, oaddr = servidor_socket.recvfrom(1024)
    iniciar_con_cliente(data, oaddr, servidor_socket)