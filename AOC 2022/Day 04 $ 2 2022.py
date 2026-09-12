FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 4 2022.txt"
# FILE_NAME = "Day 4 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

count = 0
for line in data:
    min1, max1, min2, max2 = list(map(int, line.strip().replace(",", "-").split("-")))
    count += 1 if len(set(range(min1, max1+1)).intersection(set(range(min2, max2+1)))) != 0 else 0
print(count)