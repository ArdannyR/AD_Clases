import socket
import threading
import time

# craer socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# asignar id y puerto
direccion_servidor = ("172.31.115.134", 5000)

def enviar_mensaje_a_serv(respuesta, cliente_socket, direccion_servidor):
    #enviar mensaje
    cliente_socket.sendto(respuesta.encode(), direccion_servidor)


while True:
    # enviar mensaje (cliente prmero envia)
    respuesta = str(input("Mensaje a enviar: "))
    if respuesta == "adios":
        cliente_socket.close()
        break
    else:
        hilo = threading.Thread(target=enviar_mensaje_a_serv, args=(respuesta, cliente_socket, direccion_servidor))
        hilo.start()
        data = cliente_socket.recvfrom(1024)
        # pasar mensaje a texto
        #mensaje = data.decode()
        print(f"Mensaje recivido de servidor: {data}")




