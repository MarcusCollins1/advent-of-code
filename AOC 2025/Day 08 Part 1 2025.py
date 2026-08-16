from time import time
t1 = time()
from itertools import combinations
from collections import defaultdict, deque
from math import prod
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 08 2025.txt"
FILE_NAME = "Day 08 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data: list[list[int]] = [[int(y) for y in x.strip().split(",")] for x in file.readlines()]
file.close()

numConnections = 1000
numConnections = 10

def squaredDistance(pos1: list[int], pos2: list[int]) -> int:
    return sum([(p1-p2)**2 for p1, p2 in zip(pos1, pos2)])

squaredDistances: dict[tuple[tuple[int, int, int], tuple[int, int, int]], int] = {(tuple(pos1), tuple(pos2)): squaredDistance(pos1, pos2) for pos1, pos2 in combinations(data, 2)} #type: ignore
squaredDistances = dict(sorted(squaredDistances.items(), key=lambda x:x[1]))

connections = defaultdict(list)

for i in range(numConnections):
    pos1, pos2 = list(squaredDistances.keys())[i]
    connections[pos1].append(pos2)
    connections[pos2].append(pos1)

circuits: list[int] = []
positionsLeft: list[tuple[int, int, int]] = [tuple(pos) for pos in data] # type: ignore

def getLoop(connections: defaultdict[tuple[int, int, int], list[int]], startPos: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    loop: list[tuple[int, int, int]] = []
    queue = deque()
    queue.append(startPos)
    while queue:
        currPos = queue.popleft()
        loop.append(currPos)
        for pos in connections[currPos]:
            if pos not in loop+list(queue):
                queue.append(pos)

    return loop

while positionsLeft:
    currPos = positionsLeft[0]
    loop = getLoop(connections, currPos)
    circuits.append(len(loop))
    for pos in loop:
        positionsLeft.remove(pos)

circuits = sorted(circuits, reverse=True)
print(prod(circuits[:3]))

print(f"Time Taken: {time()-t1:.3f}s")