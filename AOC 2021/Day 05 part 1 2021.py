from time import time
from collections import defaultdict
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 5 2021.txt", "r")
# home account
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 5 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 5 2021 test.txt", "r")

# list of all the lines
data = input_file.read().splitlines()
# make empty list to store co-ordinates in form (x, y)
co_ords = []
# loop through each of the lines
for line in data:
    # find x1, y1, x2, y2
    curr = line.split(" -> ")
    x1, y1 = curr[0].split(",")
    x2, y2 = curr[1].split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    # find if they are vert
    if x1 == x2:
        for i in range(min([y1, y2]), max([y1,y2])+1):
            co_ords.append(str(str(x1)+","+str(i)))
    # find if they are horiz
    elif y1 == y2:
        for i in range(min([x1,x2]), max([x1,x2])+1):
            co_ords.append(str(str(i)+","+str(y1)))
# find how many times each co-ordinate appears
totals = defaultdict(int)
for co_ord in co_ords:
    totals[co_ord] += 1
# find how many co-ordinates appear more than once
total = 0
for i in totals.values():
    total += (i >= 2)
print(total)