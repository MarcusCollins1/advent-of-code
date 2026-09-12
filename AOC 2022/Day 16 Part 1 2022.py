FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 16 2022.txt"
FILE_NAME = "Day 16 2022 alt.txt"
FILE_NAME = "Day 16 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

NUM_MINS = 3

tunnels = dict()
valve_flow_rate = dict()

for line in data:
    if "tunnels" in line:
        line = line.strip().replace("Valve ", "").replace(" has flow rate=", ",").replace("; tunnels lead to valves ", ",").replace(", ", ",").split(",")
    else:
        line = line.strip().replace("Valve ", "").replace(" has flow rate=", ",").replace("; tunnel leads to valve ", ",").replace(", ", ",").split(",")
    tunnels[line[0]] = line[2:]
    valve_flow_rate[line[0]] = int(line[1])

print("Created tunnels and flow rates")

paths = []
queue = [["AA"]]

while queue:
    curr = queue.pop(0)
    if type(curr[-1]) == int:
        curr_room = curr[-2]
    else:
        curr_room = curr[-1]
        # try opening the valve
        amount = valve_flow_rate[curr_room]*(NUM_MINS-len(curr))
        if amount != 0:
            next = curr + [amount]
            if len(next) == NUM_MINS:
                paths.append(next)
            else:
                queue.append(next)
    # go to new rooms
    for room in tunnels[curr_room]:
        if curr.count(room) > 1:
            continue
        next = curr + [room]
        if len(next) == NUM_MINS:
            paths.append(next)
        else:
            queue.append(next)

print("Found all the paths")

max_pressure_release = 0
for path in paths:
    curr = 0
    for item in path:
        if type(item) == int:
            curr += item
    max_pressure_release = max([max_pressure_release, curr])
print("Found the path that releases the most pressure")
print(f"The most pressure that can be released is: {max_pressure_release}")