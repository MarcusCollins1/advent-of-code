# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 9 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 9 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 9 2021 test.txt", "r")
file = input_file.read().splitlines()
heights = []
for i in file:
    heights.append(list(map(int, list(i))))
total = 0
for row in range(len(heights)):
    for col in range(len(heights[row])):
        flag = True
        try:
            if heights[row][col] >= heights[row][col+1]:
                flag = False
        except:
            pass
        if col != 0:
            try:
                if heights[row][col] >= heights[row][col-1]:
                    flag = False
            except:
                pass
        try:
            if heights[row][col] >= heights[row+1][col]:
                flag = False
        except:
            pass
        if row != 0:
            try:
                if heights[row][col] >= heights[row-1][col]:
                    flag = False
            except:
                pass
        if flag:
            total += 1+heights[row][col]

print(total)