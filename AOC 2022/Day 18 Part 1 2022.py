FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 18 2022.txt"
# FILE_NAME = "Day 18 2022 alt.txt"
# FILE_NAME = "Day 18 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

AROUND = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def Add(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1], t1[2]+t2[2])

positions = set()
for line in data:
    line = tuple(map(int, line.strip().split(",")))
    positions.add(line)

count = 0
for position in positions:
    for adj in AROUND:
        count += 0 if Add(position, adj) in positions else 1
print(count)