from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 03 2025.txt"
# FILE_NAME = "Day 03 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def getMaxJoltage(bank: list[int]) -> int:
    maximum = max(bank[:-1])
    maxIndex = bank.index(maximum)
    secondMax = max(bank[maxIndex+1:])
    return maximum*10+secondMax

print(sum([getMaxJoltage(list(map(int, list(bank)))) for bank in data]))

print(f"Time Taken: {time()-t1:.3f}s")