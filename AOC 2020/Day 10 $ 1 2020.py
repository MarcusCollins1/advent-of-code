input_file = open("Day 10 2020.txt")
input_file = open("Day 10 2020 alt.txt")
jolts = []
for line in input_file:
    if line[-1] == "\n":
        jolts.append(int(line[:-1]))
    else:
        jolts.append(int(line))


jolts = sorted(jolts)
jolts.append(jolts[-1] + 3)
curr_jolt = 0
ones_count = 0
threes_count = 0
for i in jolts:
    if i - curr_jolt == 1:
        ones_count += 1
    elif i - curr_jolt == 3:
        threes_count += 1
    curr_jolt = i
print(ones_count*threes_count)
