from collections import defaultdict

FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 06 2015.txt"
FILE_NAME = "Day 06 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

lights = defaultdict(bool)

for line in data:
    line = line.strip().replace("turn ", "").replace(" through ", " ").split()
    instruction, start, end = line[0], list(map(int, line[1].split(","))), list(map(int, line[2].split(",")))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if instruction == "on":
                lights[(x,y)] = True
            elif instruction == "off":
                lights[(x,y)] = False
            elif instruction == "toggle":
                lights[(x,y)] = not lights[(x,y)]
print(list(lights.values()).count(True))
    