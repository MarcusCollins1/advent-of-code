from math import isqrt
from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 20 2015.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()
target = int(data[0])

def getAllFactors(n: int) -> list[int]:
    factors: set[int] = set()
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            other = n//i
            if other <=50: factors.add(i)
            if i<=50: factors.add(n//i)
    return sorted(factors)
def getNumPresents(houseNum: int) -> int:
    return sum(getAllFactors(houseNum))*11

biggest = 0
houseNum = 1
while True:
    numPresents = getNumPresents(houseNum)
    # if numPresents > biggest:
    #     biggest = numPresents
    #     print(f"{biggest} - {houseNum}")
    if numPresents >= target:
        print(houseNum)
        break
    houseNum+=1
deltaT = time()-t1
print(f"Time taken: {deltaT:.2f}s")