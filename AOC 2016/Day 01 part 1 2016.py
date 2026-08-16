FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 1 2016.txt"
FILE_NAME = "Day 1 2016 alt.txt"

file = open(FOLDER_PATH+FILE_NAME, "r")
input_str = file.read().strip()
file.close()

directions = input_str.split(", ")
x = 0
y = 0
face = 1
for i in directions:
    if i[0] == "L":
        if face == 1:
            face = 4
        else:
            face -= 1
    if i[0] == "R":
        if face == 4:
            face = 1
        else:
            face += 1
    if face == 1:
        x += int(i[1:])
    elif face == 2:
        y += int(i[1:])
    elif face == 3:
        x -= int(i[1:])
    else:
        y -= int(i[1:])
print(abs(x) +abs(y))
