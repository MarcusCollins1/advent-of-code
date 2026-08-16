FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 09 2024.txt"
# FILE_NAME = "Day 09 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
diskMap = list(map(int, list(file.read().strip())))
file.close()

disk: dict[int, int] = {}
index = 0
fileId = 0
isFile = True
for item in diskMap:
    if isFile:
        for i in range(index, index+item): disk[i] = fileId
        fileId += 1
    index += item
    isFile = not isFile

gaps: list[int] = [i for i in range(max(disk.keys())+1) if i not in disk.keys()]
for gap in gaps:
    maximumIndex = max(disk.keys())
    if gap > maximumIndex: break
    disk[gap] = disk[maximumIndex]
    del disk[maximumIndex]

print(sum([key*val for key, val in disk.items()]))