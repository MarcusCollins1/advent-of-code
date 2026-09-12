from time import time
t1 = time()
from collections import defaultdict
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 07 2025.txt"
# FILE_NAME = "Day 07 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

splitters: set[tuple[int, int]] = {(row, col) for col in range(len(data[0])) for row in range(len(data)) if data[row][col] == "^"}
timelines: defaultdict[int, int] = defaultdict(int)
timelines[data[0].index("S")] += 1

for rowIdx in range(1, len(data)):
    newTimelines: defaultdict[int, int] = defaultdict(int)
    for beamIdx, num in timelines.items():
        if (rowIdx, beamIdx) in splitters:
            newTimelines[beamIdx-1] += num
            newTimelines[beamIdx+1] += num
        else:
            newTimelines[beamIdx] += num
    timelines = newTimelines

print(sum(timelines.values()))

print(f"Time Taken: {time()-t1:.3f}s")