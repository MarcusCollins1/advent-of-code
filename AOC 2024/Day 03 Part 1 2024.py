import re
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 03 2024.txt"
# FILE_NAME = "Day 03 2024 test 1.txt"

with open(FOLDER_PATH + FILE_NAME, "r") as file:
    print(sum([int(x)*int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file.read())]))
