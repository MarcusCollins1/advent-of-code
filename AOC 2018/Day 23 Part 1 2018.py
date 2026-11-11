from time import time
t1 = time()
import re
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

    def __str__(self) -> str:
        return f"pos=<{self.x},{self.y},{self.z}>, r={self.radius}"

    def __repr__(self) -> str:
        return self.__str__()


class Solver:
    def __init__(self, data: str) -> None:
        self.bots: list[Nanobot] = self.parseData(data)

    def parseData(self, data: str) -> list[Nanobot]:
        pattern = r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)"
        return [Nanobot(*map(int, match)) for match in re.findall(pattern, data)] # type: ignore

    def solve(self) -> int:
        strongestBot = max(self.bots, key= lambda bot: bot.radius)
        return sum(strongestBot.inRange(bot) for bot in self.bots)

solver = Solver(data)
print(solver.solve())

print(f"Time Taken: {time()-t1:.2f}s")