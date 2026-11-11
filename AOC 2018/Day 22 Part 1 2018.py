from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 22 2018.txt"
# FILE_NAME = "Day 22 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Solver:
    def __init__(self, data: list[str]) -> None:
        self.depth, self.target = self.parseData(data)
        
        self.geologicIndex = dict()
        self.erosionLevel = dict()

    def parseData(self, data: list[str]) -> tuple[int, tuple[int, int]]:
        depth = int(re.search(r"depth:\s*(\d+)", data[0]).group(1)) # type: ignore
        target = tuple(map(int, re.search(r"target:\s*(\d+),(\d+)", data[1]).groups())) # type: ignore
        return depth, target # type: ignore

    def getGeologicIndex(self, x: int, y: int) -> int:
        if not (0 <= x <= self.target[0] and 0 <= y <= self.target[1]):
            raise ValueError(f"0 <= {x} <= {self.target[0]} and 0 <= {y} <= {self.target[1]}")
        if (x, y) in self.geologicIndex: return self.geologicIndex[(x, y)]

        if (x, y) == (0, 0):
            self.geologicIndex[(x, y)] = 0
        elif (x, y) == self.target:
            self.geologicIndex[(x, y)] = 0
        elif y == 0:
            self.geologicIndex[(x, y)] = x * 16807
        elif x == 0:
            self.geologicIndex[(x, y)] = y * 48271
        else:
            self.geologicIndex[(x, y)] = self.getErosionLevel(x-1, y) * self.getErosionLevel(x, y-1)
        return self.geologicIndex[(x, y)]

    def getErosionLevel(self, x: int, y: int) -> int:
        if not (0 <= x <= self.target[0] and 0 <= y <= self.target[1]):
            raise ValueError(f"0 <= {x} <= {self.target[0]} and 0 <= {y} <= {self.target[1]}")
        if (x, y) in self.erosionLevel: return self.erosionLevel[(x, y)]
        self.erosionLevel[(x, y)] = (self.getGeologicIndex(x, y) + self.depth) % 20183
        return self.erosionLevel[(x, y)]

    def getRiskLevel(self, x: int, y: int) -> int:
        if not (0 <= x <= self.target[0] and 0 <= y <= self.target[1]):
            raise ValueError(f"0 <= {x} <= {self.target[0]} and 0 <= {y} <= {self.target[1]}")
        return self.getErosionLevel(x, y) % 3

    def solve(self) -> int:
        return sum(self.getRiskLevel(x, y) for x in range(self.target[0] + 1) for y in range(self.target[1] + 1))

solver = Solver(data)
print(solver.solve()    )

print(f"Time Taken: {time()-t1:.2f}s")