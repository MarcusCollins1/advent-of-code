from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 12 2018.txt"
# FILE_NAME = "Day 12 2018 alt.txt"
# FILE_NAME = "Day 12 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

plants: set[int] = set()
initialState = data[0].replace("initial state: ", "")
for i, p in enumerate(initialState):
    if p == "#":
        plants.add(i)

rules: defaultdict[tuple[bool, bool, bool, bool, bool], bool] = defaultdict(bool)
for line in data[2:]:
    start, end = line.split(" => ")
    start = (start[0] == "#", start[1] == "#", start[2] == "#", start[3] == "#", start[4] == "#")
    rules[start] = end == "#"

def PrintPlants() -> None:
    for num in range(-3, 36):
        print("#" if num in plants else ".", end="")
    print()

NUM_GENERATIONS = 20
for _ in range(NUM_GENERATIONS):
    nextGeneration: set[int] = set()
    for num in range(min(plants)-2, max(plants)+3):
        state = (num-2 in plants, num-1 in plants, num in plants, num+1 in plants, num+2 in plants)
        if rules[state]:
            nextGeneration.add(num)
    plants = nextGeneration
print(sum(plants))