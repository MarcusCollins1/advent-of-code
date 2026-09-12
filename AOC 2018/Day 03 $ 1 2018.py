from collections import defaultdict
input_file = open("AOC 2018 Day 3.txt", "r")
fabric_list = []
for line in input_file:
    if line[-1] == "\n":
        fabric_list.append(line[:-1])
    else:
        fabric_list.append(line)
#print(fabric_list)
#fabric_list = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

co_ordinates = defaultdict(int)

for i in fabric_list:
    curr_x = int(i[i.index("@")+1:i.index(",")])
    curr_y = int(i[i.index(",")+1:i.index(":")])
    length = int(i[i.index(":")+2:i.index("x")])
    height = int(i[i.index("x")+1:])
    for x in range(length):
        for y in range(height):
            curr_x_pos = x + curr_x
            curr_y_pos = y + curr_y
            curr_pos = (curr_x_pos, curr_y_pos)
            co_ordinates[curr_pos] += 1
            
overlaps = 0
for pos in co_ordinates:
    if co_ordinates[pos] >= 2:
        overlaps += 1

print(overlaps)