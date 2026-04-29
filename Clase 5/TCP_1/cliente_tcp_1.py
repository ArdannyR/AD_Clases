import socket
import time

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(("172.31.115.134", 5000)) # Connect para conexion a servidor 

while True:
    mensaje_envi = input(str("Ingresa un mensaje: "))
    cliente_socket.send(mensaje_envi.encode()) 

    if mensaje_envi == "salir":
        time.sleep(1)
        break

    mensaje_reciv = cliente_socket.recv(1024) 
    print(f"El servidor dice: {mensaje_reciv.decode()}")


cliente_socket.close()

