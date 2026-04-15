import threading

lock = threading.Lock()

def impresora(num_hilo):
    with lock:
        print(f"Hilo {num_hilo} esta imprimiendo su conjunto de numeros: ")
        for n in range(5):
            print(f"Hilo {num_hilo} numero: {n}")
        print(f"Hilo {num_hilo} ha finalizado\n")

for h in range(1,12):
    hilo = threading.Thread(target=impresora, args=(h,))
    hilo.start()
    hilo.join()