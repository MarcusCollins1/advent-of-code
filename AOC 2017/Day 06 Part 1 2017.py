FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 6 2017.txt"
# FILE_NAME = "Day 6 2017 alt.txt"
# FILE_NAME = "Day 6 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

def GetHighestIndex(lst:list) -> int:
    greatest = 0
    for num in lst:
        greatest = max([greatest, num])
    for i, num in enumerate(lst):
        if num == greatest:
            return i
    return -1

data = list(map(int, data[0].split()))

visited = set()
count = 0
while ",".join(list(map(str, data))) not in visited:
    visited.add(",".join(list(map(str, data))))
    index = GetHighestIndex(data)
    value = data[index]
    data[index] = 0
    for i in range(value):
        index = (index+1)%len(data)
        data[index] += 1
    count += 1
print(count)