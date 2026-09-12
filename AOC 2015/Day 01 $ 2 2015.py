FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 01 2015.txt"
# FILE_NAME = "Day 01 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

data = data[0]

floor = 0
for i, symbol in enumerate(data):
    floor += 1 if symbol == "(" else -1
    if floor == -1:
        print(i+1)
        break