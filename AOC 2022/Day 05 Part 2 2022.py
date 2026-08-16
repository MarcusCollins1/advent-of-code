FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 5 2022.txt"
# FILE_NAME = "Day 5 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

stacks = []

for _ in range(len(data[0].replace("\n","").replace("[","").replace("]", "").replace("    ", "$").replace(" ", ""))):
    stacks.append(list())

count = 0
for line in data:
    line = line.replace("\n", "")
    if line[0] == " " and line[1] not in [" ", "["]:
        break
    line = line.replace("[","").replace("]", "").replace("    ", "$").replace(" ", "")
    for item, i in zip(line,range(len(line))):
        if item == "$":
            continue
        stacks[i].append(item)
    count += 1
for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]

def Move(lst):
    global stacks
    removing = stacks[lst[1]][-lst[0]:]
    stacks[lst[1]] = stacks[lst[1]][:-lst[0]]
    stacks[lst[2]] += removing

for line in data[count+2:]:
    line = list(map(int, line.replace("\n", "").replace("move ", "").replace(" from ", "$").replace(" to ", "$").split("$")))
    line[1] -= 1
    line[2] -= 1
    Move(line)

for stack in stacks:
    print(stack[-1], end="")
print()