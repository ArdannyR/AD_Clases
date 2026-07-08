import os
from collections import Counter
final_counts = Counter()
for file in os.listdir("splits"):
    if file.endswith(".out"):
        with open(f"splits/{file}", 'r') as f:
            for line in f:
                word, count = line.strip().split()
                final_counts[word] += int(count)
for word, count in final_counts.items():
    print(f"{word}: {count}")