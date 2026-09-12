from time import time
t1 = time()
import re
from itertools import combinations, chain
from collections import deque, Counter
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 11 2016.txt"
# FILE_NAME = "Day 11 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data: list[str] = [x.strip() for x in file.readlines()]
file.close()

state = [set(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', line)) for line in data]
state[0] = state[0].union([('elerium', 'generator'), ('elerium', 'microchip'), ('dilithium', 'generator'), ('dilithium', 'microchip')])

def isValidTransition(floor: set) -> bool:
    return len(set(type for _, type in floor)) < 2 or \
        all((obj, 'generator') in floor
            for (obj, type) in floor
            if type == 'microchip')

def nextStates(state: tuple[int, int, list[set[str]]]):
    moves, elevator, floors = state
    possibleMoves = chain(combinations(floors[elevator], 2), combinations(floors[elevator], 1))
    for move in possibleMoves:
        for direction in [-1, 1]:
            nextElevator = elevator + direction
            if not 0 <= nextElevator < len(floors):
                continue

            nextFloors = floors.copy()
            nextFloors[elevator] = nextFloors[elevator].difference(move)
            nextFloors[nextElevator] = nextFloors[nextElevator].union(move)

            if (isValidTransition(nextFloors[elevator]) and isValidTransition(nextFloors[nextElevator])):
                yield (moves + 1, nextElevator, nextFloors)

def isAllTopLevel(floors):
    return all(not floor
               for number, floor in enumerate(floors)
               if number < len(floors) - 1)

def countFloorObjects(state):
    _, elevator, floors = state
    return elevator, tuple(tuple(Counter(type for _, type in floor).most_common()) for floor in floors)

def minMovesToTopLevel(floors: list[set[str]]):
    seen = set()
    queue: deque[tuple[int, int, list[set[str]]]] = deque([(0, 0, floors)])

    while queue:
        state = queue.popleft()
        moves, _, floors = state
        if isAllTopLevel(floors):
            return moves

        for nextState in nextStates(state):
            if (key := countFloorObjects(nextState)) not in seen:
                seen.add(key)
                queue.append(nextState)

print(minMovesToTopLevel(state))
print(f"Time Taken: {time()-t1:.2f}s")