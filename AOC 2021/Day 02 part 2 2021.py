# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 2 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 2 2021 alt.txt", "r")

instructions = input_file.readlines()

forward = 0
depth = 0
aim = 0
for i in instructions:
    instruction, num = i.split()
    num = int(num)
    if instruction == "forward":
        forward += num
        depth += aim*num
    elif instruction == "down":
        aim += num
    else:
        aim -= num
print(depth*forward)