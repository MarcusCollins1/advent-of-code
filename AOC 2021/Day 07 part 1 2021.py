# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 7 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 7 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 7 2021 test.txt", "r")
file = sorted(list(map(int, input_file.readlines()[0].split(","))))
meet_pos = file[(len(file)-1)//2]

total = 0
for num in file:
    total += abs(num-meet_pos)
print(total)