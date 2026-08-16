FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 8 2019.txt"
FILE_NAME = "Day 8 2019 alt.txt"
# FILE_NAME = "Day 8 2019 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, list(file.read().strip())))
file.close()

width, height = 25, 6
# width, height = 2, 2

layers = []
numLayers = len(data)//(width*height)
for layerNum in range(numLayers):
    currLayer = []
    for num in range(width*height):
        currLayer.append(data.pop(0))
    layers.append(currLayer)

index = 0
for row in range(height):
    for col in range(width):
        i = 0
        while True:
            if layers[i][index] == 0:
                print(" ", end="")
                break
            elif layers[i][index] == 1:
                print("#", end="")
                break
            elif layers[i][index] == 2:
                i += 1
        index += 1
    print()