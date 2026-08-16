from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 03 2023.txt"
# FILE_NAME = "Day 03 2023 alt.txt"
# FILE_NAME = "Day 03 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

def CheckPosition(row:int, col:int, grid:list):
    # Check U
    if row != 0:
        if grid[row-1][col] == "*":
            return (row-1, col)
    # Check UR
    if row != 0 and col != (len(grid[row])-1):
        if grid[row-1][col+1] == "*":
            return (row-1, col+1)
    # Check R
    if col != (len(grid[row])-1):
        if grid[row][col+1] == "*":
            return (row, col+1)
    # Check DR
    if row != (len(grid)-1) and col != (len(grid[row])-1):
        if grid[row+1][col+1] == "*":
            return (row+1, col+1)
    # Check D
    if row != (len(grid)-1):
        if grid[row+1][col] == "*":
            return (row+1, col)
    # Check DL
    if row != (len(grid)-1) and col != 0:
        if grid[row+1][col-1] == "*":
            return (row+1, col-1)
    # Check L
    if col != 0:
        if grid[row][col-1] == "*":
            return (row, col-1)
    # Check UL
    if row != 0 and col != 0:
        if grid[row-1][col-1] == "*":
            return (row-1, col-1)
    return False

def CheckNumber(row:int, start:int, end:int, grid:list):
    for col in range(start, end):
        ans = CheckPosition(row, col, grid)
        if ans != False:
            return ans
    return False

gears = defaultdict(list)
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
            ans = CheckNumber(row, curr_number_start, col, data)
            if ans != False:
                gears[ans].append(curr_number)
            curr_number = ""
            curr_number_start = 0
    if curr_number != "":
        ans = CheckNumber(row, curr_number_start, col, data)
        if ans != False:
            gears[ans].append(curr_number)
for val in gears.values():
    if len(val) == 2:
        total += int(val[0])*int(val[1])
print(total)