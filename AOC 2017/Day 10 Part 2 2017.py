from functools import reduce
from operator import xor

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 10 2017.txt"
# FILE_NAME = "Day 10 2017 alt.txt"
# FILE_NAME = "Day 10 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()
# data = ""


nums = list(range(256))
currentPos = 0
skipSize = 0
lengths = [ord(char) for char in data] + [17, 31, 73, 47, 23]

def reverseSublist(lst: list[int], start: int, length: int) -> list[int]:
    n = len(lst)
    if length <= 1: return lst
    vals = [lst[(start+i)%n] for i in range(length)]
    vals.reverse()
    for i, v in enumerate(vals):
        lst[(start + i) % n] = v
    return lst

def to2DigitHex(num: int) -> str:
    return hex(num)[2:] if num > 15 else f"0{hex(num)[2:]}"

for _ in range(64):
    for length in lengths:
        nums = reverseSublist(nums, currentPos, length)
        currentPos = (currentPos + length + skipSize) % len(nums)
        skipSize += 1

denseHash = [reduce(xor, [nums[i*16 + j] for j in range(16)]) for i in range(16)]
print("".join([to2DigitHex(num) for num in denseHash]))