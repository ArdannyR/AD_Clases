import socket
import threading
import time

# crea el socet
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# asignar id y puerto
servidor_socket.bind(("172.31.115.134", 5000))
print("Esperando conexiones...")

def mensaje_a_clientes(data, origen_addr, ser_socket):
    # decoficar mensaje
    mensaje = data.decode()
    print(f"Mensaje recivido de cliente: {mensaje} \n Direccion de origen: {origen_addr}")
    # respuesta enviado a cliente
    respuesta = str(input("Mensaje a veniar a cliente: "))
    ser_socket.sendto(respuesta.encode(), origen_addr)

while True:
    # recibir mensaje de cliente
    data, oaddr = servidor_socket.recvfrom(1024)
    hilo = threading.Thread(target=mensaje_a_clientes, args=(data, oaddr, servidor_socket))
    hilo.start()




# bind() Suministra un puerto a una dirección a asociar con el socket
# socket() se usa para crear un socket y regresa un descriptor correspondiente a este socket.
# sendto() Permite que el cliente o servidor transmita mensajes usando un socket sin conexión (usando datagramas).
# recvfrom() lee datos desde un socket sin conexión
# close() Indica al sistema que el uso de un socket debe de ser finalizado.
# recvfrom() espera recibir un datagrama UDP, en base a tamaño máximo del mensaje en bytes
# decode() método que convierte el mensaje en bytes a texto.
# encode() método que convierte el mensaje en texto a bytes.
# socket.AF_INET: indica la familia de direcciones. AF_INET significa que se va a trabajar con direcciones IPv4
# socket.SOCK_DGRAM: Esto indica el tipo de socket. Socket de datagramas
