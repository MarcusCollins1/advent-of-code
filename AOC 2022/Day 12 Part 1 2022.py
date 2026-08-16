FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 12 2022.txt"
FILE_NAME = "Day 12 2022 alt.txt"
# FILE_NAME = "Day 12 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

# create grid
grid = []
for line in data:
    grid.append(list(line.strip()))

# find the start and end position
start_pos = ()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            start_pos = (x, y)

# create dicitonary of levels and possible levels from there
alphabet = "abcdefghijklmnopqrstuvwxyz"
heights = {"S":["a", "b"]}
for i in range(len(alphabet)):
    curr = alphabet[:i+2] if i!= len(alphabet)-1 else alphabet[:i+1]
    heights[alphabet[i]] = curr


paths = []
visited = set()
queue = []
queue.append([start_pos])

count = 0
while queue:
    if count == 10000:
        print(f"queue length: {len(queue)}")
        print(f"visited length: {len(visited)}")
        count = 0
    count += 1
    curr = queue.pop(0)
    curr_pos = curr[-1]
    # check up
    if curr_pos[1] != 0:
        if grid[curr_pos[1]-1][curr_pos[0]] in heights[grid[curr_pos[1]][curr_pos[0]]] and (curr_pos[0], curr_pos[1]-1) not in visited:
            queue.append(curr+[(curr_pos[0], curr_pos[1]-1)])
            visited.add((curr_pos[0], curr_pos[1]-1))
        elif grid[curr_pos[1]-1][curr_pos[0]] == "E" and grid[curr_pos[1]][curr_pos[0]] in "yz":
            paths.append(curr+[(curr_pos[0], curr_pos[1]-1)])
    
    # check down
    if curr_pos[1] != len(grid)-1:
        if grid[curr_pos[1]+1][curr_pos[0]] in heights[grid[curr_pos[1]][curr_pos[0]]] and (curr_pos[0], curr_pos[1]+1) not in visited:
            queue.append(curr+[(curr_pos[0], curr_pos[1]+1)])
            visited.add((curr_pos[0], curr_pos[1]+1))
        elif grid[curr_pos[1]+1][curr_pos[0]] == "E" and grid[curr_pos[1]][curr_pos[0]] in "yz":
            paths.append(curr+[(curr_pos[0], curr_pos[1]+1)])
    
    # check left
    if curr_pos[0] != 0:
        if grid[curr_pos[1]][curr_pos[0]-1] in heights[grid[curr_pos[1]][curr_pos[0]]] and (curr_pos[0]-1, curr_pos[1]) not in visited:
            queue.append(curr+[(curr_pos[0]-1, curr_pos[1])])
            visited.add((curr_pos[0]-1, curr_pos[1]))
        elif grid[curr_pos[1]][curr_pos[0]-1] == "E" and grid[curr_pos[1]][curr_pos[0]] in "yz":
            paths.append(curr+[(curr_pos[0]-1, curr_pos[1])])
    
    # check right
    if curr_pos[0] != len(grid[0])-1:
        if grid[curr_pos[1]][curr_pos[0]+1] in heights[grid[curr_pos[1]][curr_pos[0]]] and (curr_pos[0]+1, curr_pos[1]) not in visited:
            queue.append(curr+[(curr_pos[0]+1, curr_pos[1])])
            visited.add((curr_pos[0]+1, curr_pos[1]))
        elif grid[curr_pos[1]][curr_pos[0]+1] == "E" and grid[curr_pos[1]][curr_pos[0]] in "yz":
            paths.append(curr+[(curr_pos[0]+1, curr_pos[1])])
    
paths = sorted(paths, key=len)
print(len(paths[0])-1)