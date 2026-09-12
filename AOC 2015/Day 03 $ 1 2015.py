FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 03 2015.txt"
# FILE_NAME = "Day 03 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

dict = {"<":(-1, 0), ">":(1, 0), "^":(0, -1), "v":(0, 1)}
data = data[0]

locations = {(0, 0)}
curr_location = (0, 0)
for instruction in data:
    curr_location = tuple(map(sum, zip(dict[instruction], curr_location)))
    locations.add(curr_location)
print(len(locations))