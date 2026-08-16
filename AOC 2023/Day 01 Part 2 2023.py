FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 01 2023.txt"
# FILE_NAME = "Day 01 2023 alt.txt"
# FILE_NAME = "Day 01 2023 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


def checknumbers(line: str, i: int):
    length = len(line)
    if i+3 <= length:
        if line[i:i+3] == "one":
            return 1
        elif line[i:i+3] == "two":
            return 2
        elif line[i:i+3] == "six":
            return 6
    if i+4 <= length:
        if line[i:i+4] == "four":
            return 4
        elif line[i:i+4] == "five":
            return 5
        elif line[i:i+4] == "nine":
            return 9
    if i+5 <= length:
        if line[i:i+5] == "three":
            return 3
        elif line[i:i+5] == "seven":
            return 7
        elif line[i:i+5] == "eight":
            return 8
    return 0

total = 0
for line in data:
    digits = []
    for i, character in enumerate(line):
        if character.isdigit():
            digits.append(character)
        elif checknumbers(line, i):
            digits.append(str(checknumbers(line, i)))
    total += int(f"{digits[0]}{digits[-1]}")

print(total)