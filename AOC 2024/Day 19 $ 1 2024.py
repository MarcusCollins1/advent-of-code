from collections import deque
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 19 2024.txt"
# FILE_NAME = "Day 19 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
availablePatterns, designs = [x.strip() for x in file.read().split("\n\n")]
file.close()
availablePatterns = availablePatterns.split(", ")
designs = designs.splitlines()

def PatternPossible(pattern: str, availablePatterns: list[str]) -> bool:
    queue: deque[str] = deque([availablePattern for availablePattern in availablePatterns if pattern.startswith(availablePattern)])
    while queue:
        currPattern = queue.popleft()
        for availablePattern in availablePatterns:
            nextPattern = currPattern + availablePattern
            if pattern == nextPattern: return True
            elif pattern.startswith(nextPattern): queue.appendleft(nextPattern)
    return False

print(sum([1 for design in designs if PatternPossible(design, availablePatterns)]))