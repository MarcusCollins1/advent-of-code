target = 347991
target = 368078
#target = 29
sides = []
steps = []
for i in range(4):
    count_1 = 1
    difference = ((i+1)*2)-1
    num_steps = 0
    while count_1 < target:
        count_1 += difference
        difference += 8
        num_steps += 1
    count_1_lower = count_1 - (difference-8)
    num_steps_lower = num_steps-1
    #print(count_1)
    #print(count_1_lower)

    if count_1-target < target-count_1_lower:
        sides.append(count_1)
        steps.append(num_steps)
    else:
        sides.append(count_1_lower)
        steps.append(num_steps_lower)
    #print(side_1)
print(sides)
print(steps)
lowest = float("inf")
for i in sides:
    if abs(i-target) < lowest:
        lowest = abs(i-target)
        lowest_side = i
print(lowest)
print(lowest_side)
lowest_steps = steps[sides.index(lowest_side)]
print(lowest_steps)


print("Answer is", lowest_steps+lowest)