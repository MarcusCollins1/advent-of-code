from time import time
t1 = time()
from hashlib import md5
import re
from functools import lru_cache
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 14 2016.txt"
# FILE_NAME = "Day 14 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
salt = file.read().strip()
file.close()

@lru_cache(maxsize=None)
def hash(salt: str, index: int) -> str:
    return md5(f"{salt}{index}".encode()).hexdigest()

def isKey(salt: str, index: int) -> bool:
    pattern3 = r"(.)\1\1"
    match = re.search(pattern3, hash(salt, index))
    if match:
        repeatedChar = match.group(1)
        pattern5 = repeatedChar*5
        if any(re.search(pattern5, hash(salt, i)) for i in range(index+1, index+1001)):
            return True
    return False

keys = []
idx = 0
while True:
    if isKey(salt, idx):
        keys.append(idx)
        if len(keys) == 64: break
    idx += 1

print(keys[-1])
print(f"Time Take: {time()-t1:.3f}s")