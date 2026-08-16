from time import time
t1 = time()
from math import prod
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 06 2025.txt"
# FILE_NAME = "Day 06 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data: list[str] = [x.replace("\n", "") for x in file.readlines()]
file.close()

def getResult(lst: list[str]) -> int:
    operator = lst[-1].strip()
    lst = lst[:-1]
    nums: list[int] = []
    longest = max(len(num) for num in lst)
    for i in range(longest):
        nums.append(int("".join([row[i] for row in lst if row[i] != " "])))
    return sum(nums) if operator == "+" else prod(nums)


indexesToSplit: list[int] = []
for i in range(len(data[-1])):
    if data[-1][i] != " ": indexesToSplit.append(i)
indexesToSplit.append(len(data[-1])+1)
lsts: list[list[str]] = []
for i1, i2 in zip(indexesToSplit[:-1], indexesToSplit[1:]):
    lsts.append([data[row][i1:i2-1] for row in range(len(data))])


print(sum(getResult(nums) for nums in lsts))

print(f"Time Taken: {time()-t1:.3f}s")