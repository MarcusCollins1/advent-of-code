from time import time
t1 = time()
from itertools import combinations
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 09 2025.txt"
# FILE_NAME = "Day 09 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data: list[tuple[int, int]] = [tuple(map(int, x.strip().split(","))) for x in file.readlines()] #type: ignore
file.close()

def getArea(corner1: tuple[int, int], corner2: tuple[int, int]) -> int:
    width = abs(corner1[0]-corner2[0]+1)
    height = abs(corner1[1]-corner2[1]+1)
    return width*height

print(max([getArea(c1, c2) for c1, c2 in combinations(data, 2)]))

print(f"Time Taken: {time()-t1:.3f}s")