FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 6 2019.txt"
FILE_NAME = "Day 6 2019 alt.txt"
# FILE_NAME = "Day 6 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

orbits = dict()
for line in data:
    line = line.strip().split(")")
    orbits[line[1]] = line[0]

total = 0
for key in orbits.keys():
    while True:
        try:
            key = orbits[key]
            total += 1
        except:
            break
print(total)