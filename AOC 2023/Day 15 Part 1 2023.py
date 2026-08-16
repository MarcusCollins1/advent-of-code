FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 15 2023.txt"
# FILE_NAME = "Day 15 2023 alt.txt"
# FILE_NAME = "Day 15 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().split(",")
file.close()

def Hash(s:str) -> int:
    value = 0
    for letter in s:
        value += ord(letter)
        value *= 17
        value %= 256
    return value

print(sum([Hash(x) for x in data]))