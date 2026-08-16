FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 10 2022.txt"
# FILE_NAME = "Day 10 2022 alt.txt"
# FILE_NAME = "Day 10 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

def Add(num):
    global cycle, total, register_value, curr_pixel, screen
    for i in range(num):
        cycle += 1
        if abs((curr_pixel%len(screen[0]))-register_value) <= 1:
            screen[curr_pixel//len(screen[0])][curr_pixel%len(screen[0])] = "#"
        curr_pixel += 1

screen = []
for _ in range(6):
    curr = []
    for __ in range(40):
        curr.append(".")
    screen.append(curr)

cycle = 0
register_value = 1
curr_pixel = 0

for line in data:
    line = line.strip()
    if line == "noop":
        Add(1)
        continue
    Add(2)
    register_value += int(line.split()[1])

for line in screen:
    print(*line, sep="")