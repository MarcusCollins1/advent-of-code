FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 3 2019.txt"
FILE_NAME = "Day 3 2019 alt.txt"
# FILE_NAME = "Day 3 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

LET_DIR = {"L":(-1, 0), "R":(1, 0), "U":(0, 1), "D":(0, -1)}

wire1, wire2 = data
wire1, wire2 = wire1.split(","), wire2.split(",")
wire1_pos, wire2_pos = set(), set()
curr_wire1, curr_wire2 = (0, 0), (0, 0)

for move in wire1:
    dir = LET_DIR[move[0]]
    for _ in range(int(move[1:])):
        curr_wire1  = tuple(map(sum,zip(curr_wire1, dir)))
        wire1_pos.add(curr_wire1)

for move in wire2:
    dir = LET_DIR[move[0]]
    for _ in range(int(move[1:])):
        curr_wire2 = tuple(map(sum,zip(curr_wire2, dir)))
        wire2_pos.add(curr_wire2)


min_dis = float("inf")

for pos in wire1_pos.intersection(wire2_pos):
    min_dis = min([min_dis, abs(pos[0])+abs(pos[1])])

print(min_dis)