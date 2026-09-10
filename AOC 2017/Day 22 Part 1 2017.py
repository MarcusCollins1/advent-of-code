from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 22 2017.txt"
# FILE_NAME = "Day 22 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

WIDTH, HEIGHT = len(data[0]), len(data)

infected = set() # Store as (x, y)

for r in range(HEIGHT):
    for c in range(WIDTH):
        if data[r][c] == "#":
            infected.add((c-WIDTH//2, r-HEIGHT//2))

currPos = (0, 0) # Store as (x, y)
currDir = (0, -1)
numInfections = 0

LEFT = {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)}
RIGHT = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}

for _ in range(10_000):
    currDir = RIGHT[currDir] if currPos in infected else LEFT[currDir]
    if currPos in infected: infected.remove(currPos)
    else:
        infected.add(currPos)
        numInfections += 1
    currPos = (currPos[0]+currDir[0], currPos[1]+currDir[1])

print(numInfections)
print(f"Time Taken: {time()-t1:.2f}s")