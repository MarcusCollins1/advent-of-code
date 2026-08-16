from collections import deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 16 2023.txt"
# FILE_NAME = "Day 16 2023 alt.txt"
# FILE_NAME = "Day 16 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
lines = [x.strip() for x in file.readlines()]
file.close()

MAX_X, MAX_Y = len(lines[0]), len(lines)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = {
    "|": {LEFT: (DOWN, UP), RIGHT: (DOWN, UP)},
    "-": {UP: (LEFT, RIGHT), DOWN: (LEFT, RIGHT)},
    "/": {UP: (RIGHT,), DOWN: (LEFT,), LEFT: (DOWN,), RIGHT: (UP,)},
    "\\": {UP: (LEFT,), DOWN: (RIGHT,), LEFT: (UP,), RIGHT: (DOWN,)},
    ".": {},
}

def Track(queue:deque) -> int:
    seen = set()

    while queue:
        row, column, dr, dc = queue.popleft()
        new_row = row + dr
        new_column = column + dc

        if (
            new_row < 0
            or new_row >= len(lines)
            or new_column < 0
            or new_column >= len(lines[0])
        ):
            continue

        for new_directions in DIRECTIONS[lines[new_row][new_column]].get(
            (dr, dc), ((dr, dc),)
        ):
            if (new_row, new_column, *new_directions) not in seen:
                queue.append([new_row, new_column, *new_directions]) # type:ignore
                seen.add((new_row, new_column, *new_directions))

    return len({(row, column) for row, column, *_ in seen})

maximum = 0
# top and bottom
for x in range(MAX_X):
    # top
    maximum = max(maximum, Track(deque([(-1, x, *DOWN)])))
    # bottom
    maximum = max(maximum, Track(deque([(MAX_Y, x, *UP)])))
# left and right
for y in range(MAX_Y):
    # left
    maximum = max([maximum, Track(deque([(y, -1, *RIGHT)]))])
    # right
    maximum = max([maximum, Track(deque([(y, MAX_X, *LEFT)]))])

print(maximum)