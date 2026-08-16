from time import time
from collections import defaultdict
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 5 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 5 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 5 2021 test.txt", "r")

file = input_file.readlines()
data = []
for line in file:
    if line[-1] == "\n":
        data.append(line[:-1])
        continue
    data.append(line)



co_ords = []

for line in data:
    curr = line.split(" -> ")
    x1, y1 = curr[0].split(",")
    x2, y2 = curr[1].split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    # find if they are vert
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2+1):
                co_ords.append(str(str(x1)+","+str(i)))
        else:
            for i in range(int(y2), int(y1)+1):
                co_ords.append(str(str(x1)+","+str(i)))
    # find if they are horiz
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2+1):
                co_ords.append(str(str(i)+","+str(y1)))
        else:
            for i in range(x2, x1+1):
                co_ords.append(str(str(i)+","+str(y1)))
    else:
        if  x1 < x2:
            if y1 < y2:
                for i in range(x2-x1+1):
                    next_co = (str(str(x1+i)+","+str(y1+i)))
                    co_ords.append(next_co)
            else:
                for i in range(x2-x1+1):
                    next_co = (str(str(x1+i)+","+str(y1-i)))
                    co_ords.append(next_co)
        else:
            if y1 < y2:
                for i in range(x1-x2+1):
                    next_co = (str(str(x2+i)+","+str(y2-i)))
                    co_ords.append(next_co)
            else:
                for i in range(x1-x2+1):
                    next_co = (str(str(x2+i)+","+str(y2+i)))
                    co_ords.append(next_co)
        



totals = defaultdict(int)
for co_ord in co_ords:
    totals[co_ord] += 1


total = 0
for i in totals.values():
    total += (i >= 2)
print(total)