from collections import defaultdict
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 19 2015.txt"
FILE_NAME = "Day 19 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data, target = file.read().split("\n\n")
file.close()
data = [line.strip() for line in data.splitlines()]

def splitByCapitals(line: str) -> list[str]:
    output = []
    curr = ""
    for char in line:
        if char.upper() == char and curr != "":
            output.append(curr)
            curr = ""
        curr += char
    output.append(curr)
    return output

target = splitByCapitals(target)

replacements = defaultdict(list)
for line in data:
    l1,l2 = line.split(" => ")
    replacements[l1].append(l2)

molecules: set[str] = set()
for i, element in enumerate(target):
    for replacement in replacements[element]:
        x = target[:]
        x[i] = replacement
        molecules.add("".join(x))
print(len(molecules))