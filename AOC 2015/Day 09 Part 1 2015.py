from collections import deque
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 09 2015.txt"
# FILE_NAME = "Day 09 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

paths = dict()
places = set()

for line in data:
    place1, place2, distance = line.strip().replace(" to ", " ").replace(" = ", " ").strip().split()
    paths[place1+"-"+place2] = int(distance)
    paths[place2+"-"+place1] = int(distance)
    places.add(place1)
    places.add(place2)

NUM_PLACES = len(places)
places = list(places)

minimum = float("inf")
for starting_place in places:
    visited = set()
    visited.add(starting_place)
    queue = deque()
    queue.append([[starting_place], 0])
    while queue:
        path, distance = queue.popleft()
        # print(path)
        for place in places:
            # print(place)
            if place not in path:
                new = path + [place]
                if tuple(new) not in visited:
                    visited.add(tuple(new))
                    new_distance = distance+paths[path[-1]+"-"+place]
                    if len(new) == NUM_PLACES:
                        minimum = min([minimum, new_distance])
                    else:
                        queue.append([new, new_distance])
print(minimum)

