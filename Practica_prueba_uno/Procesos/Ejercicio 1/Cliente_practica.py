# Configura un cliente UDP y define la dirección del servidor (localhost, 6000).
# Crea una función llamada transmitir_telemetria que se ejecute en un hilo secundario.
# Esta función debe tener un bucle while True que envíe constantemente (ej: "Sector Norte") al servidor, haga una pausa de 3 segundos usando time.sleep(3), 
# y repita el proceso.
# En el hilo principal (fuera de la función de transmisión), configura un bucle while True que se dedique exclusivamente a escuchar usando .recvfrom().
# Imprime en pantalla la confirmación que llega del Centro de Control.
# Opcional: Si decides enviar un comando especial desde el servidor como "Apagar", el cliente principal debería romper el bucle y cerrar el socket.

import socket
import time
import threading

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.bind(('localhost', 0)) 
direccion_servidor = ('localhost', 6000)

def transmitir_telemetria(mensaje):
    socket_cliente.sendto(mensaje.encode(), direccion_servidor)
    data, addr = socket_cliente.recvfrom(1024)
    print(f"Confirmación del Servidor: {data.decode()}")
    # time.sleep(1) #Porque aqui no agarra el sleep? 

while True:
    time.sleep(1.5)
    mensaje = input("Ingrese su ubicación (o 'apagar' para salir): ")
    if mensaje.strip().lower() != "apagar":
        hilo = threading.Thread(target=transmitir_telemetria, args=(mensaje,))
        hilo.start()
    else:
        print("Apagando el cliente...")
        time.sleep(3)
        socket_cliente.close()
        print("Cliente cerrado.")
        break
    





