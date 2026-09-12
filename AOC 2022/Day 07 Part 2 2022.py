from collections import defaultdict
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 7 2022.txt"
# FILE_NAME = "Day 7 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

paths = defaultdict(int)

curr_path = []
for line in data:
    line = line.replace("\n", "").replace("\\", "/")
    if line[:4] == "$ cd":
        if line == "$ cd ..":
            curr_path.pop(-1)
        else:
            curr_path.append(line.replace("$ cd ", ""))
    elif line == "$ ls":
        continue
    elif line[:3] == "dir":
        continue
    else:
        for i in range(1, len(curr_path)+1):
            paths[",".join(curr_path[:i])] += int(line.split()[0])

spaceNeeded = 30000000-(70000000-paths["/"])

for num in sorted(paths.values()):
    if num >= spaceNeeded:
        print(num)
        break