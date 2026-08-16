input_file = open("AOC 2018 Day 1.txt", "r")
frequency_list = []
for line in input_file:
    frequency_list.append(int(line))
total = 0
seen = set()
flag = False
count = 0
while not flag:
    if total not in seen:
        seen.add(total)
        total += frequency_list[count]
    else:
        flag = True
    if count < len(frequency_list)-1:
        count += 1
    else:
        count = 0
print(total)