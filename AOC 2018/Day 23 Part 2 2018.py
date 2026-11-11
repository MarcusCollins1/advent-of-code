from time import time
t1 = time()
import re
import heapq
from itertools import count
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 23 2018.txt"
# FILE_NAME = "Day 23 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

class Nanobot:
    def __init__(self, x: int, y: int, z: int, radius: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    @property
    def pos(self) -> tuple[int, int, int]: return (self.x, self.y, self.z)

    def inRange(self, otherBot: "Nanobot") -> bool:
        distance = abs(otherBot.x - self.x) + abs(otherBot.y - self.y) + abs(otherBot.z - self.z)
        return distance <= self.radius

    def intersectsCube(self, cube: "Cube") -> bool:
        distance = 0

        for botCoord, cubeCoord in zip(self.pos, cube.pos):
            minimum = cubeCoord
            maximum = cubeCoord + cube.size - 1

            distance += max(minimum - botCoord, 0, botCoord - maximum)

        return distance <= self.radius

    def __str__(self) -> str:
        return f"pos=<{self.x},{self.y},{self.z}>, r={self.radius}"

    def __repr__(self) -> str:
        return self.__str__()

class Cube:
    def __init__(self, x: int, y: int, z: int, size: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.size = size

    @property
    def pos(self) -> tuple[int, int, int]: return (self.x, self.y, self.z)

    def distanceToOrigin(self) -> int:
        def axisDistance(v: int) -> int:
            return max(v, 0, -v - self.size + 1)

        return axisDistance(self.x) + axisDistance(self.y) + axisDistance(self.z)

    def subdivide(self) -> list["Cube"]:
        if self.size == 1: return []

        half = self.size // 2
        return [Cube(self.x + dx, self.y + dy, self.z + dz, half) for dx in (0, half) for dy in (0, half) for dz in (0, half)]

class Solver:
    def __init__(self, data: str) -> None:
        self.bots: list[Nanobot] = self.parseData(data)

    def parseData(self, data: str) -> list[Nanobot]:
        pattern = r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)"
        return [Nanobot(*map(int, match)) for match in re.findall(pattern, data)] # type: ignore

    def countBots(self, cube: Cube) -> int:
        return sum(bot.intersectsCube(cube) for bot in self.bots)

    def initialCube(self) -> Cube:
        minX = min(bot.x - bot.radius for bot in self.bots)
        maxX = max(bot.x + bot.radius for bot in self.bots)

        minY = min(bot.y - bot.radius for bot in self.bots)
        maxY = max(bot.y + bot.radius for bot in self.bots)

        minZ = min(bot.z - bot.radius for bot in self.bots)
        maxZ = max(bot.z + bot.radius for bot in self.bots)

        size = 1
        while size < max(maxX - minX + 1, maxY - minY + 1, maxZ - minZ + 1):
            size *= 2

        return Cube(minX, minY, minZ, size)

    def solve(self) -> int:
        startCube = self.initialCube()

        queue = []
        counter = count()

        def addCube(cube: Cube) -> None:
            botsInRange = self.countBots(cube)
            heapq.heappush(queue, (-botsInRange, cube.distanceToOrigin(), cube.size, next(counter), cube))

        addCube(startCube)

        while queue:
            negCount, distance, size, _, cube = heapq.heappop(queue)

            if size == 1: return distance

            for smallerCube in cube.subdivide():
                addCube(smallerCube)
        raise RuntimeError("No solution found")

solver = Solver(data)
print(solver.solve())

print(f"Time Taken: {time()-t1:.2f}s")