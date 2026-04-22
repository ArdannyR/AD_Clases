# Servidor: Crea un servidor UDP que escuche en el puerto 4000 (usa "localhost"). Cuando reciba un mensaje, debe imprimir "Cliente dice: [mensaje]" y 
#  luego responderle a esa misma dirección con el mensaje: "Recibido fuerte y claro".
# Cliente: Crea un cliente UDP. Haz que envíe el mensaje "Hola servidor, ¿me escuchas?" al puerto 4000. Luego, debe esperar la respuesta del servidor e imprimirla.
# Pista: ¡No olvides usar .encode() al enviar y .decode() al recibir!

import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.bind(("localhost", 0))  # Elige un puerto aleatorio para el cliente?
address_servidor = ("localhost", 4000)

mensaje = "Hola servidor, ¿me escuchas?"
socket_cliente.sendto(mensaje.encode(), address_servidor)

data, address_servidor = socket_cliente.recvfrom(1024)
print(f"Servidor responde: {data.decode()}")

socket_cliente.close()