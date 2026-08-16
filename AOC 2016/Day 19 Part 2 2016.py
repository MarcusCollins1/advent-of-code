from time import time
t1 = time()
dt = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 19 2016.txt"
# FILE_NAME = "Day 19 2016 test.txt"

def formatTime(t: float) -> str:
    hrs = int(t // 3600)
    mins = int((t%3600)//60)
    s = t%60
    if hrs > 0:
        return f"{hrs}h {mins}m {s:.2f}s"
    elif mins > 0:
        return f"{mins}m {s:.2f}s"
    else:
        return f"{s:.2f}s"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = int(file.read().strip())
file.close()

elves = [_+1 for _ in range(data)]
length = data

idx: int = 0
for _ in range(data-1):
    steal = (idx + length//2) % length
    elves.pop(steal)
    length -= 1

    if steal >= idx: idx += 1
    if idx >= length: idx=0

    if length%100000 == 0:
        print(f"{length} | Time: {formatTime(time()-dt)} ({formatTime(time()-t1)})")
        dt = time()

print(elves[0])

print(f"Time Taken: {formatTime(time()-t1)}")