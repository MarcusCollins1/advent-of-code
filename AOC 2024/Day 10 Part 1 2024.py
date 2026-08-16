from collections import defaultdict, deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 10 2024.txt"
# FILE_NAME = "Day 10 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(map(int, list(x.strip()))) for x in file.readlines()]
file.close()

trailHeads: defaultdict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set[tuple[int, int]])
trailEnds: set[tuple[int, int]] = set()

queue = deque([((x, y), (x, y)) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 0])

while queue:
    currStart, currPos = queue.popleft()
    if data[currPos[1]][currPos[0]] == 9:
        trailHeads[currStart].add(currPos)
        trailEnds.add(currPos)
        continue
    # Up
    newPos = (currPos[0]-1, currPos[1])
    if (0 <= newPos[0] < len(data[0])) and (0 <= newPos[1] < len(data)):
        if data[newPos[1]][newPos[0]] == data[currPos[1]][currPos[0]] + 1:
            queue.append((currStart, newPos))
    # Right
    newPos = (currPos[0], currPos[1]+1)
    if (0 <= newPos[0] < len(data[0])) and (0 <= newPos[1] < len(data)):
        if data[newPos[1]][newPos[0]] == data[currPos[1]][currPos[0]] + 1:
            queue.append((currStart, newPos))
    # Down
    newPos = (currPos[0]+1, currPos[1])
    if (0 <= newPos[0] < len(data[0])) and (0 <= newPos[1] < len(data)):
        if data[newPos[1]][newPos[0]] == data[currPos[1]][currPos[0]] + 1:
            queue.append((currStart, newPos))
    # Left
    newPos = (currPos[0], currPos[1]-1)
    if (0 <= newPos[0] < len(data[0])) and (0 <= newPos[1] < len(data)):
        if data[newPos[1]][newPos[0]] == data[currPos[1]][currPos[0]] + 1:
            queue.append((currStart, newPos))

print(sum([len(x) for x in trailHeads.values()]))