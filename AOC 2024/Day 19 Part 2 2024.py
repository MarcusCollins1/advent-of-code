from functools import cache
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 19 2024.txt"
# FILE_NAME = "Day 19 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
availablePatterns, designs = [x.strip() for x in file.read().split("\n\n")]
file.close()
availablePatterns = tuple(sorted(availablePatterns.split(", "), key=len, reverse=True))
designs = designs.splitlines()

@cache
def Consume(pattern: str, towels: tuple[str, ...]) -> int:
    tCounter = 0
    for towel in towels:
        if pattern == towel:
            tCounter += 1
        elif pattern.startswith(towel):
            tCounter += Consume(pattern[len(towel):], towels)
    return tCounter

total = 0
for design in designs:
    total += Consume(design, availablePatterns)
print(total)