from time import time
startTime = time()
from collections import deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 20 2024.txt"
# FILE_NAME = "Day 20 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()
NEIGHBOURS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
startPosition = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "S"][0]
endPosition = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "E"][0]

def getNeighbours(position: tuple[int, int], data: list[list[str]]) -> list[tuple[int, int]]:
    x, y, = position
    return [(x + dx, y + dy) for dx, dy in NEIGHBOURS if (0 <= x + dx < len(data[0])) and (0 <= y + dy < len(data))]

def getCheatNeighbours(position: tuple[int, int], data: list[list[str]]) -> list[tuple[int, int]]:
    cheatNeighbours: list[tuple[int, int]] = []
    neighbours = getNeighbours(position, data)
    for neighbour in neighbours:
        if data[neighbour[1]][neighbour[0]] == "#":
            currNeighbours = getNeighbours(neighbour, data)
            cheatNeighbours += [(x, y) for x, y in currNeighbours if ((x, y) != position) and (data[y][x] != "#")]
    return cheatNeighbours

def getShortestPath(start, end, data) -> list[tuple[int, int]]:
    queue: deque[list[tuple[int, int]]] = deque([[start]])
    shortestPathLength = float("inf")
    shortestPath: list[tuple[int, int]] = []
    while queue:
        path = queue.popleft()
        currLocation = path[-1]
        if currLocation == end:
            if len(path) < shortestPathLength:
                shortestPathLength = len(path)
                shortestPath = path
        else:
            for neighbour in getNeighbours(currLocation, data):
                if neighbour not in path and data[neighbour[1]][neighbour[0]] != "#":
                    queue.append(path + [neighbour])
    return shortestPath

shortestPath = getShortestPath(startPosition, endPosition, data)

print("Found shortest path")

total = 0

for i, location in enumerate(shortestPath):
    cheatNeighbours = getCheatNeighbours(location, data)
    for neighbour in cheatNeighbours:
        i2 = shortestPath.index(neighbour)
        if (i2 - i) - 2 >= 100:
            total += 1
print(total)
print(f"Time taken: {time() - startTime:.3f}s")