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
            next3 = [int(f"{curr[0]}{curr[1]}")]
            queue.appendleft(next1)
            queue.appendleft(next2)
            queue.appendleft(next3)
        else:
            next1 = [curr[0] + curr[1]] + curr[2:]
            next2 = [curr[0] * curr[1]] + curr[2:]
            next3 = [int(f"{curr[0]}{curr[1]}")] + curr[2:]
            queue.appendleft(next1)
            queue.appendleft(next2)
            queue.appendleft(next3)

    return False

total = 0
for line in data:
    target = int(line[0])
    values = list(map(int, line[1].split()))
    if Valid(target, values):
        total += target

print(total)