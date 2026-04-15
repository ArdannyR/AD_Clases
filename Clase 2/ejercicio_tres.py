import threading

lock = threading.Lock()

global contador  
contador = 0

def asignar_turno(cliente):
    for n in range(1,4):
        contador =+ 1
        print(f"Turno {contador} asignado")
        print(f"Cliente {cliente}: Recibi el turno {contador}\n")

for c in range(1,4):
    with lock:
        h = threading.Thread(target=asignar_turno, args=(f"Cliente {c}",))
        h.start()

