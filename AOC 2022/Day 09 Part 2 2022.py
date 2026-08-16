FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 9 2022.txt"
# FILE_NAME = "Day 9 2022 alt.txt"
#FILE_NAME = "Advent 9 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

visited = set()
# DEBUG
num_knots = 10
tail_set_list = []
for i in range(num_knots):
    tail_set_list += [set()]


poses = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited.add((0, 0))
for i in range(num_knots):
    tail_set_list[i].add(tuple(poses[i]))


def Move_Tail():
    global poses

    # DEBUG
    tail_set_list[0].add(tuple(poses[0]))
    
    for i in range(1, len(poses)):

        # head 2 above and 2 right
        if poses[i-1][1]-poses[i][1] >= 2 and poses[i-1][0]-poses[i][0] >= 2:
            poses[i][0] = poses[i-1][0]-1
            poses[i][1] = poses[i-1][1]-1

        # head 2 above and 2 left
        elif poses[i-1][1]-poses[i][1] >= 2 and poses[i][0]-poses[i-1][0] >= 2:
            poses[i][0] = poses[i-1][0]+1
            poses[i][1] = poses[i-1][1]-1

        # head 2 below and 2 right
        elif poses[i][1]-poses[i-1][1] >= 2 and poses[i-1][0]-poses[i][0] >= 2:
            poses[i][0] = poses[i-1][0]-1
            poses[i][1] = poses[i-1][1]+1

        # head 2 below and 2 left
        elif poses[i][1]-poses[i-1][1] >= 2 and poses[i][0]-poses[i-1][0] >= 2:
            poses[i][0] = poses[i-1][0]+1
            poses[i][1] = poses[i-1][1]+1

        # head 2 above
        elif poses[i-1][1]-poses[i][1] >= 2:
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

        # DEBUG
        tail_set_list[i].add(tuple(poses[i]))

    visited.add(tuple(poses[-1]))


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

for line in data:
    line = line.replace("\n", "").split()
    # print(line)

    for _ in range(int(line[1])):
        LETTER_FUNC[line[0]]()

print(len(visited))
