from collections import defaultdict
from time import time
startTime = time()
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 06 2024.txt"
# FILE_NAME = "Day 06 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

DIRECTIONS = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
def IsLoop(map:list[list[str]]) -> bool:
    positions: defaultdict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set[tuple[int, int]])
    currDir = (0, -1)
    currX, currY = [(x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == "^"][0]

    while True:
        if currDir in positions[(currX, currY)]:
            return True
        positions[(currX, currY)].add(currDir)
        nextX = currX + currDir[0]
        nextY = currY + currDir[1]
        if not ((0 <= nextX < len(map[0])) and (0 <= nextY < len(map))):
            break
        if map[nextY][nextX] == "#":
            currDir = DIRECTIONS[currDir]
            continue
        currX = nextX
        currY = nextY
    return False

total = 0
for y in range(len(data)):
    currTime = time()
    currTotalTime = currTime - startTime
    print(f"On row {y+1} of {len(data)} | Found {total} locations so far | Taken {currTotalTime}s")
    for x in range(len(data[0])):
        if data[y][x] in ["^", "#"]: continue
        newData: list[list[str]] = []
        for _y in range(len(data)):
            newRow: list[str] = []
            for _x in range(len(data[0])):
                newRow.append("#" if (_x ==x and _y == y) else data[_y][_x])
            newData.append(newRow)
        if IsLoop(newData): total += 1
print(total)
endTime = time()
durationTime = endTime-startTime
print(f"Time took to run: {durationTime}s")