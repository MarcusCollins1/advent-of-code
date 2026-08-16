from math import prod
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 02 2015.txt"
FILE_NAME = "Day 02 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

total = 0
for line in data:
    lengths = sorted(list(map(int, line.strip().split("x"))))
    total += 2*(sum(lengths[:2]))+prod(lengths)
print(total)