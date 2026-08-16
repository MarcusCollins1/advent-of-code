FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 09 2024.txt"
# FILE_NAME = "Day 09 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
diskMap = list(map(int, list(file.read().strip())))
file.close()

disk: dict[int, tuple[int, int]] = dict()
index = 0
fileId = 0
isFile = True
for item in diskMap:
    if isFile:
        if item != 0: disk[fileId] = (index, index+item)
        fileId += 1
    index += item
    isFile = not isFile

indexes: list[int] = [i for i1, i2 in disk.values() for i in (i1, i2)][1:-1]
gaps: list[tuple[int, int]] = [(indexes[start], indexes[start+1]) for start in range(0, len(indexes), 2)]

for fileId in sorted(disk.keys(),reverse=True):
    start, end = disk[fileId]
    fileLength = end - start
    for i, (gapStart, gapEnd) in enumerate(gaps):
        if gapStart > start: break
        gapLength = gapEnd - gapStart
        if gapLength > fileLength:
            disk[fileId] = (gapStart, gapStart+fileLength)
            gaps[i] = (gapStart+fileLength, gapEnd)
            break
        elif gapLength == fileLength:
            disk[fileId] = (gapStart, gapEnd)
            del gaps[i]
            break

print(sum([sum([key*x for x in range(start, end)]) for key, (start, end) in disk.items()]))