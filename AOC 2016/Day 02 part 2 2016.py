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
            if curr_num == 3:
                curr_num = 2
            elif curr_num == 4:
                curr_num = 3
            elif curr_num == 6:
                curr_num = 5
            elif curr_num == 7:
                curr_num = 6
            elif curr_num == 8:
                curr_num = 7
            elif curr_num == 9:
                curr_num = 8
            elif curr_num == 11:
                curr_num = 10
            elif curr_num == 12:
                curr_num = 11
        elif j == "R":
            if curr_num == 2:
                curr_num = 3
            elif curr_num == 3:
                curr_num = 4
            elif curr_num == 5:
                curr_num = 6
            elif curr_num == 6:
                curr_num = 7
            elif curr_num == 7:
                curr_num = 8
            elif curr_num == 8:
                curr_num = 9
            elif curr_num == 10:
                curr_num = 11
            elif curr_num == 11:
                curr_num = 12
        elif j == "U":
            if curr_num == 3:
                curr_num = 1
            elif curr_num == 6:
                curr_num = 2
            elif curr_num == 7:
                curr_num = 3
            elif curr_num == 8:
                curr_num = 4
            elif curr_num == 10:
                curr_num = 6
            elif curr_num == 11:
                curr_num = 7
            elif curr_num == 12:
                curr_num = 8
            elif curr_num == 13:
                curr_num = 11
                
        else:
            if curr_num == 1:
                curr_num = 3
            elif curr_num == 2:
                curr_num = 6
            elif curr_num == 3:
                curr_num = 7
            elif curr_num == 4:
                curr_num = 8
            elif curr_num == 6:
                curr_num = 10
            elif curr_num == 7:
                curr_num = 11
            elif curr_num == 8:
                curr_num = 12
            elif curr_num == 11:
                curr_num = 13
                
    if curr_num < 10:
        pass_code.append(curr_num)
    else:
        if curr_num == 10:
            pass_code.append("A")
        if curr_num == 11:
            pass_code.append("B")
        if curr_num == 12:
            pass_code.append("C")
        if curr_num == 13:
            pass_code.append("D")
print(*pass_code, sep="")