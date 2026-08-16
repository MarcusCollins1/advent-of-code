input_file = open("Day 1 2020.txt", "r")

check = []
for line in input_file:
    if line[-1] == "\n":
        check.append(int(line[:-1]))
    else:
        check.append(int(line))
#print(check)




from itertools import combinations

for a, b in combinations(check,2):
    if a+b == 2020:
        print(a*b)

