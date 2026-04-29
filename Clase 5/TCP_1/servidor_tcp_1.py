import socket
import threading

def manejar_cliente(conexion):
    while True:    
        # Conexion es el canal de comunicacion, esta si se apaga no importa. El que aborda todo es el socket 
        mensaje_reciv = conexion.recv(1024) # Aqui recives la respuesta en bytes
        print(f"El cliente dice: {mensaje_reciv.decode()}")
        
        if mensaje_reciv.decode() == "salir":
            print(f"Cliente desconectado")
            break

        mensaje_envi = "Hola soy el Arda servidor"
        conexion.send(mensaje_envi.encode()) # Aqui mandas tu mensaje en bytes (aqui ahora solo se usa recv y send sin el to)
    conexion.close() 


servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # STREAM es lo que usa TCP en lugar del datagram de UDP
servidor_socket.bind(("172.31.115.134", 5000)) # 172.31.115.134 o localhost
servidor_socket.listen() # Con esta funcion le decimos que el servidor esta listo para esuchar peticiones (entre parentesis puedes poner un int para definir el max de num de conexiones)
print("Esperando conexion...")

while True:
    conexion, direccion = servidor_socket.accept() # Con esta funcion se acepta la solicitud de conexion del cliente Handshake
    hilo = threading.Thread(target=manejar_cliente, args=(conexion,))
    hilo.start()

conexion.close() # Cierre de canal
servidor_socket.close() # Cierre de servidor

