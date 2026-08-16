FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 8 2016.txt"
# FILE_NAME = "Day 8 2016 alt.txt"
# FILE_NAME = "Day 8 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

screen = [["." for _ in range(50)] for __ in range(6)]
# screen = [["." for _ in range(7)] for __ in range(3)]

def Rect(width:int, height:int, screen:list) -> list:
    for i in range(height):
        for j in range(width):
            screen[i][j] = "#"
    return screen

def RotateRow(row:int, n:int, screen:list) -> list:
    row_to_rotate = screen[row]
    row_to_rotate = row_to_rotate[-n:]+row_to_rotate[:-n]
    screen[row] = row_to_rotate
    return screen

def RotateCol(col:int, n:int, screen:list) -> list:
    col_to_rotate = []
    for line in screen:
        col_to_rotate.append(line[col])
    col_to_rotate = col_to_rotate[-n:]+col_to_rotate[:-n]
    for i in range(len(screen)):
        screen[i][col] = col_to_rotate[i]
    return screen

for line in data:
    if line[:4] == "rect":
        line = line.replace("rect ", "").split("x")
        screen = Rect(int(line[0]), int(line[1]), screen)
    elif line[:10] == "rotate row":
        line = line.replace("rotate row y=", "").split(" by ")
        RotateRow(int(line[0]), int(line[1]), screen)
    elif line[:13] == "rotate column":
        line = line.replace("rotate column x=", "").split(" by ")
        RotateCol(int(line[0]), int(line[1]), screen)

total = 0
for line in screen:
    total += line.count("#")
    print(*line)
print(total)