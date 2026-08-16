FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 18 2022.txt"
FILE_NAME = "Day 18 2022 alt.txt"
# FILE_NAME = "Day 18 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

AROUND = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
min_x = min_y = min_z = float("inf")
max_x = max_y = max_z = -float("inf")
positions = set()
for line in data:
    line = tuple(map(int, line.strip().split(",")))
    min_x, max_x = min([min_x, line[0]]), max([max_x, line[0]])
    min_y, max_y = min([min_y, line[1]]), max([max_y, line[1]])
    min_z, max_z = min([min_z, line[2]]), max([max_z, line[2]])
    positions.add(line)
def Add(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1], t1[2]+t2[2])

def Check(pos, curr_train):
    global positions, AROUND
    if pos[0] > max_x or pos[0] < min_x or pos[1] > max_y or pos[1] < min_y or pos[2] > max_z or pos[2] < min_z:
        return True
    for adj in AROUND:
        if Add(pos, adj) not in positions and Add(pos, adj) not in curr_train:
            curr_train.append(pos)
            return Check(Add(pos, adj), curr_train)
    return False


count = 0
for position in positions:
    for adj in AROUND:
        checking_pos = Add(position, adj)
        if checking_pos not in positions:
            count += 1 if Check(checking_pos, []) else 0
print(count)