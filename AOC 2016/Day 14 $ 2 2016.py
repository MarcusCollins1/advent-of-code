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
def hash(string: str) -> str:
    return md5(string.encode()).hexdigest()

@lru_cache(maxsize=None)
def hash2017(salt: str, index: int) -> str:
    string = f"{salt}{index}"
    for _ in range(2017):
        string = hash(string)
    return string


def isKey(salt: str, index: int) -> bool:
    pattern3 = r"(.)\1\1"
    match = re.search(pattern3, hash2017(salt, index))
    if match:
        repeatedChar = match.group(1)
        pattern5 = repeatedChar*5
        if any(re.search(pattern5, hash2017(salt, i)) for i in range(index+1, index+1001)):
            return True
    return False

keys = []
idx = 0
while True:
    if isKey(salt, idx):
        keys.append(idx)
        print(f"Found: {len(keys)}")
        if len(keys) == 64: break
    idx += 1

print(keys[-1])
print(f"Time Take: {time()-t1:.3f}s")