# Instrucciones: 
# 1. Crea una función llamada validar_cliente que reciba dos argumentos: el nombre del cliente y el tiempo (en segundos) que tarda en validarse.
# 2. La función debe imprimir "Validando a [nombre]...", hacer una pausa usando time.sleep() por la cantidad de segundos indicada, y al final imprimir "[nombre] validado!".
# 3. En tu programa principal, crea e inicia 3 hilos distintos pasando diferentes nombres y tiempos (ej: Cliente A - 1s, Cliente B - 2s, Cliente C - 0.5s).

import threading
import time

def validar_cliente(nombre, tiempo):
    print(f"Validando el nombre: {nombre}")
    time.sleep(tiempo)
    print(f"{nombre} validado!")

hilo1 = threading.Thread(target=validar_cliente, args=("Ardanny", 0.4))
hilo2 = threading.Thread(target=validar_cliente, args=("Arda", 0.9))
hilo3 = threading.Thread(target=validar_cliente, args=("Esau", 0.3))

hilo1.start()  
hilo2.start()
hilo3.start()

