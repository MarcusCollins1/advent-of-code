FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 9 2022.txt"
FILE_NAME = "Day 9 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()


visited = set()
head_pos_x, head_pos_y = 0, 0
tail_pos_x, tail_pos_y = 0, 0

def Move_Tail():
    global head_pos_x, head_pos_y, tail_pos_x, tail_pos_y
    if head_pos_y-tail_pos_y >= 2:
        tail_pos_y = head_pos_y - 1
        tail_pos_x = head_pos_x
    elif tail_pos_y-head_pos_y >= 2:
        tail_pos_y = head_pos_y + 1
        tail_pos_x = head_pos_x
    elif head_pos_x-tail_pos_x >= 2:
        tail_pos_x = head_pos_x - 1
        tail_pos_y = head_pos_y
    elif tail_pos_x-head_pos_x >= 2:
        tail_pos_x = head_pos_x + 1
        tail_pos_y = head_pos_y
    visited.add((tail_pos_x, tail_pos_y))

def Up():
    global head_pos_x, head_pos_y, tail_pos_x, tail_pos_y
    head_pos_y += 1
    Move_Tail()

def Down():
    global head_pos_x, head_pos_y, tail_pos_x, tail_pos_y
    head_pos_y -= 1
    Move_Tail()

def Left():
    global head_pos_x, head_pos_y, tail_pos_x, tail_pos_y
    head_pos_x -= 1
    Move_Tail()

def Right():
    global head_pos_x, head_pos_y, tail_pos_x, tail_pos_y
    head_pos_x += 1
    Move_Tail()

LETTER_FUNC = {"U":Up, "D":Down, "L":Left, "R":Right}

for line in data:
    line = line.replace("\n", "").split()
    for _ in range(int(line[1])):
        LETTER_FUNC[line[0]]()

print(len(visited))
