import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 16 2015.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

TARGET = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

def getSueFromLine(line: str) -> dict[str, int]:
    pattern = r"(\w+): (\d+)"
    match = re.findall(pattern, line)
    return {key: int(value) for key, value in match}

def sueMeetsTarget(sue: dict[str, int]) -> bool:
    global TARGET
    for key in TARGET.keys():
        if key in sue:
            if key in ["cats", "trees"]:
                if TARGET[key] >= sue[key]: return False
            elif key in ["pomeranians", "goldfish"]:
                if TARGET[key] <= sue[key]: return False
            elif TARGET[key] != sue[key]: return False
    return True

sues = [getSueFromLine(line) for line in data]

print([i+1 for i, sue in enumerate(sues) if sueMeetsTarget(sue)][0])