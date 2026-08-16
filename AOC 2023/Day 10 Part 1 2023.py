FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 10 2023.txt"
# FILE_NAME = "Day 10 2023 alt.txt"
# FILE_NAME = "Day 10 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

DIRECTIONS = {"|":[(0, -1), (0, 1)], "-":[(-1, 0), (1, 0)], "L":[(0, -1), (1, 0)], "J":[(0, -1), (-1, 0)], "7":[(0, 1), (-1, 0)], "F":[(0, 1), (1, 0)], "S":[(0, 1), (0, -1), (1, 0), (-1, 0)]}

class Pipe:
    def __init__(self, pos:tuple, valid_dir:list) -> None:
        self.pos = pos
        self.valid_dir = valid_dir
    def __repr__(self) -> str:
        return f"{self.pos} {self.valid_dir}"

pipes = dict()

starting_pos = (0, 0)

for row, line in enumerate(data):
    for col, cell in enumerate(line):
        if cell == ".":
            continue
        pipes[(col, row)] = Pipe((col, row), DIRECTIONS[cell])
        if cell == "S":
            starting_pos = (col, row)

distances = {starting_pos:0}
queue = [[starting_pos, 0]]
visited = set()
while queue:
    curr_pos, distance = queue.pop(0)
    visited.add(curr_pos)
    curr_pipe = pipes[curr_pos]
    for dir in curr_pipe.valid_dir:
        look_at = tuple(sum(x) for x in zip(curr_pos, dir))
        if look_at not in pipes.keys():
            continue
        if (-dir[0], -dir[1]) in pipes[look_at].valid_dir and look_at not in visited:
            queue.append([look_at, distance+1])
            distances[look_at] = distance+1 # type:ignore

print(max(distances.values()))