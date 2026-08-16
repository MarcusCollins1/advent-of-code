from collections import deque, defaultdict
from dataclasses import dataclass
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 12 2024.txt"
# FILE_NAME = "Day 12 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

@dataclass
class Corner:
    x: int = 0
    y: int = 0

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def GetSides(locations: set[tuple[int, int]]) -> int:
    corners = defaultdict(Corner)
    for x, y in locations:
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in locations:
                if dx == 0:
                    corners[(x - 0.5, y + dy / 2)].y += 1
                    corners[(x + 0.5, y + dy / 2)].y += 1
                else:
                    corners[(x + dx / 2, y - 0.5)].x += 1
                    corners[(x + dx / 2, y + 0.5)].x += 1
    return sum(min(counter.x, counter.y) for counter in corners.values())


regions: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)

visited: set[tuple[int, int]] = set()
queue: deque[tuple[int, tuple[int, int]]] = deque([(0, (0, 0))])
nextId: int = 1
nextStart: list[tuple[int, int]] = []
while True:
    while queue:
        regionId, currLocation = queue.popleft()
        regions[regionId].add(currLocation)
        visited.add(currLocation)
        for dir in DIRECTIONS:
            nextX, nextY = [currLocation[i] + dir[i] for i in range(2)]
            if not ((0 <= nextX < len(data[0])) and (0 <= nextY < len(data))): continue
            elif (nextX, nextY) in regions[regionId]: continue
            elif data[nextY][nextX] == data[currLocation[1]][currLocation[0]]:
                regions[regionId].add((nextX, nextY))
                queue.append((regionId, (nextX, nextY)))
            else:
                nextStart.append((nextX, nextY))

    if len(nextStart) == 0: break
    while len(nextStart) > 0:
        n = nextStart.pop()
        if n not in visited:
            queue = deque([(nextId, n)])
            nextId += 1
            break

print(sum([GetSides(locations)*len(locations) for locations in regions.values()]))
