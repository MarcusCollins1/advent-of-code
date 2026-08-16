from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 05 2025.txt"
# FILE_NAME = "Day 05 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
ranges, ids = file.read().split("\n\n")
file.close()

ranges = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in ranges.splitlines()]
ranges.sort(key=lambda r: r[0])
ids = [int(id) for id in ids.splitlines()]

merged = []
for start, end in ranges:
    if not merged:
        merged.append([start, end])
    else:
        prevStart, prevEnd = merged[-1]
        if start <= prevEnd + 1:
            merged[-1][1] = max(prevEnd, end)
        else:
            merged.append([start, end])
numFresh = sum(e-s+1 for s, e in merged)

print(numFresh)

print(f"Time Taken: {time()-t1:.3f}s")