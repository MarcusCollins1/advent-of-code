FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 11 2017.txt"
# FILE_NAME = "Day 11 2017 alt.txt"
# FILE_NAME = "Day 11 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

directions = data.split(",")

directionToDelta = {"n": (1,0), "ne": (0,1), "se": (-1,1), "s":(-1,0), "sw": (0,-1), "nw": (1,-1)}

def multiplyTuple(t:tuple, x:int) -> tuple:
    return tuple(y*x for y in t)
def sumTuples(lst:list[tuple]) -> tuple:
    return tuple(sum([t[idx] for t in lst]) for idx in range(len(lst[0])))
def distance(t: tuple[int, int]) -> int:
    return max(abs(t[0]), abs(t[1])) if (t[0] < 0 and t[1] > 0) or (t[0] > 0 and t[1] < 0) else abs(t[0]) + abs(t[1])

pos = (0,0)
maxDistance = 0

for d in directions:
    pos = sumTuples([pos, directionToDelta[d]])
    maxDistance = max([maxDistance, distance(pos)])
print(maxDistance)