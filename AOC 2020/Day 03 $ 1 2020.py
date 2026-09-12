# input_file = open("Day 3 2020.txt")
input_file = open("Day 3 2020 alt.txt")

trees = []
for line in input_file:
    curr_list = []
    if line[-1] == "\n":
        for i in line[:-1:]:
            curr_list.append(i)
    else:
        for i in line:
            curr_list.append(i)
    trees.append(curr_list)
#print(trees)

curr_row = 0
curr_col = 0
total = 0
while curr_row < len(trees):
    if trees[curr_row][curr_col] == "#":
        total += 1
    curr_row += 1
    if curr_col + 3 >= len(trees[0]):
        curr_col = 3-(len(trees[0])-curr_col)
    else:
        curr_col += 3
print(total)