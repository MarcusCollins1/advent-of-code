FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 13 2017.txt"
# FILE_NAME = "Day 13 2017 alt.txt"
# FILE_NAME = "Day 13 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

LAYERS = {int(line.split(": ")[0]): int(line.split(": ")[1]) for line in data}

def isNotCaught(delay: int, layers: dict[int, int]):
    for layer in layers.keys():
        if isCaughtInLayer(layer, delay, layers): return False
    return True

def isCaughtInLayer(layer: int, delay: int, layers:dict[int,int]):
    layerDepth = layers[layer]
    stepsIn = (layer+delay) % ((layerDepth-1)*2)
    return stepsIn == 0

delay = 0
while True:
    if isNotCaught(delay, LAYERS): break
    delay += 1
print(delay)