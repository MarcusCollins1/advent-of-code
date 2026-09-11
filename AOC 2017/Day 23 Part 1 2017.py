from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 23 2017.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip().split() for x in file.readlines()]
file.close()

def getValue(val: str) -> int:
    try:
        v = int(val)
    except:
        v = register[val]
    return v

mulUsed = 0
idx = 0
register = {x: 0 for x in "abcdefgh"}
while idx < len(data):
    instruction = data[idx]
    if instruction[0] == "set":
        register[instruction[1]] = getValue(instruction[2])
        idx += 1
    elif instruction[0] == "sub":
        register[instruction[1]] -= getValue(instruction[2])
        idx += 1
    elif instruction[0] == "mul":
        register[instruction[1]] *= getValue(instruction[2])
        mulUsed += 1
        idx += 1
    elif instruction[0] == "jnz":
        if getValue(instruction[1]) == 0:
            idx += 1
        else:
            idx += getValue(instruction[2])
    
print(mulUsed)
print(f"Time Taken: {time()-t1:.2f}s")