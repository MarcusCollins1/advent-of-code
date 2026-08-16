from collections import deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 07 2024.txt"
# FILE_NAME = "Day 07 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip().split(": ") for x in file.readlines()]
file.close()

def Valid(target: int, values: list[int]) -> bool:
    queue: deque[list[int]] = deque([values])
    while len(queue) > 0:
        curr = queue.popleft()
        if len(curr) == 1:
            if curr[0] == target: return True
        elif len(curr) == 2:
            next1 = [curr[0] + curr[1]]
            next2 = [curr[0] * curr[1]]
            queue.appendleft(next1)
            queue.appendleft(next2)
        else:
            next1 = [curr[0] + curr[1]] + curr[2:]
            next2 = [curr[0] * curr[1]] + curr[2:]
            queue.appendleft(next1)
            queue.appendleft(next2)

    return False

print(sum([int(line[0]) for line in data if (Valid(int(line[0]), list(map(int, line[1].split()))))]))