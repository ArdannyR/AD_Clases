# El hilo principal debe imprimir primero: "Gerente: Solicitando auditorías..." 
# Crea una función auditoria_sucursal que reciba el numero_sucursal. Que imprima "Sucursal [numero] auditando...", espere 1 segundo, e imprima "Sucursal [numero] lista!".
# Lanza 4 hilos (Sucursal 1, 2, 3 y 4). Pista: Puedes usar un bucle for para crearlos y guardarlos en una lista para organizarte mejor.
# El programa principal DEBE esperar obligatoriamente a que todas las sucursales terminen.
# Solo cuando todas hayan terminado, el hilo principal debe imprimir: "Gerente: Todas las auditorías terminadas. Cierre del banco."

import threading
import time

def auditoria_sucursal(numero_sucursal):
    print(f"Sucursal {numero_sucursal} auditando...")
    time.sleep(1)
    print(f"Sucursal {numero_sucursal} lista!")

print("Gerente: Solicitando auditorías...")

hilos_guardados = [] # guardar en una lista hace que todos los hilos se ejecuten al mismo tiempo

for i in range(1, 5):
    hilo = threading.Thread(target=auditoria_sucursal, args=(i,))
    hilos_guardados.append(hilo) 
    hilo.start() 

for h in hilos_guardados:
    h.join() # y por ende de esta forma hacemos que todos eso hilos se terminen para ir luego con el principal

print("Gerente: Todas las auditorías terminadas. Cierre del banco.")