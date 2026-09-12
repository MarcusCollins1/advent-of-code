FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 10 2017.txt"
# FILE_NAME = "Day 10 2017 alt.txt"
# FILE_NAME = "Day 10 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()


nums = list(range(5)) if FILE_NAME == "Day 10 2017 test.txt" else list(range(256))
currentPos = 0
skipSize = 0
lengths = list(map(int, data.split(",")))

def reverseSublist(lst: list[int], start: int, length: int) -> list[int]:
    n = len(lst)
    if length <= 1: return lst
    vals = [lst[(start+i)%n] for i in range(length)]
    vals.reverse()
    for i, v in enumerate(vals):
        lst[(start + i) % n] = v
    return lst

for length in lengths:
    nums = reverseSublist(nums, currentPos, length)
    currentPos = (currentPos + length + skipSize) % len(nums)
    skipSize += 1

print(nums[0] * nums[1])