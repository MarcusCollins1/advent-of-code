from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 15 2017.txt"
# FILE_NAME = "Day 15 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

MASK = 0xFFFF

pattern = re.compile(r"Generator \w starts with (\d+)")
a, b = [int(re.match(pattern, line).groups()[0]) for line in data] # type: ignore

total = 0

for _ in range(4*10**7):
    a, b = (a * 16807) % 2147483647, (b * 48271) % 2147483647
    if (a & MASK) == (b & MASK): total += 1
print(total)

print(f"Time Taken: {time()-t1:.2f}s")