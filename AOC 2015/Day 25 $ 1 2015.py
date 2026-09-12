import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 25 2015.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

row, column = map(int, re.findall(r'\d+', data[0]))

def diagonalValue(row, col) -> int:
    if row < 1 or col < 1:
        raise ValueError("Row and Column must be 1 or greater")
    k = row+col-1
    before = (k*(k-1))//2
    pos = (k-row)+1
    return before + pos
n = diagonalValue(row, column)

value = 20151125
for i in range(n-1):
    value = (value * 252533) % 33554393
print(value)