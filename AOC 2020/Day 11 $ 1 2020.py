from collections import defaultdict
from copy import deepcopy
input_file = open("Day 11 2020.txt")
input_file = open("Day 11 2020 alt.txt")
seats = []
for line in input_file:
    if line[-1] == "\n":
        seats.append(line[:-1])
    else:
        seats.append(line)

#print(seats)
rows = len(seats)
cols = len(seats[0])

def grid_to_str(grid, rows, cols):
    grid_str = ""
    for row in range(rows):
        for col in range(cols):
            grid_str += grid[(row, col)]
        grid_str += "\n"
    return grid_str


grid = defaultdict(str)
for row in range(len(seats)):
    for col in range(len(seats[row])):
        grid[(row,col)] = seats[row][col]
#print(grid)
#print(grid_to_str(grid, rows, cols))

def num_occ(grid, row, col):
    count = 0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if i == row and j == col:
                pass
            else:
                if grid[(i,j)] == "#":
                    count += 1
    return count


def update_grid(grid, rows, cols):
    new_grid = defaultdict(str)
    for row in range(rows):
        for col in range(cols):
            if grid[(row,col)] == "L":
                if num_occ(grid, row, col) == 0:
                    new_grid[(row,col)] = "#"
                else:
                    new_grid[(row,col)] = "L"
            elif grid[(row,col)] == "#":
                if num_occ(grid, row, col) >= 4:
                    new_grid[(row,col)] = "L"
                else:
                    new_grid[(row,col)] = "#"
            else:
                new_grid[(row,col)] = "."
    return new_grid







moving = True
while moving:
#for i in range(5):
    grid_next = update_grid(grid, rows, cols)
    #print(grid_to_str(grid_next, rows, cols))

    all_same = True
    for row in range(rows):
        for col in range(cols):
            if grid[(row,col)] != grid_next[(row,col)]:
                all_same = False
    if all_same:
        moving = False
    grid = deepcopy(grid_next)


total = 0
for row in range(rows):
    for col in range(cols):
        if grid[(row,col)] == "#":
            total += 1
print(total)