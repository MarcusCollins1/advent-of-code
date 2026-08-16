FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 06 2024.txt"
# FILE_NAME = "Day 06 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

DIRECTIONS = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
positions: set[tuple[int, int]] = set()

currDir = (0, -1)
currX, currY = [(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "^"][0]
while True:
    positions.add((currX, currY))
    nextX = currX + currDir[0]
    nextY = currY + currDir[1]
    if not ((0 <= nextX < len(data[0])) and (0 <= nextY < len(data))):
        break
    if data[nextY][nextX] == "#":
        currDir = DIRECTIONS[currDir]
        continue
    currX = nextX
    currY = nextY

print(len(positions))