import socket
import time

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(("localhost", 5000)) # Connect para conexion a servidor 

while True:
    mensaje_envi = input(str("\nIngresa un mensaje: "))
    cliente_socket.send(mensaje_envi.encode()) 

    mensaje_reciv = cliente_socket.recv(1024) 
    print(f"\nEl servidor dice: \n{mensaje_reciv.decode()}")

    if mensaje_reciv.decode() == f"Cerrando tu conexion":
        time.sleep(2)
        break
        
cliente_socket.close()
print("\nConexión cerrada exitosamente.")


