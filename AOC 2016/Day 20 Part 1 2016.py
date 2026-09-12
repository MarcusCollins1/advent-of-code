FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 20 2016.txt"
# FILE_NAME = "Day 20 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

rangesBlocked: list[tuple[int, int]] = []

for line in data:
    num1, num2 = map(int, line.split("-"))
    rangesBlocked.append((num1, num2))

rangesBlocked.sort(key=lambda x: x[0])

merged: list[tuple[int, int]] = []
for start, end in rangesBlocked:
    if not merged:
        merged.append((start, end))
    else:
        prevStart, prevEnd = merged[-1]

        if start <= prevEnd + 1:
            merged[-1] = (prevStart, max(prevEnd, end))
        else:
            merged.append((start, end))

print(merged[0][1]+1)