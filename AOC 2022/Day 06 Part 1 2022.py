FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 6 2022.txt"
# FILE_NAME = "Day 6 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

for i in range(len(data)-3):
    if len(set(data[i:i+3])) == 4:
        print(i+14)
        break