FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 14 2022.txt"
FILE_NAME = "Day 14 2022 alt.txt"
FILE_NAME = "Day 14 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()


rockPoses = set()
for line in data:
    line = line.strip().split(" -> ")
    for i in range(len(line)-1):
        first, second = list(map(int, line[i].split(","))), list(map(int, line[i+1].split(",")))
        for x in range(min([first[0], second[0]]), max([first[0], second[0]])+1):
            for y in range(min([first[1], second[1]]), max([first[1], second[1]])+1):
                rockPoses.add((x, y))

lowest_y = 0
for rock_pos in rockPoses:
    lowest_y = max([lowest_y, rock_pos[1]])

sand_start_pos = (500, 0)
sand_pos = sand_start_pos
num_sand = 0

while sand_pos[1] < lowest_y:
    # try moving down
    if (sand_pos[0], sand_pos[1]+1) not in rockPoses:
        sand_pos = (sand_pos[0], sand_pos[1]+1)
    # try moving left down
    elif (sand_pos[0]-1, sand_pos[1]+1) not in rockPoses:
        sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
    # try moving right down
    elif (sand_pos[0]+1, sand_pos[1]+1) not in rockPoses:
        sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
    else:
        rockPoses.add(sand_pos)
        num_sand += 1
        sand_pos = sand_start_pos

print(num_sand)
