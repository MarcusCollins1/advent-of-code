FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2021/"
FILE_NAME = "Day 22 2021.txt"
FILE_NAME = "Day 22 2021 test.txt"

print(527915)

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()