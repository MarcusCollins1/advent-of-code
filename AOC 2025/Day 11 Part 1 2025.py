from time import time
t1 = time()
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 11 2025.txt"
# FILE_NAME = "Day 11 2025 test 1.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


connections: dict[str, list[str]] = {line.split(": ")[0]: line.split(": ")[1].split() for line in data}

start = "you"
target = "out"

queue: deque[list[str]] = deque()
queue.append([start])
count = 0

while queue:
    currPath = queue.popleft()
    currPos = currPath[-1]
    if currPos == target:
        count += 1
        continue
    for connection in connections[currPos]:
        queue.append(currPath+[connection])


print(count)

print(f"Time Taken: {time()-t1:.3f}s")