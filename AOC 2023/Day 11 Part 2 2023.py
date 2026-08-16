from itertools import combinations
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 11 2023.txt"
# FILE_NAME = "Day 11 2023 alt.txt"
# FILE_NAME = "Day 11 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

blank_cols, blank_rows = [], []
for i, line in enumerate(data):
    if list(set(line)) == ["."]:
        blank_rows.append(i)
for i in range(len(data[0])):
    col = [data[x][i] for x in range(len(data))]
    if list(set(col)) == ["."]:
        blank_cols.append(i)

poses = []
row_index, col_index = 0, 0
for i, row in enumerate(data):
    if i in blank_rows:
        row_index += 1000000
        continue
    for j, cell in enumerate(row):
        if j in blank_cols:
            col_index += 1000000
            continue
        if cell == "#":
            poses.append((row_index, col_index))
        col_index += 1
    col_index = 0
    row_index += 1

total = 0
for x1, x2 in combinations(poses, 2):
    total += abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
print(total)