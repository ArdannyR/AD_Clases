import socket
import time

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(("localhost", 5000)) # Connect para conexion a servidor 

while True:
    mensaje_envi = input(str("\nIngresa un mensaje: "))
    cliente_socket.send(mensaje_envi.encode()) 

    if mensaje_envi == "3":
        time.sleep(1)
        break

    mensaje_reciv = cliente_socket.recv(1024) 
    print(f"El servidor dice: \n{mensaje_reciv.decode()}")


cliente_socket.close()

