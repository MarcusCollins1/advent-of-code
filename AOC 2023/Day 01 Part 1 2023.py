FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 01 2023.txt"
FILE_NAME = "Day 01 2023 alt.txt"
# FILE_NAME = "Day 01 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

total = 0
for line in data:
    digits = []
    for character in line:
        if character.isdigit():
            digits.append(character)
    total += int(f"{digits[0]}{digits[-1]}")

print(total)