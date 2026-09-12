import re
from math import prod
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 03 2024.txt"
# FILE_NAME = "Day 03 2024 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read()
file.close()

def CheckIndex(index: int, doIndexes: list[int], dontIndexes: list[int]) -> bool:
    dosLower = [i for i in doIndexes if i < index]
    dontsLower = [i for i in dontIndexes if i < index]
    if len(dosLower) == 0:
        return len(dontsLower) == 0
    if len(dontsLower) == 0:
        return True
    closestDo = max(dosLower)
    closestDont = max(dontsLower)
    return closestDo > closestDont

doIndexes = [i for i in range(len(data)-3) if data[i:i+4] == "do()"]
dontIndexes = [i for i in range(len(data)-6) if data[i:i+7] == "don't()"]

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = [(list(map(int, match.groups())), match.start()) for match in re.finditer(pattern, data)]
total = sum([prod(nums) for nums, index in matches if CheckIndex(index, doIndexes, dontIndexes)])
print(total)