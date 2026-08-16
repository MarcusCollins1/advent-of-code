from time import time
startTime = time()
from collections import deque, defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 20 2024.txt"
FILE_NAME = "Day 20 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

MAX_CHEAT_LENGTH = 20
NEIGHBOURS: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
startPosition = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "S"][0]
endPosition = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "E"][0]

def getNeighbours(position: tuple[int, int], data: list[list[str]], neighbours: list[tuple[int, int]]) -> list[tuple[int, int]]:
    x, y, = position
    return [(x + dx, y + dy) for dx, dy in neighbours if (0 <= x + dx < len(data[0])) and (0 <= y + dy < len(data)) and (data[y+dy][x+dx] != "#")]

def manhattanDistance(t1: tuple[int, int], t2: tuple[int, int]) -> int:
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

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
            for neighbour in getNeighbours(currLocation, data, NEIGHBOURS):
                if neighbour not in path:
                    queue.append(path + [neighbour])
    return shortestPath

shortestPath = getShortestPath(startPosition, endPosition, data)
shortestPathDict = {location:i for i, location in enumerate(shortestPath)}
print(shortestPath)
print(f"Found shortest path in {time()-startTime:.3f}s")

total = 0

shortcuts: defaultdict[int, int] = defaultdict(int)

for i, start in enumerate(shortestPath):
    for j, end in enumerate(shortestPath[i+1:]):
        manDist = manhattanDistance(start, end)
        if manDist > MAX_CHEAT_LENGTH: continue
        pathDist = j - i
        savings = pathDist - manDist
        shortcuts[savings] += 1
        if savings >= 100: total += 1

for key, val in sorted(shortcuts.items()):
    if key >= 50: print(f"{key}: {val}")

print(total)

print(f"Time taken: {time() - startTime:.3f}s")