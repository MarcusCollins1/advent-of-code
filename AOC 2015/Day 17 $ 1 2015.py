from itertools import combinations
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 17 2015.txt"
# FILE_NAME = "Day 17 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

containers = list(map(int, data))
TARGET = 150
# TARGET = 25

count = sum(
    1
    for n in range(1,len(containers)+1)
    for c in combinations(containers,n)
    if sum(c) == TARGET
)
print(count)