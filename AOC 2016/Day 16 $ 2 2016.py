from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 16 2016.txt"
# FILE_NAME = "Day 16 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()

DESIRED_LENGTH = 35651584
# DESIRED_LENGTH = 20

def step(a: str) -> str:
    b = a[::-1]
    b = b.replace("1", "$").replace("0", "1").replace("$", "0")
    return a + "0" + b

def checksum(a: str) -> str:
    result = ""
    for i in range(len(a) // 2):
        ch1, ch2 = a[i*2], a[i*2+1]
        result += "1" if ch1 == ch2 else "0"
    if len(result) % 2 == 0: return checksum(result)
    return result

while len(data) < DESIRED_LENGTH:
    data = step(data)

data = data[:DESIRED_LENGTH]
print(checksum(data))
print(f"Time Taken: {time()-t1:.2f}s")