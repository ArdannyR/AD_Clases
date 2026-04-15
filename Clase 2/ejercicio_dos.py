import threading
import time

def descarga(archivo, peso):
    print(f"Descargando {archivo} {peso}...")
    time.sleep(0.5) # Tiempo de descarga
    print(f"Descarga completa: {archivo}")

h1 = threading.Thread(target=descarga, args=("archivo1.zip","(3MB)"))
h2 = threading.Thread(target=descarga, args=("archivo2.mp4","(7MB)"))
h3 = threading.Thread(target=descarga, args=("archivo3.pdf","(3MB)"))

h1.start()
h2.start()
h3.start()