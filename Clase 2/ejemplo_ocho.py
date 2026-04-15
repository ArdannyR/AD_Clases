import threading
import time

def tarea(cliente):
    print(f"Atendiendo al cliente {cliente}")
    time.sleep(0.2)
    print(f"Cliente {cliente} atendido")

hilos = []

for i in range(0, 5):
    h = threading.Thread(target=tarea, args=(i, ))
    hilos.append(h)
    h.start()

for i in hilos:
    i.join()

print("Fin")