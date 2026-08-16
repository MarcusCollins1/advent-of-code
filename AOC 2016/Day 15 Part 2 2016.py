from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 15 2016.txt"
# FILE_NAME = "Day 15 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Disc:
    def __init__(self, pos: int, numPos: int, discNum: int) -> None:
        self.pos = pos
        self.numPos = numPos
        self.discNum = discNum
    
    def valid(self, t: int) -> bool:
        return (self.pos + t + self.discNum)%self.numPos == 0

    def __str__(self) -> str:
        return f"Disc: Pos:{self.pos}, numPos: {self.numPos}"

discs: list[Disc] = []
for line in data:
    match = re.match(r"Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+).", line)
    if match:
        discNum, numPos, pos = list(map(int, match.groups()))
        discs.append(Disc(pos, numPos, discNum))

discs.append(Disc(0, 11, max([disc.discNum for disc in discs])+1))

t = 0
while True:
    if all([disc.valid(t) for disc in discs]):
        break
    t += 1
print(t)

print(f"Time Taken: {time()-t1:.3f}s")