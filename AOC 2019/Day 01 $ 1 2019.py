input_file = open("Day 1 2019.txt")
masses = []
for line in input_file:
    if line[-1] == "\n":
        masses.append(line[:-1])
    else:
        masses.append(line)
#print(masses)
total = 0
for i in masses:
    curr_fuel = int(i)//3
    curr_fuel -= 2
    total += curr_fuel
input_file.close()
print(total)