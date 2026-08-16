input_file = open("AOC 2018 Day 1.txt", "r")
frequency_list = []
for line in input_file:
    frequency_list.append(int(line))
total = 0
for i in frequency_list:
    total += i
print(total)