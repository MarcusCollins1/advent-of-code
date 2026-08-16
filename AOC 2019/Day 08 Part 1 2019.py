FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 8 2019.txt"
FILE_NAME = "Day 8 2019 alt.txt"
# FILE_NAME = "Day 8 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, list(file.read().strip())))
file.close()

width, height = 25, 6
# width, height = 3, 2

layers = []
numLayers = len(data)//(width*height)
for layerNum in range(numLayers):
    currLayer = []
    for num in range(width*height):
        currLayer.append(data.pop(0))
    layers.append(currLayer)

fewest = float("inf")
index = 0
for i, layer in enumerate(layers):
    count = layer.count(0)
    if count < fewest:
        fewest = count
        index = i
print(layers[index].count(1)*layers[index].count(2))