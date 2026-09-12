from time import time
t1 = time()
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 13 2016.txt"
# FILE_NAME = "Day 13 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
favNum = int(file.read().strip())
file.close()

def isOpenSpace(x: int, y: int, favNum: int) -> bool:
    num = x*x + 3*x + 2*x*y + y + y*y + favNum
    return bin(num).count("1")%2 == 0

DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]

target = (31, 39)
# target = (7, 4)

queue: deque[list[tuple[int, int]]] = deque()
queue.append([(1, 1)])
while queue:
    currPath = queue.popleft()
    currPos = currPath[-1]
    if currPos == target:
        # print(currPath)
        print(len(currPath)-1)
        break
    for direction in DIRECTIONS:
        x = direction[0] + currPos[0]
        y = direction[1] + currPos[1]
        if x<0 or y<0: continue
        if (x, y) in currPath: continue
        if isOpenSpace(x, y, favNum):
            queue.append(currPath+[(x,y)])

print(f"Time Taken: {time()-t1:.3f}")