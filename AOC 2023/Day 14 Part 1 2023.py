FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 14 2023.txt"
# FILE_NAME = "Day 14 2023 alt.txt"
# FILE_NAME = "Day 14 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

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

grid = TiltNorth(data)

total = 0
for i, row in enumerate(grid):
    score = len(grid)-i
    total += score*row.count("O")
print(total)