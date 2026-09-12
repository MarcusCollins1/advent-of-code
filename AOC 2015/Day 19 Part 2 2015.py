FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 19 2015.txt"
# FILE_NAME = "Day 19 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data, target = file.read().split("\n\n")
file.close()
data = [line.strip() for line in data.splitlines()]

target = target.strip()

replacements: list[tuple[str, str]] = []
for line in data:
    l1,l2 = line.split(" => ")
    replacements.append((l1,l2))

reverseReplacements: list[tuple[str, str]] = [(b, a) for (a, b) in replacements]
reverseReplacements.sort(key= lambda rule: len(rule[0]), reverse=True)

steps = 0
molecule = target

while molecule != "e":
    changed = False

    for (big, small) in reverseReplacements:
        idx = molecule.find(big)
        if idx != -1:
            molecule = molecule[:idx]+ small + molecule[idx+len(big):]
            steps += 1
            changed = True
            break
    if not changed:
        raise RuntimeError("No possible replacement: stuck on molecule:", molecule)
print(steps)