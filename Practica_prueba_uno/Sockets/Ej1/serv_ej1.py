# Servidor: Crea un servidor UDP que escuche en el puerto 4000 (usa "localhost"). Cuando reciba un mensaje, debe imprimir "Cliente dice: [mensaje]" y 
#  luego responderle a esa misma dirección con el mensaje: "Recibido fuerte y claro".
# Cliente: Crea un cliente UDP. Haz que envíe el mensaje "Hola servidor, ¿me escuchas?" al puerto 4000. Luego, debe esperar la respuesta del servidor e imprimirla.
# Pista: ¡No olvides usar .encode() al enviar y .decode() al recibir!

import socket

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(("localhost", 4000))

print("Servidor esperando mensajes...")
while True:
    data, address = socket_servidor.recvfrom(1024)
    print(f"Cliente dice: {data.decode()} desde {address}")

    respuesta = "Recibido fuerte y claro"
    socket_servidor.sendto(respuesta.encode(), address)

