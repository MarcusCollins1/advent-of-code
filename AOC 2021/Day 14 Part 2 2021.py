from copy import deepcopy
from collections import Counter, defaultdict
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 14 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 14 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 14 2021 test.txt", "r")
file = input_file.read().splitlines()
polymer, x = file[0], file[2:]
start, end = polymer[0], polymer[-1]
instructions = defaultdict(str)
for line in x:
    instructions[line.split(" -> ")[0]] = line.split(" -> ")[1]
pairs = defaultdict(int)
for idx in range(len(polymer)-1):
    pairs[polymer[idx]+polymer[idx+1]] += 1

for _ in range(40):
    curr = defaultdict(int)
    for pair, num in pairs.items():
        new = pair[0] + instructions[pair[0] + pair[1]] + pair[1]
        for idx in range(len(new)-1):
            curr[new[idx]+new[idx+1]] += num
    pairs = deepcopy(curr)

#pairs = {"AB":1, "BA":1}
#polymer = "ABA"
#start, end = polymer[0], polymer[-1]

appears = defaultdict(int)
for pair, num in pairs.items():
    appears[pair[0]] += num/2
    appears[pair[1]] += num/2
appears[start] += 0.5
appears[end] += 0.5
print(int(appears[max(appears, key=appears.get)] - appears[min(appears, key=appears.get)]))
