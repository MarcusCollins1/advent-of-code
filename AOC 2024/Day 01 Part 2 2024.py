FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 01 2024.txt"
# FILE_NAME = "Day 01 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

list1: list[int]
list2: list[int]
list1, list2 = list(map(list, zip(*(map(int, line.split()) for line in data))))

print(sum([num1 * list2.count(num1) for num1 in list1]))