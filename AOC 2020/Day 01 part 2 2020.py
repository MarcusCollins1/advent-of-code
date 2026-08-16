input_file = open("Day 1 2020.txt")
check = []
for line in input_file:
    if line[-1] == "\n":
        check.append(int(line[:-1]))
    else:
        check.append(int(line))
#print(masses)
from itertools import combinations
for a,b,c in combinations(check,3):
    if a+b+c == 2020:
        print(a*b*c)