from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 6 2018.txt"
# FILE_NAME = "Day 6 2018 alt.txt"
# FILE_NAME = "Day 6 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [tuple(map(int, x.strip().split(","))) for x in file.readlines()]
file.close()

x0, x1 = min(x for x, y in data), max(x for x, y in data)
y0, y1 = min(y for x, y in data), max(y for x, y in data)

def dist(x1:int, y1:int, x2:int, y2:int) -> int:
    return abs(x1-x2) + abs(y1-y2)

counts = defaultdict(int)
infinite = set()

for y in range(y0, y1+1):
    for x in range(x0, x1+1):
        ds = sorted((dist(x, y, px, py), i) for i, (px, py) in enumerate(data))
        if ds[0][0] != ds[1][0]:
            counts[ds[0][1]] += 1
            if x==x0 or y==y0 or x==x1 or y==y1:
                infinite.add(ds[0][1])
for k in infinite:
    counts.pop(k)
print(max(counts.values()))