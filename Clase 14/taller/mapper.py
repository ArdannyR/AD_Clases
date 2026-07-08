import sys
from collections import Counter
from datetime import datetime

filename = sys.argv[1]
counts = Counter()

# Definición del horario laboral
hora_inicio = datetime.strptime("08:00:00", "%H:%M:%S").time()
hora_fin = datetime.strptime("18:00:00", "%H:%M:%S").time()

try:
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 4:
                hora_str = parts[1]
                usuario = parts[2]
                
                # Convertir el string de hora a un objeto time
                hora_acceso = datetime.strptime(hora_str, "%H:%M:%S").time()
                
                # Si el acceso fue antes de las 08:00 o después de las 18:00
                if hora_acceso < hora_inicio or hora_acceso > hora_fin:
                    counts[usuario] += 1

    # Guarda resultados en archivo .out
    with open(f"{filename}.out", 'w') as out:
        for user, count in counts.items():
            out.write(f"{user} {count}\n")
except FileNotFoundError:
    pass
