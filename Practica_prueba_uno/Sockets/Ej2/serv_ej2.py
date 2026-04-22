# Cliente: Usa un input() para pedirle al usuario que ingrese un número. Envía ese número al servidor. Al recibir la respuesta, imprime: "El servidor calculó: [respuesta]".
# Servidor: Escucha en el puerto 4005. Al recibir el número (recuerda que llega como texto/bytes), conviértelo a entero (int()), multiplícalo por 2, y envía el resultado de 
#  vuelta al cliente (recuerda pasarlo a texto de nuevo antes de codificarlo).

import socket

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(('localhost', 4000))

print("Servidor escuchando...")
while True:
    data, addr = socket_servidor.recvfrom(1024)
    print(f"Recibí el número: {data.decode()} de {addr}")

    numero = int(data.decode())
    resultado = numero * 2

    respuesta = str(resultado).encode()
    socket_servidor.sendto(respuesta, addr)
    print(f"Envié el resultado: {resultado} a {addr}")

