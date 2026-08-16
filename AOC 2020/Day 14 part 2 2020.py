input_file = open("Day 14 2020.txt")
input_file = open("Day 14 2020 alt.txt")
lines = []
for line in input_file:
    if line[-1] == "\n":
        lines.append(line[:-1])
    else:
        lines.append(line)

def through_mask(mask, value):
    val_list = [0]
    binary_val = str(bin(value))
    binary_val = binary_val[2:]
    while len(binary_val) != 36:
        binary_val = "0"+binary_val
    binary_val_list = list(binary_val)
    
    for i in range(len(mask)):
        temp_list = []
        index = -i -1
        if mask[index] == "0":
            for num in val_list:
                temp_list.append(int(binary_val_list[index]) * (2**i) + num)
        elif mask[index] =="1":
            for num in val_list:
                temp_list.append((2**i) + num)
        
        elif mask[index] =="X":
            for num in val_list:
                temp_list.append(num)
                temp_list.append((2**i) + num)

        val_list = list(temp_list)

    return val_list
'''
mask = "000000000000000000000000000000X1001X"
print(through_mask(mask,42))

'''
mem = dict()

for i in lines:
    if i[1] == "e":
        curr_pos = through_mask(mask, int(i[4:i.index("]")]))
        curr_val = int(i[i.index("=")+2:])
        for position in curr_pos:
            mem[position] = curr_val
        
    else:
        mask = i[7:]

#print(mem)
print(sum(mem.values()))
