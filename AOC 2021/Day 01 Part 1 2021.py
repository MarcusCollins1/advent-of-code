# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 1 2021.txt", "r")
# home account
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 1 2021 alt.txt", "r")

depths = input_file.readlines()
depths = list(map(int, depths))

total = 0
for i in range(len(depths)-1):
    total += (depths[i] < depths[i+1])
print(total)