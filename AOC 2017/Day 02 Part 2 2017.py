from itertools import combinations
# rows_file = open("Day 2 2017.txt")
rows_file = open("Day 2 2017 alt.txt")
rows = []
for line in rows_file:
    if line[-1] == "\n":
        curr_row = line[:-1].split("\t")
    else:
        curr_row = line.split("\t")
    rows.append(curr_row)

total = []
for i in rows:
    for x,y in combinations(i,2):
        x = int(x)
        y = int(y)
        if x % y == 0:
            total.append(x//y)
        elif y % x == 0:
            total.append(y//x)
print(sum(total))

