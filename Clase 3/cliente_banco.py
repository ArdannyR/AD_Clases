import socket
import threading

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_socket.bind(("", 0))
direccion_servidor = ("localhost", 5000)

def escuchar_al_banco():
    while True:
        try:
            data, oaddres = cliente_socket.recvfrom(1024)
            print("\nBanco:", data.decode())
        except OSError:
            break

hilo = threading.Thread(target=escuchar_al_banco)
hilo.start()

print("Escribe 'inicio' para empezar o 'cierre' para salir.")

while True:
    respuesta = input("Mensaje: ")
    if respuesta == "cierre":
        cliente_socket.close()
        break
    cliente_socket.sendto(respuesta.encode(), direccion_servidor)