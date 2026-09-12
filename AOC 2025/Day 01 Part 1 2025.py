from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 01 2025.txt"
# FILE_NAME = "Day 01 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

num = 50
count = 0

for line in data:
    direction, clicks = line[0], line[1:]
    x = 1 if direction == "R" else -1
    clicks = int(clicks)
    num = (num + clicks * x) % 100
    if num == 0: count += 1

print(count)
print(f"Time taken: {time()-t1:.3f}")