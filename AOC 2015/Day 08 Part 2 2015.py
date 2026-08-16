FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 08 2015.txt"
FILE_NAME = "Day 08 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

extra = 0
for line in data:
    extra += 2
    extra += sum(map(line.count, ['"', '\\']))
print(extra)