FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 02 2024.txt"
# FILE_NAME = "Day 02 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(map(int, x.strip().split())) for x in file.readlines()]
file.close()

def IsSafe(nums: list[int]) -> bool:
    differences = [num2-num1 for num1, num2 in zip(nums[:-1], nums[1:])]
    isPositive = [x > 0 for x in differences]
    if not(all(isPositive) or not any(isPositive)):
        return False
    inRange = [1 <= abs(x) <= 3 for x in differences]
    if not all(inRange):
        return False
    return True


numSafe = sum([IsSafe(report) for report in data])
print(numSafe)