from itertools import combinations
input_file = open("Day 9 2020.txt")
input_file = open("Day 9 2020 alt.txt")
data = []
for line in input_file:
    if line[-1] == "\n":
        data.append(int(line[:-1]))
    else:
        data.append(int(line))


count = 25
found = False

while not found:
    curr_list = list(data[count:count+25])
    flag = False
    for a,b in combinations(curr_list,2):
        if int(a) + int(b) == int(data[count+25]):
            flag = True
    if not flag:
        found = True
    else:
        count += 1

print(data[count+25])