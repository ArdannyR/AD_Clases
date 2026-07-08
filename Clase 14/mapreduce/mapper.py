import sys
import os
from collections import Counter

filename = sys.argv[1]
counts = Counter()

if os.path.exists(filename):
    with open(filename, 'r') as f:
        words = f.read().lower().split()
        counts = Counter(words)

# Guarda resultados en archivo .out
with open(f"{filename}.out", 'w') as out:
    for word, count in counts.items():
        out.write(f"{word} {count}\n")