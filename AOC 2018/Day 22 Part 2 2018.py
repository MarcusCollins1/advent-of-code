from time import time
t1 = time()
import re
from heapq import heappush, heappop
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
        if (x, y) in self.erosionLevel: return self.erosionLevel[(x, y)]
        self.erosionLevel[(x, y)] = (self.getGeologicIndex(x, y) + self.depth) % 20183
        return self.erosionLevel[(x, y)]

    def getSquareType(self, x: int, y: int) -> int:
        return self.getErosionLevel(x, y) % 3

    def solve(self) -> int:
        allowedTools = {
            0: {"torch", "climbing"},
            1: {"climbing", "neither"},
            2: {"torch", "neither"}
        }

        start = (0, 0, "torch")
        end = (*self.target, "torch")

        queue = [(0, start)]
        distances: dict = {start: 0}

        while queue:
            time, (x, y, tool) = heappop(queue)

            if time > distances[(x, y, tool)]: continue

            if (x, y, tool) == end: return time

            # Option 1: switch equipment
            region = self.getSquareType(x, y)

            for newTool in allowedTools[region]:
                if newTool == tool: continue

                newState = (x, y, newTool)
                newTime = time + 7
                if newTime < distances.get(newState, float("inf")):
                    distances[newState] = newTime
                    heappush(queue, (newTime, newState)) # type: ignore
            
            # Option 2: Move to adjacent squares
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy

                if nx < 0 or ny < 0: continue

                newRegion = self.getSquareType(nx, ny)
                if tool not in allowedTools[newRegion]: continue

                newState = (nx, ny, tool)
                newTime = time + 1

                if newTime < distances.get(newState, float("inf")):
                    distances[newState] = newTime
                    heappush(queue, (newTime, newState)) # type: ignore

        raise RuntimeError("No path found")

solver = Solver(data)
print(solver.solve()    )

print(f"Time Taken: {time()-t1:.2f}s")