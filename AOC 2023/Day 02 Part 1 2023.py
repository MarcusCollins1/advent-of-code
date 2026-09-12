FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 02 2023.txt"
# FILE_NAME = "Day 02 2023 alt.txt"
# FILE_NAME = "Day 02 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

MAX_REDS = 12
MAX_GREENS = 13
MAX_BLUES = 14

games = []
for line in data:
    line = line.split(": ")[1]
    line = line.split("; ")
    curr = []
    for cubes in line:
        curr.append(cubes.split(", "))
    games.append(curr)

total = 0

for i, game in enumerate(games):
    possible = True
    for subset in game:
        for cube in subset:
            if "red" in cube:
                if int(cube.replace(" red", "")) > MAX_REDS:
                    possible = False
                    break
            elif "green" in cube:
                if int(cube.replace(" green", "")) > MAX_GREENS:
                    possible = False
                    break
            elif "blue" in cube:
                if int(cube.replace(" blue", "")) > MAX_BLUES:
                    possible = False
                    break

    total += i+1 if possible else 0
print(total)