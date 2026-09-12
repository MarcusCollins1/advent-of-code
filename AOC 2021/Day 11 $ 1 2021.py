# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 11 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 11 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 11 2021 test.txt", "r")
file = input_file.read().splitlines()
octo = []
for line in file:
    octo.append(list(map(int, list(line))))
rows = len(octo)
cols = len(octo[0])
flashes = 0
def flashing(r, c):
    global flashed, flashes
    flashes += 1
    flashed.add((r, c))
    # up
    if r > 0:
        octo[r-1][c] += 1
        if octo[r-1][c] > 9 and (r-1,c) not in flashed:
            flashing(r-1, c)
    # up and right
    if r > 0 and c < cols-1:
        octo[r-1][c+1] += 1
        if octo[r-1][c+1] > 9 and (r-1,c+1) not in flashed:
            flashing(r-1, c+1)
    # right
    if c < cols-1:
        octo[r][c+1] += 1
        if octo[r][c+1] > 9 and (r,c+1) not in flashed:
            flashing(r, c+1)
    # down and right
    if r < rows-1 and c < cols-1:
        octo[r+1][c+1] += 1
        if octo[r+1][c+1] > 9 and (r+1,c+1) not in flashed:
            flashing(r+1, c+1)
    # down
    if r < rows-1:
        octo[r+1][c] += 1
        if octo[r+1][c] > 9 and (r+1,c) not in flashed:
            flashing(r+1, c)
    # down and left
    if r < rows-1 and c > 0:
        octo[r+1][c-1] += 1
        if octo[r+1][c-1] > 9 and (r+1,c-1) not in flashed:
            flashing(r+1, c-1)
    # left
    if c > 0:
        octo[r][c-1] += 1
        if octo[r][c-1] > 9 and (r,c-1) not in flashed:
            flashing(r, c-1)
    # up and left
    if r > 0 and c > 0:
        octo[r-1][c-1] += 1
        if octo[r-1][c-1] > 9 and (r-1,c-1) not in flashed:
            flashing(r-1, c-1)


for _ in range(100):
    flashed = set()
    for row in range(rows):
        for col in range(cols):
            octo[row][col] += 1
            if octo[row][col] > 9 and (row,col) not in flashed:
                flashed.add((row,col))
                flag = True
                flashing(row,col)
    for pos in flashed:
        row, col = pos
        octo[row][col] = 0
print(flashes)