from hashlib import md5

FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 5 2016.txt"
# FILE_NAME = "Day 5 2016 alt.txt"
# FILE_NAME = "Day 5 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

DOOR_ID = data[0]

index = 0
code = "xxxxxxxx"

while "x" in code:
    result = md5(f"{DOOR_ID}{index}".encode()).hexdigest()
    if result[:5] == "00000":
        pos = result[5]
        val = result[6]
        if "0" <= pos <= "7":
            pos = int(pos)
            if code[pos] == "x":
                code = code[:pos] + val + code[pos+1:]
    index += 1
print(code)