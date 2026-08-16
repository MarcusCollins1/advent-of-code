from tkinter import *
from time import sleep
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 9 2022.txt"
FILE_NAME = "Day 9 2022 alt.txt"
# FILE_NAME = "Day 9 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()


visited = set()
poses = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def Offset():
    global poses
    x_offset, y_offset = min(poses, key=lambda x: x[0])[0], min(poses, key=lambda x: x[1])[1]
    return x_offset, y_offset

def Display():
    global poses, lines, window
    x_offset, y_offset = Offset()
    count = 0
    for y in range(10):
        y += y_offset
        curr_line = ""
        for x in range(10):
            x += x_offset
            if [x, y] in poses:
                curr_line += str(poses.index([x, y]))
            else:
                curr_line += "x"
        lines[count]["text"] = curr_line
        count += 1
    window.update()

def Move_Tail():
    global poses
    for i in range(1, len(poses)):
        # head 2 above and 2 right
        if poses[i-1][1]-poses[i][1] >= 2 and poses[i-1][0]-poses[i][0] >= 2:
            poses[i][0] = poses[i-1][0]-1
            poses[i][1] = poses[i-1][1]-1
        # head 2 above and 2 left
        if poses[i-1][1]-poses[i][1] >= 2 and poses[i][0]-poses[i-1][0] >= 2:
            poses[i][0] = poses[i-1][0]-1
            poses[i][1] = poses[i-1][1]+1
        # head 2 below and 2 right
        if poses[i][1]-poses[i-1][1] >= 2 and poses[i-1][0]-poses[i][0] >= 2:
            poses[i][0] = poses[i-1][0]+1
            poses[i][1] = poses[i-1][1]-1
        # head 2 below and 2 left
        if poses[i][1]-poses[i-1][1] >= 2 and poses[i][0]-poses[i-1][0] >= 2:
            poses[i][0] = poses[i-1][0]+1
            poses[i][1] = poses[i-1][1]+1
        # head 2 above
        if poses[i-1][1]-poses[i][1] >= 2:
            poses[i][1] = poses[i-1][1] - 1
            poses[i][0] = poses[i-1][0]
        # head 2 below
        elif poses[i][1]-poses[i-1][1] >= 2:
            poses[i][1] = poses[i-1][1] + 1
            poses[i][0] = poses[i-1][0]
        # head 2 right
        elif poses[i-1][0]-poses[i][0] >= 2:
            poses[i][0] = poses[i-1][0] - 1
            poses[i][1] = poses[i-1][1]
        # head 2 left
        elif poses[i][0]-poses[i-1][0] >= 2:
            poses[i][0] = poses[i-1][0] + 1
            poses[i][1] = poses[i-1][1]
    visited.add(tuple(poses[-1]))
    # sleep(0.1)
    Display()
    

def Up():
    global poses
    poses[0][1] += 1
    Move_Tail()

def Down():
    global poses
    poses[0][1] -= 1
    Move_Tail()

def Left():
    global poses
    poses[0][0] -= 1
    Move_Tail()

def Right():
    global poses
    poses[0][0] += 1
    Move_Tail()

LETTER_FUNC = {"U":Up, "D":Down, "L":Left, "R":Right}



def Go(*args):
    Display()
    for line in data:
        line = line.replace("\n", "").split()
        # print(line)
        for _ in range(int(line[1])):
            LETTER_FUNC[line[0]]()

    print(len(visited))

# TKINTER
window = Tk()

button = Button(window)
button.bind("<Button-1>", Go)
button.pack(anchor="w")
lines = []
for _ in range(10):
    lines.append(Label(window))
for line in lines:
    line.pack(anchor="w")
window.mainloop()
################