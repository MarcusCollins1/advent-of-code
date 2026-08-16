from collections import deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 16 2024.txt"
# FILE_NAME = "Day 16 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

START = [(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "S"][0]
END = [(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "E"][0]

CLOCKWISE: dict[tuple[int, int], tuple[int, int]] = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
COUNTERCLOCKWISE: dict[tuple[int, int], tuple[int, int]] = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}

minScore = float("inf")
visited: dict[tuple[tuple[int, int], tuple[int, int]], int] = {(START, (1, 0)): 0}
queue: deque[tuple[int, tuple[int, int], tuple[int, int]]] = deque([(0, START, (1, 0))])
while queue:
    currScore, currLocation, currDirection = queue.popleft()
    if currScore > minScore: continue
    if currLocation == END:
        minScore = min(minScore, currScore)
        continue
    nextItems: list[tuple[int, tuple[int, int], tuple[int, int]]] = []
    # Forward
    nextItems.append((currScore + 1, (currLocation[0]+currDirection[0], currLocation[1]+currDirection[1]), currDirection))
    # Clockwise
    nextItems.append((currScore + 1000, currLocation, CLOCKWISE[currDirection]))
    # Counter-clockwise
    nextItems.append((currScore + 1000, currLocation, COUNTERCLOCKWISE[currDirection]))
    for nextScore, nextLocation, nextDirection in nextItems:
        if data[nextLocation[1]][nextLocation[0]] == "#": continue
        if (nextLocation, nextDirection) in visited and visited[(nextLocation, nextDirection)] <= nextScore: continue
        visited[(nextLocation, nextDirection)] = nextScore
        queue.append((nextScore, nextLocation, nextDirection))
print(minScore)