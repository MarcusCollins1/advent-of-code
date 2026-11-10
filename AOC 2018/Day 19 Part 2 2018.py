from time import time
t1 = time()
from math import isqrt
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 19 2018.txt"
# FILE_NAME = "Day 19 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


total = 0
N = 10551261
for i in range(1, isqrt(N) + 1):
    if N % i == 0:
        total += i
        if i != N // i:
            total += N // i

print(total)

print(f"Time Taken: {time()-t1:.2f}s")