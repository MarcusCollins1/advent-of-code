input_file = open("Day 7 2020.txt")
input_file = open("Day 7 2020 alt.txt")
rules = []
for line in input_file:
    if line[-1] == "\n":
        rules.append(line[:-1])
    else:
        rules.append(line)

bags = dict()
bags_num = dict()
for i in range(len(rules)):
    curr_list = rules[i].replace(" contain no other bags.", "")
    curr_list = curr_list.replace(" bags","")
    curr_list = curr_list.replace(" contain ", ",")
    curr_list = curr_list.replace(", ",",")
    curr_list = curr_list.replace(" bag","")
    curr_list = curr_list.replace(".","")
    curr_list = curr_list.split(",")
    ex = (len(curr_list)-1) * [0]
    y = (len(curr_list)-1) * [0]
    for i in range(1,len(curr_list)):
        q = curr_list[i][2:]
        ex[i-1] = q
        y[i-1] = int(curr_list[i][0])
    bags[curr_list[0]] = list(ex)
    bags_num[curr_list[0]] = list(y)


def num_bags(bag_colour):
    # base case
    if bags_num[bag_colour] == []:
        return 1
    count = 1
    for idx in range(len(bags_num[bag_colour])):
        count += bags_num[bag_colour][idx] * num_bags(bags[bag_colour][idx])
    return count


tot_bags = num_bags("shiny gold")
print(tot_bags-1)