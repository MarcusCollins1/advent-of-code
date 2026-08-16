from collections import defaultdict

FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 06 2015.txt"
FILE_NAME = "Day 06 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

lights = defaultdict(int)

for line in data:
    line = line.strip().replace("turn ", "").replace(" through ", " ").split()
    instruction, start, end = line[0], list(map(int, line[1].split(","))), list(map(int, line[2].split(",")))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if instruction == "on":
                lights[(x,y)] += 1
            elif instruction == "off":
                lights[(x,y)] -= 1
                lights[(x,y)] = max([lights[(x,y)], 0])
            elif instruction == "toggle":
                lights[(x,y)] += 2
print(sum(list(lights.values())))
    