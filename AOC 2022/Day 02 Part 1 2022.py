FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 2 2022.txt"
FILE_NAME = "Day 2 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

SCORES = {"AX":4, "AY":8, "AZ":3, "BX":1, "BY":5, "BZ":9, "CX":7, "CY":2, "CZ":6}

total = 0
for line in data:
    total += SCORES[line.strip().replace(" ", "")]
print(total)