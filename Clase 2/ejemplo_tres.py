import threading

def tarea(nombre):
    print(f"Hola! {nombre}")

hilo = threading.Thread(target=tarea, args=("Ardanny",)) # Si es solo un argmento va con , (SI O SI)
hilo.start() 
