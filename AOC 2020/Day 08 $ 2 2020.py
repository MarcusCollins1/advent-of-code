input_file = open("Day 8 2020.txt")
input_file = open("Day 8 2020 alt.txt")
boot = []
for line in input_file:
    if line[-1] == "\n":
        boot.append(line[:-1])
    else:
        boot.append(line)

#x = boot
#print(x)
#print(boot)


found = False
change = 0
while not found:
    temp_boot = boot
    if change != 0:
        if temp_boot[change-1][:3] == "jmp":
            curr_str = "nop " + temp_boot[change-1][4:]
            #print(curr_str)
            temp_boot.pop(change-1)
            temp_boot.insert(change-1, curr_str)
            #print(temp_boot[change-1])
        elif temp_boot[change-1][:3] == "nop":
            curr_str = "jmp " + temp_boot[change-1][4:]
            #print(curr_str)
            temp_boot.pop(change-1)
            temp_boot.insert(change-1, curr_str)
            #print(temp_boot[change-1])

    if temp_boot[change][:3] == "jmp":
        curr_str = "nop " + temp_boot[change][4:]
        #print(curr_str)
        temp_boot.pop(change)
        temp_boot.insert(change, curr_str)
        #print(temp_boot[change])

    elif temp_boot[change][:3] == "nop":
        curr_str = "jmp " + temp_boot[change][4:]
        #print(curr_str)
        temp_boot.pop(change)
        temp_boot.insert(change, curr_str)
        #print(temp_boot[change])
    


    visited = set()
    count = 0
    accumulator = 0
    while count not in visited:
        visited.add(count)
        
        if temp_boot[count][:3] == "acc":
            curr_num = int(temp_boot[count][4:])
            accumulator += curr_num
            count += 1
        
        elif temp_boot[count][:3] == "jmp":
            curr_num = int(temp_boot[count][4:])
            count += curr_num

        elif temp_boot[count][:3] == "nop":
            count += 1
        if count >= len(temp_boot):
            found = True
            print("Found")
            break
    change += 1
    if change >= len(temp_boot):
        print("Too high")
        break
    
    
print(accumulator)