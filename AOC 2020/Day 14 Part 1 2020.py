input_file = open("Day 14 2020.txt")
input_file = open("Day 14 2020 alt.txt")
lines = []
for line in input_file:
    if line[-1] == "\n":
        lines.append(line[:-1])
    else:
        lines.append(line)

def through_mask(mask, value):
    binary_val = str(bin(value))
    binary_val = binary_val[2:]
    while len(binary_val) != 36:
        binary_val = "0"+binary_val
    binary_val_list = list(binary_val)
    for i in range(len(binary_val)):
        if mask[i] == "1":
            binary_val_list[i] = "1"
        elif mask[i] == "0":
            binary_val_list[i] = "0"
    binary_val = "".join(binary_val_list)
    return int(binary_val,2)

mem = dict()

for i in lines:
    if i[1] == "e":
        curr_pos = int(i[4:i.index("]")])
        curr_val = through_mask(mask, int(i[i.index("=")+2:]))
        mem[curr_pos] = curr_val
        
    else:
        mask = i[7:]
total = 0
for i in mem:
    total += mem[i]
print(total)