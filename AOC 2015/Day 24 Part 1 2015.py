from time import time
from itertools import combinations
from math import prod
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 24 2015.txt"
# FILE_NAME = "Day 24 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()
parcels = [int(x) for x in data]
totalPerGroup = sum(parcels) // 3

def isValidGroup1(group1: list[int], parcels: list[int], totalPerGroup: int) -> bool:
    parcelsLeft = [parcel for parcel in parcels if parcel not in group1]
    for n in range(1, len(parcelsLeft)):
        for group2 in combinations(parcelsLeft, n):
            if sum(group2) == totalPerGroup:
                return True
    return False

n = 1
while True:
    validGroup1s = []
    for group1 in combinations(parcels, n):
        if sum(group1) == totalPerGroup:
            validGroup1s.append(list(group1))
    if validGroup1s: break
    n += 1

validGroup1s = [group1 for group1 in validGroup1s if isValidGroup1(group1, parcels, totalPerGroup)]
print(min(prod(group1) for group1 in validGroup1s))
tDelta = time() - t1
print(f"Time taken: {tDelta:.2f} seconds")