FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 6 2019.txt"
# FILE_NAME = "Day 6 2019 alt.txt"
# FILE_NAME = "Day 6 2019 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

orbits = dict()
for line in data:
    line = line.strip().split(")")
    orbits[line[1]] = line[0]

def get_parents(node):
    path = set()
    while node in orbits:
        parent = orbits[node]
        path.add(parent)
        node = parent
    return path

YOU = get_parents("YOU")
SAN = get_parents("SAN")
print(len(YOU-SAN)+len(SAN-YOU))