from time import time
startTime = time()
from collections import deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME, WIDTH_HEIGHT, NUM_BYTES = "Day 18 2024.txt", 71, 1024
# FILE_NAME, WIDTH_HEIGHT, NUM_BYTES = "Day 18 2024 test.txt", 7, 12

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [tuple(map(int, x.strip().split(","))) for x in file.readlines()]
file.close()

while True:
    unsafeTiles: set[tuple[int, int]] = {(position[0], position[1]) for position in data[:NUM_BYTES]}

    visited: set[tuple[int, int]] = {(0, 0)}
    found = False

    queue: deque[tuple[int, int]] = deque([(0, 0)])
    while queue:
        currPosition = queue.pop()
        if currPosition == (WIDTH_HEIGHT-1, WIDTH_HEIGHT-1):
            found = True
            break
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nextPosition = (currPosition[0]+direction[0], currPosition[1]+direction[1])
            if (0 <= nextPosition[0] < WIDTH_HEIGHT) and (0 <= nextPosition[1] < WIDTH_HEIGHT) and (nextPosition not in visited) and (nextPosition not in unsafeTiles):
                visited.add(nextPosition)
                queue.append(nextPosition)
    if not found: break
    NUM_BYTES += 1
print(*data[NUM_BYTES-1], sep=",")
print(time()-startTime)