import pyperclip
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 5 2018.txt"
FILE_NAME = "Day 5 2018 alt.txt"
# FILE_NAME = "Day 5 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def RemoveUnits(polymer:str) -> str:
    result = ['']
    for unit in polymer:
        if unit == result[-1].swapcase():
            result.pop()
        else:
            result.append(unit)
    return "".join(result)

minimum = float("inf")
original_polymer = data[0]
for letter in "abcdefghijklmnopqrstuvwxyz":
    minimum = min([minimum, len(RemoveUnits(original_polymer.replace(letter, "").replace(letter.upper(), "")))])

pyperclip.copy(minimum)
print(minimum)