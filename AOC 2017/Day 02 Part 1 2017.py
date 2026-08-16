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
    highest = 0
    lowest = float("inf")
    for j in i:
        curr_num = int(j)
        if curr_num > highest:
            highest = curr_num
        if curr_num < lowest:
            lowest = curr_num
    total.append(highest-lowest)
print(sum(total))