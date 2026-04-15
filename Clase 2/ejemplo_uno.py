import threading
import time

# Usar hilos hace que el flujo de ejecucion sea simultanea y no secuencial
def tarea(): 
    print("Hola, soy un hilo :D")
    time.sleep(3)
    print("Fin de hilo")

hilo = threading.Thread(target=tarea) # Aqui defines que a que tarea esta dirigido el hilo y su nombre para llamarlo
hilo.start() # Con esto ejecutas el hilo
print("Hilo secundario")