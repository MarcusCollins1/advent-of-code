FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 12 2015.txt"
# FILE_NAME = "Day 12 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

data = data[0]

total = 0
curr = ""
for letter in data:
    if letter in "-1234567890":
        curr += letter
    elif curr != "":
        total += int(curr)
        curr = ""
print(total)