# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 17 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 17 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 17 2021 test.txt", "r")
file = input_file.read().replace("target area: x=", "").replace("..", ",").replace(" ", "").replace("y=", "")
min_x, max_x, min_y, max_y = list(map(int, file.split(",")))
highest_y = 0
count_y = 0
for i in range(1000):
    count_x = 0
    made_once = False
    while True:
        x, y = 0, 0
        trajectory_x, trajectory_y = count_x, count_y
        made_it = True
        move_on = False
        curr_highest = 0
        while not((min_x <= x <= max_x) and (min_y <= y <= max_y)):
            x += trajectory_x
            y += trajectory_y
            if trajectory_x > 0:
                trajectory_x -= 1
            trajectory_y -= 1
            curr_highest = max([curr_highest, y])
            if x > max_x :
                made_it = False
                move_on = True
                break
            if y < min_y:
                made_it = False
                break
        if made_it:
            highest_y = max([highest_y, curr_highest])
            made_once = True
        if move_on:
            break
        count_x += 1
    count_y += 1
    #if not made_once:
    #    break
print(highest_y)
