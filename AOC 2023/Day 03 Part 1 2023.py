FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 03 2023.txt"
# FILE_NAME = "Day 03 2023 alt.txt"
# FILE_NAME = "Day 03 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

def CheckPosition(row:int, col:int, grid:list) -> bool:
    # Check U
    if row != 0:
        if grid[row-1][col] not in "0123456789.":
            return True
    # Check UR
    if row != 0 and col != (len(grid[row])-1):
        if grid[row-1][col+1] not in "0123456789.":
            return True
    # Check R
    if col != (len(grid[row])-1):
        if grid[row][col+1] not in "0123456789.":
            return True
    # Check DR
    if row != (len(grid)-1) and col != (len(grid[row])-1):
        if grid[row+1][col+1] not in "0123456789.":
            return True
    # Check D
    if row != (len(grid)-1):
        if grid[row+1][col] not in "0123456789.":
            return True
    # Check DL
    if row != (len(grid)-1) and col != 0:
        if grid[row+1][col-1] not in "0123456789.":
            return True
    # Check L
    if col != 0:
        if grid[row][col-1] not in "0123456789.":
            return True
    # Check UL
    if row != 0 and col != 0:
        if grid[row-1][col-1] not in "0123456789.":
            return True
    return False

def CheckNumber(row:int, start:int, end:int, grid:list) -> bool:
    for col in range(start, end):
        if CheckPosition(row, col, grid):
            return True
    return False

total = 0

for row, line in enumerate(data):
    curr_number = ""
    curr_number_start = 0
    col = 0
    for col, chararcter in enumerate(line):
        if chararcter.isdigit():
            if curr_number == "":
                curr_number_start = col
            curr_number += chararcter
        elif curr_number != "":
            total += int(curr_number) if CheckNumber(row, curr_number_start, col, data) else 0
            curr_number = ""
            curr_number_start = 0
    if curr_number != "":
        total += int(curr_number) if CheckNumber(row, curr_number_start, col, data) else 0

print(total)