import threading
import time

lock = threading.Lock()

def tarea(cliente):
    with lock:
        print(f"Atendiendo al cliente {cliente}")
        time.sleep(0.2)
        print(f"Cliente {cliente} atendido")

h1 = threading.Thread(target=tarea, args=(1,))
h2 = threading.Thread(target=tarea, args=(2,))
h3 = threading.Thread(target=tarea, args=(3,))
h4 = threading.Thread(target=tarea, args=(4,))
h1.start()
h2.start()
h3.start()
h4.start()

h1.join()
h2.join()
h3.join()
h4.join()

print("Fin")