FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 8 2022.txt"
# FILE_NAME = "Day 8 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

trees = []
for line in data:
    line = line.strip()
    trees.append(list(map(int, list(line))))

count = 0

for row in range(len(trees)):
    for col in range(len(trees[row])):
        curr = trees[row][col]
        flag = False
        # check down
        flag1 = True
        for row1 in range(row+1, len(trees)):
            if curr <= trees[row1][col]:
                flag1 = False
                break
        flag = flag or flag1
        # check up
        if not flag:
            flag1 = True
            for row1 in range(0, row):
                if curr <= trees[row1][col]:
                    flag1 = False
                    break
            flag = flag or flag1
        # check right
        if not flag:
            flag1 = True
            for col1 in range(col+1, len(trees[row])):
                if curr <= trees[row][col1]:
                    flag1 = False
                    break
            flag = flag or flag1
        # check left
        if not flag:
            flag1 = True
            for col1 in range(0, col):
                if curr <= trees[row][col1]:
                    flag1 = False
                    break
            flag = flag or flag1
        count += 1 if flag else 0
print(count)
        