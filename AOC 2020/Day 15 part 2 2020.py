from collections import defaultdict
input_file = open("Day 15 2020.txt")
input_file = open("Day 15 2020 alt.txt")
start_nums = list(map(int, input_file.read().strip().split(",")))
said = defaultdict(int)
for i in range(len(start_nums)):
    said[start_nums[i]] = i + 1

last_num = start_nums[-1]


for i in range(len(start_nums), 30000001):
    if last_num in said:
        saying = i-said[last_num]
    else:
        saying = 0

    said[last_num] = i
    #print(last_num)
    x = last_num
    last_num = saying
            
print(x)
