from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 17 2017.txt"
# FILE_NAME = "Day 17 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
STEPS = int([x.strip() for x in file.readlines()][0])
file.close()

nums = [0]
idx = 0
for n in range(1, 2018):
    idx = (idx + STEPS) % len(nums) + 1
    nums = nums[:idx] + [n] + nums[idx:]

print(nums[nums.index(2017)+1])
print(f"Time Taken: {time()-t1:.2f}s")