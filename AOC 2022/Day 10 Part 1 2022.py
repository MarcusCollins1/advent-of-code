FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 10 2022.txt"
# FILE_NAME = "Day 10 2022 alt.txt"
# FILE_NAME = "Day 10 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

def Add(num):
    global cycle, total, register_value
    for i in range(num):
        cycle += 1
        if (cycle-20)%40 == 0:
            total += cycle*register_value

cycle = 0
total = 0
register_value = 1

for line in data:
    line = line.strip()
    if line == "noop":
        Add(1)
        continue
    Add(2)
    register_value += int(line.split()[1])
print(total)