import re
from collections import defaultdict
from itertools import combinations, permutations
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 13 2015.txt"
# FILE_NAME = "Day 13 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def calculateScore(seating: list[str]) -> int:
    global pairings
    return sum([pairings[tuple(sorted([a,b]))] for a, b in zip(seating, seating[1:]+seating[0:1])]) #type:ignore
    


happiness:defaultdict[str, defaultdict[str,int]] = defaultdict(defaultdict)
pattern = r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."
for line in data:
    match = re.match(pattern, line)
    if match != None:
        name1, loseGain, points, name2 = match.groups()
        points = int(points)
        happiness[name1[0]][name2[0]] = points if loseGain == "gain" else -points
    
pairings: defaultdict[tuple[str, str], int] = defaultdict(int)
for a, b in combinations(happiness.keys(), 2):
    [a, b] = sorted([a, b])
    pairings[(a, b)] = happiness[a][b] + happiness[b][a]

best = max([calculateScore(list(seating)) for seating in permutations(happiness.keys())])
print(best)