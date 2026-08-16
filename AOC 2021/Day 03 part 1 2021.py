from collections import Counter
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
gamma = ""
epsilon = ""

for i in nums:
    for j in range(len(i)):
        columns[j] += i[j]

for column in columns:
    gamma += Counter(column).most_common(1)[0][0]
    epsilon += Counter(column).most_common()[-1][0]

total = 1
for num in [list(gamma), list(epsilon)]:
    val = 0
    for i in range(len(num)):
        digit = num.pop()
        if digit == "1":
            val += 2**i
    total *= val
print(total)