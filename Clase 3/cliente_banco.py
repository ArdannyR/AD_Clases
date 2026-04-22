import socket
import threading
import time

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_socket.bind(("", 0))
direccion_servidor = ("localhost", 5000)

def escuchar_al_banco():
    while True:
        try:
            data, oaddres = cliente_socket.recvfrom(1024)
            print("\nBanco:", data.decode())
        except: # Si el socket se cierra, se acita la exepcion y sale del bucle
            break

hilo = threading.Thread(target=escuchar_al_banco)
hilo.start()

print("Escribe 'inicio' para empezar o 'cierre' para salir.")

while True:
    respuesta = input(" ")
    cliente_socket.sendto(respuesta.encode(), direccion_servidor)
    if respuesta == "cierre":
        time.sleep(2) # Ardanny recuerda que el servidor debe de esuchar el adios
        cliente_socket.close()
        break