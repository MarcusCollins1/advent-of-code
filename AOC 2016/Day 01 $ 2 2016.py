FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 1 2016.txt"
FILE_NAME = "Day 1 2016 alt.txt"

file = open(FOLDER_PATH+FILE_NAME, "r")
input_str = file.read().strip()
file.close()
directions = input_str.split(", ")
x = 0
y = 0
num_dir = {0:"north", 1:"east", 2:"south", 3:"west"}
face = 0
visited = set()
flag = False
for dir in directions:
    if dir[0] == "R":
        face = (face+1) % 4
    else:
        face = (face-1) % 4
    for i in range(int(dir[1:])):
        if face == 0:
            y += 1
        elif face == 2:
            y -= 1
        elif face == 1:
            x += 1
        elif face == 3:
            x -= 1
        curr_pos = (x, y)
        if curr_pos in visited:
            print(abs(x)+abs(y))
            flag = True
            break
        visited.add(curr_pos)
    if flag:
        break