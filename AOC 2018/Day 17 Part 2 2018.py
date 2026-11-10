from time import time
t1 = time()
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 17 2018.txt"
# FILE_NAME = "Day 17 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Reservoir:
    def __init__(self, text: list[str]) -> None:
        self.clay: set[tuple[int, int]] = set()
        self.flowing: set[tuple[int, int]] = set()
        self.settled: set[tuple[int, int]] = set()

        self.parse(text)

        self.min_y = min(y for x, y in self.clay)
        self.max_y = max(y for x, y in self.clay)
        self.min_x = min(x for x, y in self.clay)
        self.max_x = max(x for x, y in self.clay)

        self.queue = deque([(500, self.min_y)])

    def parse(self, text: list[str]) -> None:
        for line in text:
            axis, values = line.split(", ")
            fixed = int(axis[2:])
            start, end = map(int, values[2:].split(".."))
            for n in range(start, end + 1):
                self.clay.add((fixed, n) if axis[0] == "x" else (n, fixed))

    def free(self, x: int, y: int) -> bool:
        return (x, y) not in self.clay and (x, y) not in self.settled

    def run(self) -> None:
        while self.queue:
            x, y = self.queue.pop()

            if y > self.max_y: continue

            if self.free(x, y + 1):
                self.flowing.add((x, y))
                self.queue.append((x, y + 1))
            else:
                self.scan(x, y)

        self.flowing -= self.settled

    def scan(self, x: int, y: int) -> None:
        x0 = x - 1
        stop0 = True

        while self.free(x0, y):
            if self.free(x0, y + 1):
                x0 -= 1
                stop0 = False
                break
            x0 -= 1
        x0 += 1

        x1 = x + 1
        stop1 = True

        while self.free(x1, y):
            if self.free(x1, y + 1):
                x1 += 1
                stop1 = False
                break
            x1 += 1
        x1 -= 1

        if stop0 and stop1:
            for i in range(x0, x1 + 1):
                self.settled.add((i, y))

            if self.free(x, y - 1):
                self.queue.append((x, y - 1))

        else:
            for i in range(x0, x1 + 1):
                self.flowing.add((i, y))

            if self.free(x0, y + 1):
                self.queue.append((x0, y + 1))

            if self.free(x1, y + 1):
                self.queue.append((x1, y + 1))

    def countAll(self) -> int:
        return sum(self.min_y <= y <= self.max_y for x, y in self.settled | self.flowing)

    def countSettled(self) -> int:
        return sum(self.min_y <= y <= self.max_y for x, y in self.settled)

    def output(self) -> None:
        for y in range(self.min_y, self.max_y + 1):
            line = ""
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) in self.clay:
                    line += "#"
                elif (x, y) in self.settled:
                    line += "~"
                elif (x, y) in self.flowing:
                    line += "|"
                else:
                    line += "."
            print(line)
    
reservoir = Reservoir(data)
reservoir.run()
print(reservoir.countSettled())

print(f"Time Taken: {time()-t1:.2f}s")