input_file = open("Day 7 2020_.txt")
input_file = open("Day 7 2020 alt.txt")
rules = []
for line in input_file:
    if line[-1] == "\n":
        rules.append(line[:-1])
    else:
        rules.append(line)

bags = dict()

for i in range(len(rules)):
    curr_list = rules[i].replace(" contain no other bags.", "")
    curr_list = curr_list.replace(" bags","")
    curr_list = curr_list.replace(" contain ", ",")
    curr_list = curr_list.replace(", ",",")
    curr_list = curr_list.replace(" bag","")
    curr_list = curr_list.replace(".","")
    curr_list = curr_list.split(",")
    ex = (len(curr_list)-1) * [0]
    for i in range(1,len(curr_list)):
        q = curr_list[i][2:]
        ex[i-1] = q
    
    bags[curr_list[0]] = tuple(ex)

#print(bags)
children_bag = dict()
for curr_bag in bags:
    
    queue = []
    visited = set()
    queue.append(curr_bag)
    visited.add(curr_bag)
    while len(queue) != 0:
        curr_col = queue.pop(0)
        for ne in bags[curr_col]:
            if ne not in visited:
                queue.append(ne)
                visited.add(ne)
    children_bag[curr_bag] = visited
    print(curr_bag)
    print(visited)
print(children_bag)
possible = []
for i in children_bag:
    if "shiny gold" in children_bag[i]:
        possible.append(i)
print(len(possible)-1)

    