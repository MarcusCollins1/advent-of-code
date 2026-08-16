FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 10 2015.txt"
FILE_NAME = "Day 10 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

value = data[0]

for _ in range(40):
    new = ""
    curr_digit, curr_count = "", 0
    for digit in value:
        if digit == curr_digit:
            curr_count += 1
        else:
            if curr_digit != "":
                new += str(curr_count)+curr_digit
            curr_digit = digit
            curr_count = 1
    new += str(curr_count)+curr_digit
    value = new
print(len(value))