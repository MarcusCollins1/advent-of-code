input_file = open("Day 8 2020.txt")
input_file = open("Day 8 2020 alt.txt")
boot = []
for line in input_file:
    if line[-1] == "\n":
        boot.append(line[:-1])
    else:
        boot.append(line)


visited = set()
count = 0
accumulator = 0
while count not in visited:
    visited.add(count)
    print(boot[count][:3])
    if boot[count][:3] == "acc":
        curr_num = int(boot[count][4:])
        accumulator += curr_num
        count += 1
    
    elif boot[count][:3] == "jmp":
        curr_num = int(boot[count][4:])
        count += curr_num

    elif boot[count][:3] == "nop":
        count += 1
    
    
print(accumulator)
