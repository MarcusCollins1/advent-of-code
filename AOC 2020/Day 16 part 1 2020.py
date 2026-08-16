input_file = open("Day 16 2020 ranges.txt")
input_file = open("Day 16 2020 ranges alt.txt")
ranges = []
for line in input_file:
    if line[-1] == "\n":
        ranges.append(line[:-1])
    else:
        ranges.append(line)

poses = set()
for i in ranges:
    lower = int(i.split("-")[0])
    upper = int(i.split("-")[1])
    for j in range(lower,upper+1):
        poses.add(j)

#print(poses)

input_file = open("Day 16 2020 tickets.txt")
input_file = open("Day 16 2020 tickets alt.txt")
tickets = []
for line in input_file:
    if line[-1] == "\n":
        tickets.append(line[:-1])
    else:
        tickets.append(line)
total = 0
for i in tickets:
    curr_ticket = i.split(",")
    for j in curr_ticket:
        if int(j) not in poses:
            total += int(j)
print(total)