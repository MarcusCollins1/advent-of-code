import re
from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 02 2025.txt"
# FILE_NAME = "Day 02 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0].split(",")
file.close()

data = [list(map(int, x.split("-"))) for x in data]

t1 = time()

def isInvalid(num: int) -> bool:
    pattern = r"^(.+)\1+$"
    return bool(re.match(pattern, str(num)))
print(sum([i for x1, x2 in data for i in range(x1,x2+1) if isInvalid(i)]))
print(f"Time taken: {time()-t1:.3f}s")