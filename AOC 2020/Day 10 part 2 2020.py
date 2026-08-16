from collections import defaultdict
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



ways = defaultdict(int)
ways[0] = 1
for i in jolts:
    ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
print(ways[jolts[-1]])