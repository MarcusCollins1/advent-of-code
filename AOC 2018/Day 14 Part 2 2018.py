from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 14 2018.txt"
# FILE_NAME = "Day 14 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [int(x) for x in file.read().strip()]
file.close()

length = len(data)

recipes: list[int] = [3, 7]
idx1, idx2 = 0, 1

while True:
    r1, r2 = recipes[idx1], recipes[idx2]
    total = r1+r2
    if total >= 10:
        recipes.append(1)
        recipes.append(total-10)
    else:
        recipes.append(total)

    start = len(recipes) - length

    if start >= 0 and recipes[start:] == data: break

    if len(recipes)>=length+1:
        start = len(recipes) - length - 1
        if recipes[start:start + length] == data: break

    idx1 = (idx1+r1+1)%len(recipes)
    idx2 = (idx2+r2+1)%len(recipes)

print(start)

print(f"Time Taken: {time()-t1:.2f}s")