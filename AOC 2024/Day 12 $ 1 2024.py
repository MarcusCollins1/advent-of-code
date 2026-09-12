from collections import deque, defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 12 2024.txt"
# FILE_NAME = "Day 12 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

def GetPerimeter(locations: set[tuple[int, int]]) -> int:
    perimeter: int = 0
    for location in locations:
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nextX, nextY = [location[i] + dir[i] for i in range(2)]
            if (nextX, nextY) not in locations: perimeter += 1
    return perimeter

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
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
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

print(sum([GetPerimeter(locations)*len(locations) for locations in regions.values()]))
