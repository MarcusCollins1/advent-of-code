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
code = ""

while len(code) < 8:
    result = md5(f"{DOOR_ID}{index}".encode()).hexdigest()
    if result[:5] == "00000":
        code += result[5]
        print(code)
    index += 1
print(code)