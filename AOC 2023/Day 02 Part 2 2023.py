FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 02 2023.txt"
# FILE_NAME = "Day 02 2023 alt.txt"
# FILE_NAME = "Day 02 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

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
    min_red, min_green, min_blue = 0, 0, 0
    for subset in game:
        for cube in subset:
            if "red" in cube:
                if int(cube.replace(" red", "")) > min_red:
                    min_red = int(cube.replace(" red", ""))
            elif "green" in cube:
                if int(cube.replace(" green", "")) > min_green:
                    min_green = int(cube.replace(" green", ""))
            elif "blue" in cube:
                if int(cube.replace(" blue", "")) > min_blue:
                    min_blue = int(cube.replace(" blue", ""))

    total += min_red*min_green*min_blue
print(total)