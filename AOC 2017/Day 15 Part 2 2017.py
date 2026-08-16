from time import time
t1 = time()
import re
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 15 2017.txt"
# FILE_NAME = "Day 15 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

MASK = 0xFFFF

pattern = re.compile(r"Generator \w starts with (\d+)")
a, b = [int(re.match(pattern, line).groups()[0]) for line in data] # type: ignore
outputA = deque()
numA = 0
outputB = deque()
numB = 0
total = 0
compared = 0
while compared < 5_000_000:
    a, b = (a * 16807) % 2147483647, (b * 48271) % 2147483647
    if a % 4 == 0 and numA < 5_000_000:
        outputA.append(a)
        numA += 1
    if b % 8 == 0 and numB < 5_000_000:
        outputB.append(b)
        numB += 1
    if outputA and outputB:
        ca, cb = outputA.popleft(), outputB.popleft()
        if (ca&MASK) == (cb&MASK): total += 1
        compared += 1

print(total)

print(f"Time Taken: {time()-t1:.2f}s")