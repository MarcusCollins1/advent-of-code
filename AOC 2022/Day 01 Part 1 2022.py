FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 1 2022.txt"
FILE_NAME = "Day 1 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

elves = []
curr = []
for line in data:
    line = line.strip()
    if line == "":
        elves.append(curr)
        curr = []
        continue
    curr.append(int(line))
elves.append(curr)

biggest = 0
for elf in elves:
    biggest = max([biggest, sum(elf)])
print(biggest)