from itertools import combinations
from copy import deepcopy

FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 12 2023.txt"
# FILE_NAME = "Day 12 2023 alt.txt"
# FILE_NAME = "Day 12 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

lines, nums = [], []
for line in data:
    line = line.split()
    lines.append(list(line[0]))
    nums.append(list(map(int, line[1].split(","))))

def IsValid(row:list, ns:list) -> bool:
    index = 0
    count = 0
    for character in row:
        if character == "#":
            count += 1
        elif count == 0:
            continue
        else:
            if count != ns[index]:
                return False
            count = 0
            index += 1
    if index < len(ns):
        if count != 0 and count != ns[index]:
            return False
    return True
def GetUnknowns(line:list) -> list:
    output = []
    for i, x in enumerate(line):
        if x == "?":
            output.append(i)
    return output

total = 0
for line, num in zip(lines, nums):
    unknowns = GetUnknowns(line)
    needed = sum(num)-line.count("#")
    for x in combinations(unknowns, needed):
        new_line = deepcopy(line)
        for uk in unknowns:
            new_line[uk] = "."
        for y in x:
            new_line[y] = "#"
        total += 1 if IsValid(new_line, num) else 0
print(total)