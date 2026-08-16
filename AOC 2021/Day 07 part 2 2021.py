# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 7 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 7 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 7 2021 test.txt", "r")
file = sorted(list(map(int, input_file.readlines()[0].split(","))))

lowest_fuel = float("inf")
for meet_pos in range(min(file), max(file) + 1):
    total = 0
    for num in file:
        n = abs(num-meet_pos)
        total += (n**2 + n)/2
    lowest_fuel = min([lowest_fuel, total])
print(int(lowest_fuel))