from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 05 2025.txt"
# FILE_NAME = "Day 05 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
ranges, ids = file.read().split("\n\n")
file.close()

ranges = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in ranges.splitlines()]
ids = [int(id) for id in ids.splitlines()]

def isFresh(ranges: list[tuple[int, int]], id: int) -> bool:
    for lower, upper in ranges:
        if lower <= id <= upper: return True
    return False

print(sum([1 for id in ids if isFresh(ranges, id)]))

print(f"Time Taken: {time()-t1:.3f}s")