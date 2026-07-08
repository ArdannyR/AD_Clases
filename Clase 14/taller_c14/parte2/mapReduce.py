import os
import sys
from collections import Counter

def map_function(file_path):
    # Fase Map: Lee el archivo y genera un mapa local de palabras y frecuencias
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = f.read().lower().split()
        # Eliminar puntuaciones básicas para un conteo más limpio
        cleaned_words = [w.strip('.,!?;:"()[]{}') for w in words]
        # Filtrar palabras vacías si resultaran de la limpieza
        cleaned_words = [w for w in cleaned_words if w]
        return Counter(cleaned_words)
    except Exception as e:
        print(f"Error en mapeo de {file_path}: {e}")
        return Counter()

def reduce_function(counters):
    # Fase Reduce: Agrega los contadores individuales en un contador consolidado
    total_counts = Counter()
    for counter in counters:
        total_counts.update(counter)
    return total_counts

if __name__ == "__main__":
    folder_path = "textos"
    if not os.path.exists(folder_path):
        print(f"Error: La carpeta '{folder_path}' no existe.")
        sys.exit(1)

    # Listar los archivos txt en la carpeta textos
    archivos = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    print(f"Procesando {len(archivos)} archivos en la fase Map...")
    
    # Fase Map
    datos_mapeados = [map_function(archivo) for archivo in archivos]
    
    print("Consolidando resultados en la fase Reduce...")
    # Fase Reduce
    resultado_final = reduce_function(datos_mapeados)
    
    print("\n-------------------------------------------")
    print(" RESULTADO DEL CONTEO DE PALABRAS (MAPREDUCE)")
    print("-------------------------------------------")
    for palabra, cantidad in resultado_final.most_common():
        print(f"{palabra}: {cantidad}")
    print("-------------------------------------------")
