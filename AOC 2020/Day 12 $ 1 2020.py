input_file = open("Day 12 2020.txt")
input_file = open("Day 12 2020 alt.txt")
directions = []
for line in input_file:
    if line[-1] == "\n":
        directions.append(line[:-1])
    else:
        directions.append(line)


curr_x = 0
curr_y = 0 
facing = 2
for i in directions:
    instruction = i[0]
    move = int(i[1:])
    #print(instruction)
    #print(move)
    if instruction == "N":
        curr_y += move
    elif instruction == "E":
        curr_x += move
    elif instruction == "S":
        curr_y -= move
    elif instruction == "W":
        curr_x -= move

    elif instruction == "R":
        if move == 90:
            if facing < 4:
                facing += 1
            else:
                facing = 1
        elif move == 180:
            if facing < 3:
                facing += 2
            elif facing == 3:
                facing = 1
            elif facing == 4:
                facing = 2
        elif move == 270:
            if facing > 1:
                facing -= 1
            else:
                facing = 4
    
    elif instruction == "L":
        if move == 90:
            if facing > 1:
                facing -= 1
            else:
                facing = 4
        elif move == 180:
            if facing > 2:
                facing -= 2
            elif facing == 2:
                facing = 4
            elif facing == 1:
                facing = 3
        elif move == 270:
            if facing < 4:
                facing += 1
            else:
                facing = 1
    elif instruction == "F":
        if facing == 1:
            curr_y += move
        elif facing == 2:
            curr_x += move
        elif facing == 3:
            curr_y -= move
        elif facing == 4:
            curr_x -= move
    
    #print(facing)
    #print((curr_x,curr_y))
    #print()
print(abs(curr_x)+abs(curr_y))