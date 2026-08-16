FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 11 2017.txt"
# FILE_NAME = "Day 11 2017 alt.txt"
# FILE_NAME = "Day 11 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

directions = data.split(",")

possibleDirections = ["n", "ne", "se", "s", "sw", "nw"]
frequency = {d:directions.count(d) for d in possibleDirections}

directionToDelta = {"n": (1,0), "ne": (0,1), "se": (-1,1), "s":(-1,0), "sw": (0,-1), "nw": (1,-1)}

def multiplyTuple(t:tuple, x:int) -> tuple:
    return tuple(y*x for y in t)
def sumTuples(lst:list[tuple]) -> tuple:
    return tuple(sum([t[idx] for t in lst]) for idx in range(len(lst[0])))

endPos = sumTuples([multiplyTuple(directionToDelta[d], f) for d,f in frequency.items()])
print(endPos)

if (endPos[0] < 0 and endPos[1] > 0) or (endPos[0] > 0 and endPos[1] < 0):
    print(max([abs(endPos[0]), abs(endPos[1])]))
else:
    print(abs(endPos[0]) + abs(endPos[1]))