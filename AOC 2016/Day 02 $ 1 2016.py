FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 2 2016.txt"
FILE_NAME = "Day 2 2016 alt.txt"
input_file = open(FOLDER_PATH+FILE_NAME, "r")
lines = []
for row in input_file:
    if row[-1] == "\n":
        lines.append(row[:-1])
    else:
        lines.append(row)
input_file.close()
pass_code = []
curr_num = 5
for i in lines:
    for j in i:
        if j == "L":
            if curr_num % 3 != 1:
                curr_num -= 1
        elif j == "R":
            if curr_num % 3 != 0:
                curr_num += 1
        elif j == "U":
            if curr_num > 3:
                curr_num -= 3
        else:
            if curr_num < 7:
                curr_num += 3
    pass_code.append(curr_num)
print(*pass_code, sep="")