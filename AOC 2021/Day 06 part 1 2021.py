from copy import deepcopy
from collections import defaultdict
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 6 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 6 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 6 2021 test.txt", "r")
file = input_file.readlines()
file = list(map(int, file[0].split(",")))
NUM_DAYS = 80
fish = defaultdict(int)
for num in file:
    fish[num] += 1

for _ in range(NUM_DAYS):
    next_fish = defaultdict(int)
    next_fish[0] = fish[1]
    next_fish[1] = fish[2]
    next_fish[2] = fish[3]
    next_fish[3] = fish[4]
    next_fish[4] = fish[5]
    next_fish[5] = fish[6]
    next_fish[6] = fish[7] + fish[0]
    next_fish[7] = fish[8]
    next_fish[8] = fish[0]
    fish = deepcopy(next_fish)
print(sum(fish.values()))