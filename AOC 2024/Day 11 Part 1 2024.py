from time import time
from functools import cache
startTime = time()
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 11 2024.txt"
# FILE_NAME = "Day 11 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
stones: list[int] = [int(x.strip()) for x in file.read().split()]
file.close()

@cache
def blink(num: int, blinksLeft: int) -> int:
    if blinksLeft == 0: return 1
    elif num == 0:
        return blink(1, blinksLeft-1)
    elif len(str(num))%2 == 0:
        return blink(int(str(num)[:len(str(num))//2]), blinksLeft-1) + blink(int(str(num)[len(str(num))//2:]), blinksLeft-1)
    else:
        return blink(num*2024, blinksLeft-1)

print(sum([blink(stone, 25) for stone in stones]))