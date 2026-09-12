FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 8 2022.txt"
FILE_NAME = "Day 8 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

trees = []
for line in data:
    line = line.strip()
    trees.append(list(map(int, list(line))))

best_score = 0
for row in range(len(trees)):
    for col in range(len(trees[row])):
        curr = trees[row][col]
        curr_score = 1
        # check down
        if row < len(trees)-1:
            for row1 in range(row+1, len(trees)):
                if curr <= trees[row1][col]:
                    break
            curr_score *= row1-row
        else:
            curr_score = 0
        # check up
        if row > 0:
            for row1 in range(row-1, -1, -1):
                if curr <= trees[row1][col]:
                    break
            curr_score *= row-row1
        else:
            curr_score = 0
        # check right
        if col < len(trees[row])-1:
            for col1 in range(col+1, len(trees[row])):
                if curr <= trees[row][col1]:
                    break
            curr_score *= col1-col
        else:
            curr_score = 0
        # check left
        if col > 0:
            for col1 in range(col-1, -1, -1):
                if curr <= trees[row][col1]:
                    break
            curr_score *= col-col1
        else:
            curr_score = 0
        if curr_score > best_score:
            best_score = curr_score
            best_pos = [col, row]
print(best_score)