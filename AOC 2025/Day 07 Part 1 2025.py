from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 07 2025.txt"
# FILE_NAME = "Day 07 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

numSplits: int = 0
beamIndexes: set[int] = set()
beamIndexes.add(data[0].index("S"))

for rowIndex in range(1, len(data)):
    newBeamIndex: set[int] = set()
    for beamIdx in beamIndexes:
        if data[rowIndex][beamIdx] == ".":
            newBeamIndex.add(beamIdx)
        else:
            newBeamIndex.add(beamIdx-1)
            newBeamIndex.add(beamIdx+1)
            numSplits += 1
    beamIndexes = newBeamIndex

print(numSplits)

print(f"Time Taken: {time()-t1:.3f}s")