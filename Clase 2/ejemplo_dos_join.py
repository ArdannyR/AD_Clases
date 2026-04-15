import threading

def tarea_uno():
    for a in range(5):
        print(f"Hilo A: A{a}")
    
def tarea_dos():
    for b in range(5):
        print(f"Hilo B: B{b}")

h1 = threading.Thread(target=tarea_uno)
h2 = threading.Thread(target=tarea_dos)
h1.start()
h2.start()

for p in range(5):
        print(f"Hilo Principal: P{p}")

h1.join()
h2.join() # Join permite que una tarea 
print("Fin principal")