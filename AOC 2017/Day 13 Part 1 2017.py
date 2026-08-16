FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 13 2017.txt"
# FILE_NAME = "Day 13 2017 alt.txt"
# FILE_NAME = "Day 13 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

LAYERS = {int(line.split(": ")[0]): int(line.split(": ")[1]) for line in data}

def isCaughtInLayer(layer: int, layers:dict[int,int]):
    layerDepth = layers[layer]
    stepsIn = layer % ((layerDepth-1)*2)
    return stepsIn == 0

severity = sum([layer * LAYERS[layer] if isCaughtInLayer(layer, LAYERS) else 0 for layer in LAYERS.keys()])
print(severity)