from copy import deepcopy
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 15 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 15 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 15 2021 test.txt", "r")
def add(lst, num):
    for idx in range(len(lst)):
        for _ in range(num):
            if lst[idx] == 9:
                lst[idx] = 0
            lst[idx] += 1
    return lst
file = list(input_file.read().splitlines())
file1 = []
for line in file:
    file1.append(list(map(int, list(line))))
data = []
for j in range(5):
    for line in file1:
        curr = []
        for i in range(5):
            curr += add(deepcopy(line), i+j)  
        data.append(curr)
data[0][0] = 0
shortest_paths = []
for i in range(len(data)):
    curr = []
    for j in range(len(data[i])):
        curr.append(float("inf"))
    shortest_paths.append(curr)
shortest_paths[0][0] = 0

changed = True
while changed:
    changed = False
    for y in range(len(shortest_paths)):
        for x in range(len(shortest_paths[y])):
            pos = []
            if x > 0:
                pos.append(shortest_paths[y][x-1])
            if x < len(shortest_paths[y])-1:
                pos.append(shortest_paths[y][x+1])
            if y > 0:
                pos.append(shortest_paths[y-1][x])
            if y < len(shortest_paths)-1:
                pos.append(shortest_paths[y+1][x])
            curr = data[y][x]
            curr_min = float("inf")
            for i in pos:
                curr_min = min([curr_min, i])
            z = shortest_paths[y][x]
            shortest_paths[y][x] = min([shortest_paths[y][x], (curr_min + curr)])
            if z != shortest_paths[y][x]:
                changed = True
    print(f"Current shortest path to end: {shortest_paths[-1][-1]}")
print(f"Shortest path to end: {shortest_paths[-1][-1]}")
            