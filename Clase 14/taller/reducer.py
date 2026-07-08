import os
from collections import Counter

final_counts = Counter()

for file in os.listdir("splits"):
    if file.endswith(".out"):
        with open(f"splits/{file}", 'r') as f:
            for line in f:
                user, count = line.strip().split()
                final_counts[user] += int(count)

print("------------------------------------------") # carcateres para que se vea mas vistoso :D
print(" RESULTADO: Accesos fuera del horario")
print("------------------------------------------")
for user, count in final_counts.items():
    print(f"{user} {count}")
print("------------------------------------------")
