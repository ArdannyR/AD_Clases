# Cliente: Usa un input() para pedirle al usuario que ingrese un número. Envía ese número al servidor. Al recibir la respuesta, imprime: "El servidor calculó: [respuesta]".
# Servidor: Escucha en el puerto 4005. Al recibir el número (recuerda que llega como texto/bytes), conviértelo a entero (int()), multiplícalo por 2, y envía el resultado de 
#  vuelta al cliente (recuerda pasarlo a texto de nuevo antes de codificarlo).

import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.bind(('localhost', 0))  
direccion_servidor = ('localhost', 4000)

numero = input("Ingrese un número: ")
if numero.isdigit():
    numero_mensaje = str(numero) # Esto resulto ser opcional por el momento. mas en validacion si puede ser util.
    socket_cliente.sendto(numero.encode(), direccion_servidor)
    
    respuesta, address = socket_cliente.recvfrom(1024)
    print(f"El servidor calculó: {respuesta.decode()}")
else:
    print("Numero no valido")
    socket_cliente.close()

socket_cliente.close()