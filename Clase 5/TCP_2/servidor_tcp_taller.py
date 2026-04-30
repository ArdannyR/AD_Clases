import socket
import threading
import time

estado = {} # dir de cliente y estado
usuarios = {} # cedula y datos{}

menu_inicial = "-- Menu -- \n1. Registrar usuario \n2. Consultar usuario \n3. Salir"
menu_recarga = "-- Menu -- \n1. Recargar tarjeta \n2. Regresar "
peticion_de_datos = "Envie sus datos separados por coma \n(cédula, correo, teléfono, nombre y preferencial (true o false). El saldo se ira en 0)"
 
def manejar_cliente(conexion, direccion):
    print(f"Cliente conectado: {direccion[0]}")
    while True:    
        mensaje_reciv = conexion.recv(1024)
        print(f"El cliente dice: {mensaje_reciv.decode()}")
        
        # Sin estado solo puede ver menu
        if direccion not in estado:
            estado[direccion] = 0
            mensaje_envi = menu_inicial
            conexion.send(mensaje_envi.encode())
        
        # En estado 0 puede pedir/dar datos
        elif mensaje_reciv.decode() == "1" and estado[direccion] == 0:
            estado[direccion] = 1
            mensaje_envi = peticion_de_datos
            conexion.send(mensaje_envi.encode()) 

        # En estado 1 puede almacenar datos
        elif "," in mensaje_reciv.decode() and estado[direccion] == 1:
            estado[direccion] = 0
            lista_datos_usuario = mensaje_reciv.decode().split(',') # Esta linea me ayudo la IA
            if len(lista_datos_usuario) == 5:
                if "@" in lista_datos_usuario[1] and (lista_datos_usuario[4].lower() == "true" or lista_datos_usuario[4].lower() == "false"):
                    if lista_datos_usuario[4].lower() == "true":
                        lista_datos_usuario[4] = True
                    else:
                        lista_datos_usuario[4] = False

                    usuarios[lista_datos_usuario[0]] = { # Esta linea me ayudo la IA
                        "cedula": lista_datos_usuario[0],
                        "correo": lista_datos_usuario[1],
                        "telefono": lista_datos_usuario[2],
                        "nombre": lista_datos_usuario[3],
                        "preferencial": lista_datos_usuario[4],
                        "saldo": 0
                    }
                    mensaje_envi = f"Datos guardados\n{menu_inicial}"
                    conexion.send(mensaje_envi.encode())
                else: 
                    mensaje_envi = f"Datos erroneos\n{menu_inicial}"
                    conexion.send(mensaje_envi.encode())
            else: 
                mensaje_envi = f"Datos incompletos\n{menu_inicial}"
                conexion.send(mensaje_envi.encode())
            

        # En estado 0 puede mandar a buscar por cedula
        elif mensaje_reciv.decode() == "2" and estado[direccion] == 0:
            estado[direccion] = 2
            mensaje_envi = f"Ingresa la cedula del usuario a buscar"
            conexion.send(mensaje_envi.encode())
        
        # En estado 2 puede ver el resultado de la busqueda
        elif estado[direccion] == 2:
            if mensaje_reciv.decode().strip() in usuarios:
                estado[direccion] = 3
                cedula_activa = mensaje_reciv.decode().strip()
                mensaje_envi = f"Usuario encontrado \n{usuarios[mensaje_reciv.decode().strip()]}\n\n {menu_recarga}"
                conexion.send(mensaje_envi.encode())
            else:
                estado[direccion] = 0
                mensaje_envi = f"Usuario no encontrado\n{menu_inicial}"
                conexion.send(mensaje_envi.encode())
        
        # En estado 3 puede ingresar un saldo o regresar al menu inicial
        elif estado[direccion] == 3:
            if mensaje_reciv.decode() == "1":
                estado[direccion] = 4
                mensaje_envi = f"Ingresa el saldo a recargar"
                conexion.send(mensaje_envi.encode())
            else:
                estado[direccion] = 0
                conexion.send(menu_inicial.encode())
        
        # En estado 4 puede registrar un saldo
        elif estado[direccion] == 4:
            saldo_valor = mensaje_reciv.decode()
            if saldo_valor.isdigit(): # Esta linea me ayudo la IA
                usuarios[cedula_activa]["saldo"] = mensaje_reciv.decode()
                estado[direccion] = 0
                mensaje_envi = f"Saldo registrado\n{usuarios[cedula_activa]["saldo"]}\n{menu_inicial}"
                conexion.send(mensaje_envi.encode())
            else:
                mensaje_envi = f"Valor incorrecto"
                conexion.send(mensaje_envi.encode())

        # En estado 0 puede salir
        elif mensaje_reciv.decode() == "3" and estado[direccion] == 0:
            mensaje_envi = f"Cerrando tu conexion"
            conexion.send(mensaje_envi.encode())
            print(f"Cliente desconectado: {direccion[0]}")
            estado.pop(direccion) # Esta linea me ayudo la IA
            conexion.close() 
            break

        else:
            estado[direccion] = 0
            mensaje_envi = f"Error en datos\n{menu_inicial}"
            conexion.send(mensaje_envi.encode()) 



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
