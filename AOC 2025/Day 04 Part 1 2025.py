from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 04 2025.txt"
# FILE_NAME = "Day 04 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()


def numAdjacentRolls(grid:list[list[str]], x: int, y: int) -> int:
    width, height = len(grid[0]), len(grid)
    count = 0
    for x1, y1 in [(x,y-1), (x+1,y-1), (x+1,y), (x+1,y+1), (x,y+1), (x-1,y+1), (x-1,y), (x-1,y-1)]:
        if (0 <= x1 < width) and (0 <= y1 < height):
            if grid[y1][x1] == "@": count += 1
    return count


print(sum([1 for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "@" and numAdjacentRolls(data, x, y) < 4]))

print(f"Time Taken: {time()-t1:.3f}s")