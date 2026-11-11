from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 25 2018.txt"
# FILE_NAME = "Day 25 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Solver:
    def __init__(self, data: list[str]) -> None:
        self.points = [tuple(map(int, line.split(","))) for line in data if line]

    def distance(self, a: tuple, b: tuple) -> int:
        return sum(abs(x-y) for x, y in zip(a, b))

    def solve(self) -> int:
        points = self.points.copy()

        constellations = 0

        while points:
            constellations += 1

            constellation = [points.pop()]

            i = 0
            while i < len(constellation):
                current = constellation[i]

                for point in points[:]:
                    if self.distance(current, point) <= 3:
                        constellation.append(point)
                        points.remove(point)
                
                i += 1
        return constellations

solver = Solver(data)
print(solver.solve())

print(f"Time Taken: {time()-t1:.2f}s")