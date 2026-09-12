from collections import defaultdict
from itertools import combinations
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 08 2024.txt"
# FILE_NAME = "Day 08 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()
WIDTH, HEIGHT = len(data[0]), len(data)

antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

for y in range(len(data)):
    for x in range(len(data[0])):
        curr = data[y][x]
        if curr != ".": antennas[curr].append((x, y))

antiNodes: set[tuple[int, int]] = set()

for locations in antennas.values():
    for l1, l2 in combinations(locations, 2):
        dx, dy = l2[0] - l1[0], l2[1] - l1[1]
        currX, currY = l1
        # Forwards
        while 0 <= currX < WIDTH and 0 <= currY < HEIGHT:
            antiNodes.add((currX, currY))
            currX += dx
            currY += dy
        currX, currY = l1
        # Backwards
        while 0 <= currX < WIDTH and 0 <= currY < HEIGHT:
            antiNodes.add((currX, currY))
            currX -= dx
            currY -= dy
print(len(antiNodes))