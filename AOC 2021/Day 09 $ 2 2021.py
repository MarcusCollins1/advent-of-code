from math import prod
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 9 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 9 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 9 2021 test.txt", "r")
file = input_file.read().splitlines()
heights = []
for i in file:
    heights.append(list(map(int, list(i))))
basin_sizes = []
for row in range(len(heights)):
    for col in range(len(heights[row])):
        flag = True
        try:
            if heights[row][col] >= heights[row][col+1]:
                flag = False
        except:
            pass
        if col != 0:
            try:
                if heights[row][col] >= heights[row][col-1]:
                    flag = False
            except:
                pass
        try:
            if heights[row][col] >= heights[row+1][col]:
                flag = False
        except:
            pass
        if row != 0:
            try:
                if heights[row][col] >= heights[row-1][col]:
                    flag = False
            except:
                pass
        if flag:
            queue = [(row, col)]
            visited = set(queue)
            while len(queue) != 0:
                curr_pos = queue.pop(0)
                curr_row, curr_col = curr_pos[0], curr_pos[1]
                try:
                    if (heights[curr_row][curr_col] < heights[curr_row][curr_col+1]) and ((curr_row, curr_col+1) not in visited) and (heights[curr_row][curr_col+1] != 9):
                        queue.append((curr_row, curr_col+1))
                except:
                    pass
                try:
                    if (heights[curr_row][curr_col] < heights[curr_row+1][curr_col]) and ((curr_row+1, curr_col) not in visited) and (heights[curr_row+1][curr_col] != 9):
                        queue.append((curr_row+1, curr_col))
                except:
                    pass
                if curr_row != 0:
                    try:
                        if (heights[curr_row][curr_col] < heights[curr_row-1][curr_col]) and ((curr_row-1, curr_col) not in visited) and (heights[curr_row-1][curr_col] != 9):
                            queue.append((curr_row-1, curr_col))
                    except:
                        pass
                if curr_col != 0:
                    try:
                        if (heights[curr_row][curr_col] < heights[curr_row][curr_col-1]) and ((curr_row, curr_col-1) not in visited) and (heights[curr_row][curr_col-1] != 9):
                            queue.append((curr_row, curr_col-1))
                    except:
                        pass
                visited.add(curr_pos)
            basin_sizes.append(len(visited))
highest = sorted(basin_sizes)[-3:]
print(prod(highest))