from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 19 2017.txt"
# FILE_NAME = "Day 19 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x) for x in file.readlines()]
file.close()

row = 0
col = data[0].index("|")
dRow = 1
dCol = 0

msg = ""

while True:
    row, col = row+dRow, col+dCol
    cell = data[row][col]
    if cell in ["|", "-", "+"]:
        if cell == "+":
            # Check Up
            if (not (dRow == 1 and dCol == 0)) and (data[row-1][col] != " "):
                dRow, dCol = -1, 0
            # Check Right
            elif (not (dRow == 0 and dCol == -1)) and (data[row][col+1] != " "):
                dRow, dCol = 0, 1
            # Check Down
            elif (not (dRow == -1 and dCol == 0)) and (data[row+1][col] != " "):
                dRow, dCol = 1, 0
            # Check left
            elif (not (dRow == 0 and dCol == 1)) and (data[row][col-1] != " "):
                dRow, dCol = 0, -1
    elif cell == " ": break
    else:
        msg += cell

print(msg)


print(f"Time Taken: {time()-t1:.2f}s")