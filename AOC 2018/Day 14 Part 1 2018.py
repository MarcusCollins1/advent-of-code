from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 14 2018.txt"
# FILE_NAME = "Day 14 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = int(file.read().strip())
file.close()

recipes: list[int] = [3, 7]
idx1, idx2 = 0, 1

while len(recipes) < data + 10:
    r1, r2 = recipes[idx1], recipes[idx2]
    newRecipes = [int(x) for x in str(r1+r2)]
    recipes += newRecipes
    idx1 = (idx1+r1+1)%len(recipes)
    idx2 = (idx2+r2+1)%len(recipes)
    # print(recipes)

print("".join([str(x) for x in recipes[data:data+10]]))

print(f"Time Taken: {time()-t1:.2f}s")