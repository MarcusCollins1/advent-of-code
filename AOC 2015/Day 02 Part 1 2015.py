FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 02 2015.txt"
# FILE_NAME = "Day 02 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

total = 0
for line in data:
    l, w, h = list(map(int, line.strip().split("x")))
    faces = [l*w, l*h, w*h]
    total += 2*(sum(faces))+min(faces)
print(total)