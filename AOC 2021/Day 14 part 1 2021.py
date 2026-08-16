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
instructions = defaultdict(str)
for line in x:
    instructions[line.split(" -> ")[0]] = line.split(" -> ")[1]

for _ in range(10):
    curr = ""
    for idx in range(len(polymer)-1):
        curr += polymer[idx]
        curr += instructions[polymer[idx]+polymer[idx+1]]
    curr += polymer[idx+1]
    polymer = curr
print(Counter(polymer).most_common()[0][1]-Counter(polymer).most_common()[-1][1])