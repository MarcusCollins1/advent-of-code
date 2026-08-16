input_file = open("Day 16 2020 ranges.txt")
###
input_file = open("Day 16 2020 ranges alt.txt")
ranges = []
for line in input_file:
    if line[-1] == "\n":
        ranges.append(line[:-1])
    else:
        ranges.append(line)

input_file = open("Day 16 2020 tickets.txt")
###
input_file = open("Day 16 2020 tickets alt.txt")
tickets = []
for line in input_file:
    if line[-1] == "\n":
        tickets.append(line[:-1])
    else:
        tickets.append(line)

if True:
    poses = set()
    for i in ranges:
        lower = int(i.split("-")[0])
        upper = int(i.split("-")[1])
        for j in range(lower,upper+1):
            poses.add(j)


    total = 0
    for i in tickets:
        curr_ticket = i.split(",")
        for j in curr_ticket:
            if int(j) not in poses:
                total += int(j)
    print("total",total)
    
    for i in tickets:
        curr_ticket = i.split(",")
        for j in curr_ticket:
            if int(j) not in poses:
                tickets.remove(i)
                break
    



    total = 0
    for i in tickets:
        curr_ticket = i.split(",")
        for j in curr_ticket:
            if int(j) not in poses:
                total += int(j)
    print("total",total)



poses = []

for i in range(len(ranges)):
    if i % 2 == 0:
        curr_list = []
    lower = int(ranges[i].split("-")[0])
    upper = int(ranges[i].split("-")[1])
    for j in range(lower,upper+1):
        curr_list.append(str(j))
    if i % 2 != 0:
        poses.append(curr_list)

#print(poses)



my_ticket = [139,109,61,149,101,89,103,53,107,59,73,151,71,67,97,113,83,163,137,167]
###
#my_ticket = [11,12,13]

pos = []

for k in range(len(my_ticket)):

    pos_first = []
    for i in range(len(poses)):
        if str(my_ticket[k]) in poses[i]:
            pos_first.append(str(i))
    #print(pos_first)
    #print(tickets)
    for i in tickets:
        for j in pos_first:
            if i.split(",")[k] not in poses[int(j)]:
                pos_first.remove(j)
    #print(pos_first)
    pos.append(pos_first)



print(pos)

catergories = []

curr = True
while curr:
    curr = False
    for i in pos:
        
        if len(i) == 1:
            x = pos.index(i),",",i
            catergories.append(x)
            curr = True
            pos[pos.index(i)] == ""
        
print(catergories)