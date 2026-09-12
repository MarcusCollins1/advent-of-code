from collections import defaultdict
from itertools import combinations
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 08 2024.txt"
# FILE_NAME = "Day 08 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

for y in range(len(data)):
    for x in range(len(data[0])):
        curr = data[y][x]
        if curr != ".": antennas[curr].append((x, y))

def IsAntiNode(antennas: defaultdict[str, list[tuple[int, int]]], x: int, y: int) -> bool:
    for locations in antennas.values():
        for l1, l2 in combinations(locations, 2):
            x1, y1 = l1[0] - x, l1[1] - y
            x2, y2 = l2[0] - x, l2[1] - y
            if (x1 * 2 == x2 and y1 * 2 == y2) or (x2 * 2 == x1 and y2 * 2 == y1): return True
    return False

print(sum([1 for y in range(len(data)) for x in range(len(data[0])) if IsAntiNode(antennas, x, y)]))