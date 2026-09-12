# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 8 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 8 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 8 2021 test.txt", "r")
file = input_file.read().splitlines()
total = 0
for line in file:
    curr = line.split(" | ")[1].split()
    for num in curr:
        length = len(num)
        total += (length == 2 or length == 3 or length == 4 or length == 7)
print(total)