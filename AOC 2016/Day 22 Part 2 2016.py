from time import time
t1 = time()
import re
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 22 2016.txt"
# FILE_NAME = "Day 22 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

pattern = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")

nodes = {}

for line in data:
    match = pattern.fullmatch(line)
    if match:
        x, y, size, used, avail, percent = map(int, match.groups())
        nodes[(x, y)] = (used, avail)

empty = next(pos for pos, (used, avail) in nodes.items() if used == 0)
goal = max(
    (pos for pos in nodes if pos[1] == 0),
    key=lambda pos: pos[0]
)

emptyCapacity = nodes[empty][1]

walls = {
    pos
    for pos, (used, avail) in nodes.items()
    if used > emptyCapacity
}

state = (empty, goal)

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

queue = deque([(empty, goal, 0)])
visited = {(empty, goal)}

while queue:
    empty, goal, moves = queue.popleft()

    if goal == (0, 0):
        print(moves)
        break

    for dx, dy in directions:
        newEmpty = (empty[0] + dx, empty[1] + dy)
        if newEmpty not in nodes:
            continue
        if newEmpty in walls:
            continue

        newGoal = empty if newEmpty == goal else goal
        state = (newEmpty, newGoal)

        if state in visited: continue
        visited.add(state)
        queue.append((newEmpty, newGoal, moves+1))

print(f"Time Taken: {time()-t1:.2f}s")