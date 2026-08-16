from time import time
t1 = time()
from collections import deque
from itertools import permutations
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 24 2016.txt"
# FILE_NAME = "Day 24 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

ROWS = len(data)
COLS = len(data[0])

points = {int(data[row][col]): (row, col) for row in range(ROWS) for col in range(COLS) if data[row][col].isdigit()}

start = points[0]
targets = sorted(n for n in points if n != 0)

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(start):
    """Return shortest distance from start to every numbered point."""
    queue = deque([(start, 0)])
    visited = {start}
    distances = {}

    while queue:
        (row, col), steps = queue.popleft()
        cell: str = data[row][col]
        if cell.isdigit(): distances[int(cell)] = steps

        for dr, dc in DIRECTIONS:
            nr = row + dr
            nc = col + dc

            if not (0 <= nr < ROWS and 0 <= nc < COLS): continue

            if data[nr][nc] == "#": continue

            pos = (nr, nc)
            if pos in visited: continue

            visited.add(pos)
            queue.append((pos, steps+1))
    return distances

distances = {
    number: bfs(position)
    for number, position in points.items()
}

best = float("inf")

for order in permutations(targets):
    distance = 0
    current = 0

    for target in order:
        distance += distances[current][target]
        current = target
        if distance >= best: break
    distance += distances[current][0]
    best = min(best, distance)

print(best)

print(f"Time Taken: {time()-t1:.2f}s")