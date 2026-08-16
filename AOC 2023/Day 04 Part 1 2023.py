FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 4 2023.txt"
# FILE_NAME = "Day 4 2023 alt.txt"
# FILE_NAME = "Day 4 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

total = 0
for line in data:
    line = line.split(": ")[1].split(" | ")
    line = [list(map(int, x.split())) for x in line]
    length = len(set(line[0]).intersection(set(line[1])))-1
    total += 2**length if length >= 0 else 0
print(total)