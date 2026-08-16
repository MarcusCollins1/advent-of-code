from time import time
from itertools import combinations
from math import prod
from functools import lru_cache
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 24 2015.txt"
# FILE_NAME = "Day 24 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()
parcels = [int(x) for x in data]
parcels.sort(reverse=True)
totalPerGroup = sum(parcels) // 4
n = len(parcels)

@lru_cache(maxsize=None)
def canPartition(usedMask: int, groupsLeft: int, currentSum: int, startIndex: int) -> bool:
    if groupsLeft == 1:
        return sum(parcels[i] for i in range(n) if not (usedMask >> i) & 1) == totalPerGroup
    
    for i in range(startIndex, n):
        if (usedMask >> i) & 1:
            continue
        nextSum = currentSum + parcels[i]
        if nextSum > totalPerGroup:
            continue
        nextUsedMask = usedMask | (1 << i)
        if nextSum == totalPerGroup:
            if canPartition(nextUsedMask, groupsLeft - 1, 0, 0):
                return True
        else:
            if canPartition(nextUsedMask, groupsLeft, nextSum, i + 1):
                return True
    return False

n1 = 1
while True:
    groups1 = [group1 for group1 in combinations(parcels, n1) if sum(group1) == totalPerGroup]
    if groups1:
        break
    n1 += 1

groups1.sort(key=prod)
bestQE = None
for group1 in groups1:
    usedMask = 0
    for parcel in group1:
        for i in range(n):
            if ((usedMask >> i) & 1) == 0 and parcels[i] == parcel:
                usedMask |= (1 << i)
                break
    if canPartition(usedMask, 3, 0, 0):
        bestQE = prod(group1)
        break

print(bestQE)
tDelta = time() - t1
print(f"Time taken: {tDelta:.2f} seconds")