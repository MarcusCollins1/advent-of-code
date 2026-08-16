from time import time
t1 = time()
from math import prod
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 06 2025.txt"
# FILE_NAME = "Day 06 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip().split() for x in file.readlines()]
file.close()

def getCol(data: list[list[str]], col: int) -> list[int]:
    answer: list[int] = []
    for row in data[:-1]:
        answer.append(int(row[col]))
    return answer

answers: list[int] = []

for col in range(len(data[0])):
    operator = data[-1][col]
    if operator == "+":
        answers.append(sum(getCol(data, col)))
    else:
        answers.append(prod(getCol(data, col)))

print(sum(answers))

print(f"Time Taken: {time()-t1:.3f}s")