from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 19 2016.txt"
# FILE_NAME = "Day 19 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = int(file.read().strip())
file.close()

presents = [True for _ in range(data)]

idx: int = 0
for _ in range(data-1):
    steal = (idx+1)%data
    while not presents[steal]:
        steal = (steal+1)%data
    presents[steal] = False

    idx = (idx+1)%data
    while not presents[idx]:
        idx = (idx+1)%data

print(presents.index(True)+1)

print(f"Time Taken: {time()-t1:.2f}s")