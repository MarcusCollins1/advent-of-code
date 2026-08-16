from time import time
t1 = time()

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 08 2025.txt"
# FILE_NAME = "Day 08 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data: list[tuple[int, int, int]] = [(x, y, z) for (x,y,z) in [map(int, line.strip().split(",")) for line in file.readlines()]]
file.close()

numPos = len(data)
parent = list(range(numPos))
size = [1] * numPos
components = numPos

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    global components
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    components -= 1
    return True

dists = []
for i in range(numPos):
    x1, y1, z1 = data[i]
    for j in range(i+1, numPos):
        x2, y2, z2 = data[j]
        dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        dists.append((dist, i, j))

dists.sort(key=lambda x: x[0])

lastPair = None

for dist, i, j in dists:
    if union(i, j):
        lastPair = (i, j)
        if components == 1:
            break

x1 = data[lastPair[0]][0] #type: ignore
x2 = data[lastPair[1]][0] #type: ignore
print(x1*x2)


print(f"Time Taken: {time()-t1:.3f}s")