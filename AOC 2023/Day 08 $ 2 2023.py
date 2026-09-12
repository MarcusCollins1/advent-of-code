from math import lcm

FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 08 2023.txt"
# FILE_NAME = "Day 08 2023 alt.txt"
# FILE_NAME = "Day 08 2023 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

LR = list(data[0])

tunnels = dict()
for line in data[2:]:
    line = line.replace("(", "").replace(" = ", ", ").replace(")", "").split(", ")
    tunnels[line[0]] = line[1:]

locations = []
for place in tunnels.keys():
    if place[-1] == "A":
        locations.append(place)

stepses = []
for place in locations:
    curr_location = place
    steps = 0
    lr_index = 0
    while curr_location[-1] != "Z":
        curr_location = tunnels[curr_location][0 if LR[lr_index] == "L" else 1]
        steps += 1
        lr_index = (lr_index+1)%len(LR)
    stepses.append(steps)
print(lcm(*stepses))