from copy import deepcopy
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 14 2023.txt"
# FILE_NAME = "Day 14 2023 alt.txt"
# FILE_NAME = "Day 14 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

ROWS, COLS = len(data), len(data[0])

def TiltNorth(grid:list[list[str]]) -> list[list[str]]:
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "O":
                x = row_index
                while x > 0 and grid[x-1][col_index] == ".":
                    x -= 1
                grid[row_index][col_index] = "."
                grid[x][col_index] = "O"
    return grid

def TiltEast(grid:list[list[str]]) -> list[list[str]]:
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row[::-1]):
            col_index = (len(row)-1)-col_index
            if cell == "O":
                x = col_index
                while x < len(row)-1 and grid[row_index][x+1] == ".":
                    x += 1
                grid[row_index][col_index] = "."
                grid[row_index][x] = "O"
    return grid

def TiltSouth(grid:list[list[str]]) -> list[list[str]]:
    for row_index, row in enumerate(grid[::-1]):
        row_index = (len(grid)-1)-row_index
        for col_index, cell in enumerate(row):
            if cell == "O":
                x = row_index
                while x < len(grid)-1 and grid[x+1][col_index] == ".":
                    x += 1
                grid[row_index][col_index] = "."
                grid[x][col_index] = "O"
    return grid

def TiltWest(grid:list[list[str]]) -> list[list[str]]:
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "O":
                x = col_index
                while x > 0 and grid[row_index][x-1] == ".":
                    x -= 1
                grid[row_index][col_index] = "."
                grid[row_index][x] = "O"
    return grid

def Spin(grid:list[list[str]]) -> list[list[str]]:
    return TiltEast(TiltSouth(TiltWest(TiltNorth(grid))))

def Convert(grid:list[list[str]]) -> str:
    return "".join(["".join(x) for x in grid])
def Unconvert(grid:str) -> list[list[str]]:
    output = []
    x = 0
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(grid[x])
            x += 1
        output.append(row)
    return output

grid = deepcopy(data)
visited = []
while Convert(grid) not in visited:
    visited.append(Convert(grid))
    grid = Spin(grid)
x = visited.index(Convert(grid))

loop = visited[x:]

# print(loop)
# print(Convert(grid))

data = Unconvert(loop[(1000000000-x)%len(loop)])
# print(data)

total = 0
for i, row in enumerate(data):
    score = len(data)-i
    total += score*row.count("O")
print(total)