from copy import deepcopy
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 3 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 3 2021 alt.txt", "r")
data = input_file.readlines()
nums = []
for i in data:
    if i[-1] == "\n":
        nums.append(i[:-1])
    else:
        nums.append(i)
LENGTH = len(nums[0])
columns = [""]*LENGTH
oxygen = ""
co2 = ""
co2_nums = deepcopy(nums)
def most_common(str):
    ones = str.count("1")
    zeros = str.count("0")
    if zeros > ones:
        return("0")
    else:
        return("1")
def least_common(str):
    ones = str.count("1")
    zeros = str.count("0")
    if zeros > ones:
        return("1")
    else:
        return("0")
def bin_den(str):
    str = list(str)
    val = 0
    for i in range(len(str)):
        digit = str.pop()
        if digit == "1":
            val += 2**i
    return val
for i in nums:
    for j in range(len(i)):
        columns[j] += i[j]
# ox num
flag = False
while True:
    pos = 0
    while True:
        keep = most_common(columns[pos])
        x = deepcopy(nums)
        for num in x:
            if num[pos] != keep:
                nums.remove(num)
        columns = [""]*LENGTH
        for i in nums:
            for j in range(len(i)):
                columns[j] += i[j]
        if len(nums) == 1:
            flag = True
            break
        pos += 1
    if flag:
        break
ox_num = bin_den(nums[0])
#print(ox_num)
# co2 nums
columns = [""]*LENGTH
for i in co2_nums:
    for j in range(len(i)):
        columns[j] += i[j]
while True:
    pos = 0
    while True:
        keep = least_common(columns[pos])
        x = deepcopy(co2_nums)
        for num in x:
            if num[pos] != keep:
                co2_nums.remove(num)
        columns = [""]*LENGTH
        for i in co2_nums:
            for j in range(len(i)):
                columns[j] += i[j]
        if len(co2_nums) == 1:
            flag = True
            break
        pos += 1
    if flag:
        break
co2_num = bin_den(co2_nums[0])
#print(co2_num)
print(co2_num*ox_num)