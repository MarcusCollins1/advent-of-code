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

def num_occ_2(grid, row, col):
    count = 0
    #check up
    curr_row = row-1
    curr_col = col
    while grid[(curr_row,curr_col)] == ".":
        curr_row -= 1    
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check up-right
    curr_row = row-1
    curr_col = col+1
    while grid[(curr_row,curr_col)] == ".":
        curr_row -= 1   
        curr_col += 1 
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check right
    curr_row = row
    curr_col = col+1
    while grid[(curr_row,curr_col)] == ".":
        curr_col += 1 
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check down-right
    curr_row = row+1
    curr_col = col+1
    while grid[(curr_row,curr_col)] == ".":
        curr_row += 1   
        curr_col += 1 
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check down
    curr_row = row+1
    curr_col = col
    while grid[(curr_row,curr_col)] == ".":
        curr_row += 1   
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check down-left
    curr_row = row+1
    curr_col = col-1
    while grid[(curr_row,curr_col)] == ".":
        curr_row += 1   
        curr_col -= 1 
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check left
    curr_row = row
    curr_col = col-1
    while grid[(curr_row,curr_col)] == ".":
        curr_col -= 1 
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    #check up-left
    curr_row = row-1
    curr_col = col-1
    while grid[(curr_row,curr_col)] == ".":
        curr_row -= 1   
        curr_col -= 1 
    if grid[(curr_row,curr_col)] == "#":
        count += 1
    
    
    
    return count





def update_grid(grid, rows, cols):
    new_grid = defaultdict(str)
    for row in range(rows):
        for col in range(cols):
            if grid[(row,col)] == "L":
                if num_occ_2(grid, row, col) == 0:
                    new_grid[(row,col)] = "#"
                else:
                    new_grid[(row,col)] = "L"
            elif grid[(row,col)] == "#":
                if num_occ_2(grid, row, col) >= 5:
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