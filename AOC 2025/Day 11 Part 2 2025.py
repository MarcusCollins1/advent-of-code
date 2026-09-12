from time import time
t1 = time()
from collections import deque
from functools import lru_cache
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 11 2025.txt"
# FILE_NAME = "Day 11 2025 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


connections: dict[str, list[str]] = {line.split(": ")[0]: line.split(": ")[1].split() for line in data}

start = "svr"
target = "out"

@lru_cache(maxsize=None)
def dfs(node, seenDAC, seenFFT):
    if node == "dac": seenDAC = True
    if node == "fft": seenFFT = True

    if node == target:
        return 1 if (seenDAC and seenFFT) else 0
    
    total = 0
    for nxt in connections[node]:
        total += dfs(nxt, seenDAC, seenFFT)
    return total

print(dfs(start, False, False))

print(f"Time Taken: {time()-t1:.3f}s")