# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 1 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 1 2021 alt.txt", "r")
# kyla's account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 1 2021 kyla.txt", "r")

depths = input_file.readlines()
depths = list(map(int, depths))
total = 0
depths1 = []
for i in range(len(depths)-2):
    depths1.append((depths[i] + depths[i+1] + depths[i+2]))
for i in range(len(depths1)-1):
    total += (depths1[i] < depths1[i+1])
print(total)