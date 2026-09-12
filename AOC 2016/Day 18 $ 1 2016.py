from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 18 2016.txt"
# FILE_NAME = "Day 18 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()

TOTAL_ROWS = 40
# TOTAL_ROWS = 10

def createNewRow(board: list[list[bool]]) -> list[list[bool]]:
    currRow = board[-1]
    newRow = []
    for i in range(len(currRow)):
        left = True if i == 0 else currRow[i-1]
        centre = currRow[i]
        right = True if i == len(currRow)-1 else currRow[i+1]

        if ((not left) and (not centre) and (right)) or ((left) and (not centre) and (not right)) or ((not left) and (centre) and (right)) or ((left) and (centre) and (not right)):
            newRow.append(False)
        else:
            newRow.append(True)
    board.append(newRow)
    return board

board = [[x == "." for x in data]]
for i in range(TOTAL_ROWS-1):
    board = createNewRow(board)

print(sum(sum(row) for row in board))


print(f"Time Taken: {time()-t1:.2f}s")