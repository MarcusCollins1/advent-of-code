from time import time
t1 = time()
from math import prod
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 12 2025.txt"
# FILE_NAME = "Day 12 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.read().split("\n\n")]
file.close()

presents: list[int] = [line.count("#") for line in data[:-1]]

count = 0

for line in data[-1].splitlines():
    size, idxs = line.split(": ")
    idxs = [int(x) for x in idxs.split()]
    size = prod([int(x) for x in size.split("x")])
    for i, num in enumerate(idxs):
        size -= num*presents[i]
    if size >= 0: count+=1

print(count)

print(f"Time Taken: {time()-t1:.3f}s")