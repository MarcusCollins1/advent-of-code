from time import time
t1 = time()
from collections import defaultdict
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 24 2017.txt"
# FILE_NAME = "Day 24 2017 test.txt"

with open(FOLDER_PATH + FILE_NAME, encoding="utf-8") as file:
    parts = [
        tuple(map(int, line.strip().split("/")))
        for line in file
        if line.strip()
    ]

byPort: dict[int, list[int]] = defaultdict(list)

for index, (a, b) in enumerate(parts):
    byPort[a].append(index)
    if a!= b: byPort[b].append(index)

def strongestBridge(port: int, used: int) -> int:
    bestStrength = 0

    for index in byPort[port]:
        if used & (1 << index): continue

        a, b = parts[index]

        nextPort = b if a == port else a

        strength = strongestBridge(nextPort, used | (1 << index))

        strength += a+b

        if strength > bestStrength:
            bestStrength = strength

    return bestStrength

strength = strongestBridge(0, 0)

print(strength)

print(f"Time Taken: {time()-t1:.2f}s")