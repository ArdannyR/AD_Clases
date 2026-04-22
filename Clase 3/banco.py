import socket

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind(("localhost", 5000))
print("Esperando conexiones al banco...")

preguntas = [
    "Eres mayor de edad (si o no)?",
    "Tienes fuentes de ingresos (si o no)?",
    "Tienes titulo academico (si o no)?",
    "Posees una tarjeta de debito (si o no)?",
    "Posees una tarjeta de credito (si o no)?"
]

usuarios = {} 

while True:
    data, addr = servidor_socket.recvfrom(1024)
    mensaje = data.decode().strip().lower() # Strip y lower para ahorrarnos el formato de la respuestas

    if mensaje == "inicio":
        usuarios[addr] = 0
        print(f"Nuevo cliente conectado desde {addr}")
        respuesta = f"Saludos cliente!\n{preguntas[0]}"
        servidor_socket.sendto(respuesta.encode(), addr)

    elif mensaje == "cierre":
        usuarios.pop(addr, None) # El none esta para evitarme posibles errores. Lo puse solo de buena practica, no lo veria necesario para este caso
        servidor_socket.sendto("Sesion cerrada. Adios!".encode(), addr)

    elif addr in usuarios:
        usuarios[addr] += 1 
        indice = usuarios[addr] 
        
        if indice < len(preguntas) and mensaje == "si":
            respuesta = f"Perfecto, siguiente.\n{preguntas[indice]}"
            servidor_socket.sendto(respuesta.encode(), addr)
        elif indice < len(preguntas):
            respuesta = f"No cumples uno de los requisitos, siguiente.\n{preguntas[indice]}"
            servidor_socket.sendto(respuesta.encode(), addr)
        else:
            respuesta = "Perfecto, fin de las preguntas (ingrese 'cierre' para salir)"
            servidor_socket.sendto(respuesta.encode(), addr)
            
    else:
        servidor_socket.sendto("Por favor escriba 'inicio' para comenzar.".encode(), addr)