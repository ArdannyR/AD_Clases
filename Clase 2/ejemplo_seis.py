import threading
import time 

contador = 0

def incrementar(hilo):
    global contador
    for i in range(3):
        temp = contador
        print(f"{hilo} lee: {temp}")
        time.sleep(0.2)
        temp += 1
        contador = temp            
        print(f"{hilo} escribe: {contador}")

h1 = threading.Thread(target=incrementar, args=("Hilo A ",))
h2 = threading.Thread(target=incrementar, args=("Hilo B ",))
h1.start()
h2.start()
h1.join()
h2.join()

print(f"Contador final: {contador}")