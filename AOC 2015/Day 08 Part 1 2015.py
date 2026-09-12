FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 08 2015.txt"
# FILE_NAME = "Day 08 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

code_length = str_length = 0
for line in data:
    line = line.strip()
    code_length += len(line)
    str_length += len(eval(line))
print(code_length-str_length)