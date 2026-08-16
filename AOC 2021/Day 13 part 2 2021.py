from copy import deepcopy
from time import time
t1 = time()
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 13 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 13 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 13 2021 test.txt", "r")
file = input_file.read().splitlines()
separator = file.index("")
poses, folds = file[:separator], file[separator+1:]
positions = set()
for line in poses:
    curr_x, curr_y = line.split(",")
    positions.add((int(curr_x), int(curr_y)))

for line in folds:
    line = line.replace("fold along", "").replace("=", "").replace(" ", "")
    amount = int(line[1:])
    loop = set()
    if line[0] == "y":
        for pos in positions:
            if pos[1] > amount:
                loop.add((pos[0], 2*amount-pos[1]))
            else:
                loop.add(pos)
    else:
        for pos in positions:
            if pos[0] > amount:
                loop.add((2*amount-pos[0], pos[1]))
            else:
                loop.add(pos)
    positions = deepcopy(loop)
max_x, max_y = 0, 0
for pos in positions:
    curr_x, curr_y = pos
    max_x, max_y = max([max_x, curr_x]), max([max_y, curr_y])
for i in range(max_y+1):
    for j in range(max_x+1):
        if (j, i) in positions:
            print("#", end="")
        else:
            print(" ", end="")
    print()