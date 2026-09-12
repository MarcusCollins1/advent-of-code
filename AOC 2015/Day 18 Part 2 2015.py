FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 18 2015.txt"
# FILE_NAME = "Day 18 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

NUM_STEPS = 100
# NUM_STEPS = 5

def nextStateForCell(grid: list[list[int]], x: int, y: int) -> int:
    width, height = len(grid[0]), len(grid)
    if (x in [0, width-1]) and (y in [0, height-1]): return 1
    dirs = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    total = 0
    for dir in dirs:
        currX, currY = x+dir[0], y+dir[1]
        if (0 <= currX < width) and (0<= currY < height):
            total += grid[currY][currX]
    if grid[y][x] == 1:
        return 1 if total in [2, 3] else 0
    else:
        return 1 if total == 3 else 0

def nextState(grid: list[list[int]]) -> list[list[int]]:
    newGrid: list[list[int]] = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            newGrid[y][x] = nextStateForCell(grid, x, y)
    return newGrid

width, height = len(data[0]), len(data)
grid = [[1 if (cell == "#" or ((x==0 or x==width-1) and (y==0 or y==height-1))) else 0 for x, cell in enumerate(line)] for y, line in enumerate(data)]

for _ in range(NUM_STEPS):
    grid = nextState(grid)
    
print(sum(sum(line) for line in grid))