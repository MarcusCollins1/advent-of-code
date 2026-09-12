FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 13 2023.txt"
# FILE_NAME = "Day 13 2023 alt.txt"
# FILE_NAME = "Day 13 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().split("\n\n")
file.close()

def Get_Difference(l1:list[str], l2:list[str]) -> list:
    output = []
    for x, y in zip(l1, l2):
        if x != y:
            output.append(x)
            output.append(y)
    return output

def Get_Column(col:int, grid:list[list[str]]) -> list:
    return [line[col] for line in grid]

def Check_Vertical(col:int, grid:list[list[str]]) -> bool:
    c1, c2 = col, col+1
    smudges = 0
    while c1 >= 0 and c2 < len(grid[0]):
        smudges += len(Get_Difference(Get_Column(c1, grid), Get_Column(c2, grid)))//2
        if smudges > 1:
            return False
        c1 -= 1
        c2 += 1
    return smudges == 1

def Check_Horizontal(row:int, grid:list[list[str]]) -> bool:
    r1, r2 = row, row+1
    smudges = 0
    while r1 >= 0 and r2 < len(grid):
        smudges += len(Get_Difference(grid[r1], grid[r2]))//2
        if smudges > 1:
            return False
        r1 -= 1
        r2 += 1
    return smudges == 1

total = 0
for grid in data:
    grid = [list(x) for x in grid.split("\n")]
    for row in range(len(grid)-1):
        total += 100*(row+1) if Check_Horizontal(row, grid) else 0
    for col in range(len(grid[0])-1):
        total += (col+1) if Check_Vertical(col, grid) else 0
print(total)