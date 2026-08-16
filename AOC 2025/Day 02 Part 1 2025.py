FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 02 2025.txt"
# FILE_NAME = "Day 02 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0].split(",")
file.close()

data = [list(map(int, x.split("-"))) for x in data]

def isValid(num: int) -> bool:
    numstr = str(num)
    length = len(numstr)
    if length%2 == 1: return True
    part1, part2 = numstr[:length//2], numstr[length//2:]
    return not (part1==part2)

print(sum([i for x1,x2 in data for i in range(x1,x2+1) if not isValid(i)]))