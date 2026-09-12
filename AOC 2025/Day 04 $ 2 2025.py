from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 04 2025.txt"
# FILE_NAME = "Day 04 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()


def numAdjacentRolls(grid:list[list[str]], x: int, y: int) -> int:
    width, height = len(grid[0]), len(grid)
    count = 0
    for x1, y1 in [(x,y-1), (x+1,y-1), (x+1,y), (x+1,y+1), (x,y+1), (x-1,y+1), (x-1,y), (x-1,y-1)]:
        if (0 <= x1 < width) and (0 <= y1 < height):
            if grid[y1][x1] == "@": count += 1
    return count

def removableRolls(grid:list[list[str]]) -> list[tuple[int, int]]:
    removable: list[tuple[int, int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@" and numAdjacentRolls(grid, x, y) < 4: removable.append((x, y))
    return removable

def removeRolls(grid:list[list[str]]) -> tuple[list[list[str]], int]:
    removable = removableRolls(grid)
    for x,y in removable:
        grid[y][x] = "."
    return (grid, len(removable))

count = 0
while True:
    newData, numRemoved = removeRolls(data)
    count += numRemoved
    if numRemoved == 0: break
    data = newData

print(count)

print(f"Time Taken: {time()-t1:.3f}s")