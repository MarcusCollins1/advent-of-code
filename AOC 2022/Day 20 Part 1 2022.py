FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 20 2022.txt"
FILE_NAME = "Day 20 2022 alt.txt"
# FILE_NAME = "Day 20 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

POSITIONS = [1000, 2000, 3000]

nums = []
for line in data:
    nums.append([int(line.strip()), False])

def getCount():
    global nums
    count = 0
    while True:
        try:
            if not nums[count][1]:
                return count
        except:
            return None
        count += 1

def display():
    global nums
    new = []
    for num in nums:
        new.append(num[0])
    print(*new, sep=", ")

while True:
    # display()
    count = getCount()
    if count == None:
        break
    moving = nums[count]
    new_location = (count + moving[0])
    if new_location >= len(nums):
        new_location %= len(nums)
        new_location += 1
    if new_location == 0:
        new_location = len(nums)-1
    if count + moving[0] < 0 and new_location > count:
        nums.insert(new_location, [moving[0], True])
        nums.pop(count)
    else:
        nums.pop(count)
        nums.insert(new_location, [moving[0], True])

offset = nums.index([0, True])

total = 0
for pos in POSITIONS:
    total += nums[(pos+offset)%len(nums)][0]
    # print(nums[(pos+offset)%len(nums)][0])

print(total)