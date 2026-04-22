# Configura un servidor UDP escuchando en el puerto 6000 (en localhost).
# Crea un diccionario global vacío llamado registro_rastreadores y un threading.Lock() para protegerlo.
# En un bucle infinito, el servidor debe escuchar los mensajes entrantes (las ubicaciones de los rastreadores).
# La magia de los hilos: Cada vez que reciba un mensaje usando .recvfrom(), el servidor NO debe procesarlo en el hilo principal. 
# Debe crear y arrancar un hilo secundario pasando el mensaje y la dirección (addr) a una función llamada actualizar_mapa.

# La función actualizar_mapa debe:
# Usar el with lock: para acceder de forma segura al diccionario global.
# Guardar o actualizar la información. Imagina que el mensaje decodificado es "Sector Norte"; debes guardarlo en el diccionario usando el addr como clave: 
# registro_rastreadores[addr] = mensaje.
# Imprimir en pantalla: "Centro de Control: Rastreador {addr} reportando en {mensaje}".
# Enviar una respuesta de confirmación al rastreador: "Coordenadas recibidas".

import socket
import threading

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(('localhost', 6000))

global registro_rastreadores
global lock

lock = threading.Lock()
registro_rastreadores = {} # diccioario addr:msg_ubicacion

def actualizar_mapa(mensaje, addr):
    with lock:
        registro_rastreadores[addr] = mensaje
    print(f"Centro de Control: Rastreador {addr} reportando en {mensaje}")
    socket_servidor.sendto("Coordenadas recibidas".encode(), addr)


print("Servidor esperando mensajes...")
while True:
    mensaje, addr = socket_servidor.recvfrom(1024)
    locacion = mensaje.decode()
    hilo = threading.Thread(target=actualizar_mapa, args=(locacion, addr))
    hilo.start()