from collections import defaultdict
from time import time
t1 = time()
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 12 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 12 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 12 2021 test.txt", "r")
file = input_file.read().splitlines()
tunnels = defaultdict(list)
for line in file:
    curr1, curr2 = line.split("-")
    tunnels[curr1].append(curr2)
    tunnels[curr2].append(curr1)

pos = []
queue = [["start"]]
while len(queue) != 0:
    curr = queue.pop(0)
    curr_pos = curr[-1]
    for i in tunnels[curr_pos]:
        if i == "end":
            pos.append(curr+["end"])
        elif i.upper() == i:
            queue.append(curr+[i])
        elif i not in curr:
            queue.append(curr+[i])
print(len(pos))
print(f"This took: {(time()-t1):.3f} secs")