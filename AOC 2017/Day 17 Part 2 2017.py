from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 17 2017.txt"
# FILE_NAME = "Day 17 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
STEPS = int([x.strip() for x in file.readlines()][0])
file.close()

position = 0
valueAfterZero = 0

for value in range(1, 50_000_001):
    position = (position + STEPS) % value
    position += 1

    if position == 1: valueAfterZero = value

print(valueAfterZero)

print(f"Time Taken: {time()-t1:.2f}s")