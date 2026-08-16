from hashlib import md5
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 17 2016.txt"
# FILE_NAME = "Day 17 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()

OPEN = ["b", "c", "d", "e", "f"]
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # UP, DOWN, LEFT, RIGHT
LET_DIR = {let: d for let, d in zip("UDLR", DIRS)}

def doHash(s: str) -> str:
    return md5(s.encode()).hexdigest()[:4]

queue: deque[str] = deque()
queue.append("")

while queue:
    curr: str = queue.popleft()
    # print(curr)
    row: int = sum(LET_DIR[x][0] for x in curr)
    col: int = sum(LET_DIR[x][1] for x in curr)
    if row == 3 and col == 3:
        print(curr)
        quit()
    hash = doHash(data+curr)
    possibleDirs: list[str] = []
    # Up
    if hash[0] in OPEN and row != 0:
        possibleDirs.append("U")
    # Down
    if hash[1] in OPEN and row != 3:
        possibleDirs.append("D")
    # Left
    if hash[2] in OPEN and col != 0:
        possibleDirs.append("L")
    # Right
    if hash[3] in OPEN and col != 3:
        possibleDirs.append("R")

    for d in possibleDirs:
        queue.append(curr+d)