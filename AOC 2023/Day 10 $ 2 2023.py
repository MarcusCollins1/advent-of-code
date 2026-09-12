FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 10 2023.txt"
# FILE_NAME = "Day 10 2023 alt.txt"
# FILE_NAME = "Day 10 2023 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)

DIRECTIONS = {'S':(N, S, E, W), '|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}

down = {'|', '7', 'F'}

x, y = 0, 0
for i in range(len(data)):        
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            x, y = i, j
            break
queue = []
visited = {(x, y)}
if N in DIRECTIONS[data[x + 1][y]]:
    queue.append(((x + 1, y), 1))
    visited.add((x + 1, y))
    down.add('S')
if S in DIRECTIONS[data[x - 1][y]]:
    queue.append(((x - 1, y), 1))
    visited.add((x - 1, y))
if E in DIRECTIONS[data[x][y - 1]]:
    queue.append(((x, y - 1), 1))
    visited.add((x, y - 1))
if W in DIRECTIONS[data[x][y + 1]]:
    queue.append(((x, y + 1), 1))
    visited.add((x, y + 1))

while queue:
    (x, y), cost = queue.pop(0)
    for offset in DIRECTIONS[data[x][y]]:
        next = (x + offset[0], y + offset[1])
        if next not in visited:
            queue.append((next, cost + 1))
            visited.add(next)

counter = 0
for i in range(len(data)):
    up = False
    for j in range(len(data[i])):
        if data[i][j] in down and (i, j) in visited:
            up = not up
        if up and (i, j) not in visited:
            counter += 1
print(counter)