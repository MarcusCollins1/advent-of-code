# input_file = open("Day 5 2020.txt")
input_file = open("Day 5 2020 alt.txt")
seats = []
for line in input_file:
    if line[-1] == "\n":
        seats.append(line[:-1])
    else:
        seats.append(line)


seats_found = []

for i in seats:
    curr_max_row = 127
    curr_min_row = 0
    for j in i[:7]:
        if j == "F":
            curr_max_row = ((curr_max_row + curr_min_row)//2)
        elif j == "B":
            curr_min_row = ((curr_max_row + curr_min_row)//2)+1
    
    row = curr_max_row

    curr_max_col = 7
    curr_min_col = 0
    for j in i[7:]:
        if j == "R":
            curr_min_col = ((curr_max_col + curr_min_col)//2)+1
        elif j == "L":
            curr_max_col = ((curr_max_col + curr_min_col)//2)
    col = curr_max_col
    curr_id = row*8 + col
    seats_found.append(curr_id)


print(max(seats_found))

    

    
    
    
    


