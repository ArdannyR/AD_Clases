import socket
import threading
import time

estado = {} # dir de cliente y estado
usuarios = {} # dir cliente y datos

menu_inicial = "-- Menu -- \n1. Registrar usuario \n2. Consultar usuario \n3. Salir"
menu_recarga = "-- Menu -- \n1. Recargar tarjeta \n2. Regresar "
peticion_de_datos = "Envie sus datos separados por coma \n(cédula, correo, teléfono, nombre y preferencial (verdadero o falso) y saldo)"
 
def manejar_cliente(conexion, direccion):
    while True:    
        mensaje_reciv = conexion.recv(1024)
        print(f"El cliente dice: {mensaje_reciv.decode()}")
        
        if direccion not in estado:
            estado[direccion] = 0
            mensaje_envi = menu_inicial
            conexion.send(mensaje_envi.encode())
        
        elif mensaje_reciv.decode() == "1" and estado[direccion] == 0:
            estado[direccion] = 1
            mensaje_envi = peticion_de_datos
            conexion.send(mensaje_envi.encode()) 

        elif "," in mensaje_reciv.decode() and estado[direccion] == 1:
            estado[direccion] = 0
            lista_datos_usuario = mensaje_reciv.decode().split(',')
            usuarios[direccion] = lista_datos_usuario
            mensaje_envi = f"Usuario registrado\n{menu_inicial}"
            conexion.send(mensaje_envi.encode())

        elif mensaje_reciv.decode() == "2" and estado[direccion] == 0:
            estado[direccion] = 2
            mensaje_envi = f"Ingresa la cedula del usuario a buscar"
            conexion.send(mensaje_envi.encode())
        
        elif estado[direccion] == 2:
            if mensaje_reciv.decode() == usuarios[direccion][0]:
                estado[direccion] = 3
                mensaje_envi = f"Usuario encontrado \n{usuarios[direccion]}\n\n {menu_recarga}"
                conexion.send(mensaje_envi.encode())
            else:
                estado[direccion] = 0
                mensaje_envi = f"Usuario no encontrado\n{menu_inicial}"
                conexion.send(mensaje_envi.encode())

            
        elif mensaje_reciv.decode() == "3":
            print(f"Cliente desconectado")
            break

        else:
            mensaje_envi = "Error en datos"
            conexion.send(mensaje_envi.encode()) 

    conexion.close() 


servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind(("localhost", 5000))
servidor_socket.listen() 
print("Esperando conexion...")

while True:
    conexion, direccion = servidor_socket.accept()
    hilo = threading.Thread(target=manejar_cliente, args=(conexion,direccion))
    hilo.start()

conexion.close() 
servidor_socket.close() 
