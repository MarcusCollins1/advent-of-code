FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 5 2017.txt"
# FILE_NAME = "Day 5 2017 alt.txt"
# FILE_NAME = "Day 5 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

data = list(map(int, data))
index = 0
steps = 0
while 0 <= index < len(data):
    temp_index = index + data[index]
    data[index] += 1
    index = temp_index
    steps += 1

print(steps)