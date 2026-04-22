# Crea una variable global llamada dinero_en_boveda que inicie en 0.
# Crea una función llamada hacer_deposito que reciba el nombre del hilo (ej: "Cajero 1").
# Dentro de la función, haz un bucle que se repita 5 veces. En cada ciclo, debe sumar 100 a la variable global dinero_en_boveda e imprimir "[Nombre Cajero] depositó 100. 
# Total en bóveda: [total]".
# La trampa: Debes usar la herramienta correcta de la librería threading para asegurar que si dos cajeros intentan depositar al mismo tiempo, 
# el contador no se rompa (imagina que es una puerta que solo deja pasar a uno a la vez).
# Ejecuta 2 o 3 hilos haciendo depósitos simultáneos.

import threading
import time

global dinero_en_boveda
global lock

dinero_en_boveda = 0
lock = threading.Lock()

def hacer_deposito(nombre):
    global dinero_en_boveda # pregunta para la IA, debes definir la variable global dentro de la función para modificarla, o no es necesario?
    global lock
    # with lock: aqui hace que solo acceda un hilo a la vez al for
    for n in range(5):
        # aqui todos los hilos pueden acceder al for, pero solo uno va a dar el print meintras los otros esperan su turno
        with lock: # Depende de donde vaya el lock, los hilos llegaran hasta ese punto
            dinero_en_boveda += 100
            print(f"{nombre} depositó 100. Total en bóveda: {dinero_en_boveda}")
            time.sleep(0.2)

hilo1 = threading.Thread(target=hacer_deposito, args=("Cajero 1",))
hilo2 = threading.Thread(target=hacer_deposito, args=("Cajero 2",))
hilo3 = threading.Thread(target=hacer_deposito, args=("Cajero 3",))

hilo1.start()
hilo2.start()
hilo3.start()