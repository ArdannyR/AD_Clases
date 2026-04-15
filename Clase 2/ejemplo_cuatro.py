import threading

def tarea_uno(hilo):
    for a in range(5):
        print(f"{hilo}: A{a}")
    
def tarea_dos(hilo):
    for b in range(5):
        print(f"{hilo}: B{b}")

h1 = threading.Thread(target=tarea_uno, args=("Hilo A",))
h2 = threading.Thread(target=tarea_dos, args=("Hilo B",))
h1.start()
h2.start()

for p in range(5):
        print(f"Hilo Principal: P{p}")