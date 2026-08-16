FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 01 2024.txt"
FILE_NAME = "Day 01 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

print(sum([abs(num1-num2) for num1, num2 in zip(*list(map(sorted, map(list, zip(*(map(int, line.split()) for line in data))))))]))