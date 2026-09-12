FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 3 2022.txt"
FILE_NAME = "Day 3 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

PRIORITIES = dict()
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter, num in zip(LETTERS, range(1, 53)):
    PRIORITIES[letter] = num

groups = []
curr = []
for line in data:
    line = line.strip()
    if len(curr) == 3:
        groups.append(curr)
        curr = []
    curr.append(line)
groups.append(curr)

total = 0
for group in groups:
    total += PRIORITIES[list(set(group[0]).intersection(set(group[1]), set(group[2])))[0]]
print(total)