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

way_point_x = 10
way_point_y = 1
for i in directions:
    instruction = i[0]
    move = int(i[1:])
    #print(instruction)
    #print(move)
    if instruction == "N":
        way_point_y += move
    elif instruction == "E":
        way_point_x += move
    elif instruction == "S":
        way_point_y -= move
    elif instruction == "W":
        way_point_x -= move
    
    elif instruction == "R":
        for i in range(move//90):
            temp = way_point_y
            way_point_y = way_point_x*-1
            way_point_x = temp
    
    elif instruction == "L":
        for i in range(move//90):
            temp = way_point_y*-1
            way_point_y = way_point_x
            way_point_x = temp
    elif instruction == "F":
        curr_x += way_point_x*move
        curr_y += way_point_y*move
    
    #print(facing)
    #print((curr_x,curr_y))
    #print()
print(abs(curr_x)+abs(curr_y))