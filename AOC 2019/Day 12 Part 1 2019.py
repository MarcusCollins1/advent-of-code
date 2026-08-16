import re
from itertools import permutations
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 12 2019.txt"
# FILE_NAME = "Day 12 2019 alt.txt"
# FILE_NAME = "Day 12 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Moon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.velX = 0
        self.velY = 0
        self.velZ = 0
    
    def Gravity(self, otherMoon: "Moon") -> None:
        # x
        self.velX += 0 if self.x == otherMoon.x else 1 if self.x < otherMoon.x else -1
        # y
        self.velY += 0 if self.y == otherMoon.y else 1 if self.y < otherMoon.y else -1
        # z
        self.velZ += 0 if self.z == otherMoon.z else 1 if self.z < otherMoon.z else -1
    
    def Move(self) -> None:
        # x
        self.x += self.velX
        # y
        self.y += self.velY
        # z
        self.z += self.velZ
    
    def TotalEnergy(self) -> int:
        potentialEnergy = sum([abs(self.x), abs(self.y), abs(self.z)])
        kineticEnergy = sum([abs(self.velX), abs(self.velY), abs(self.velZ)])
        return potentialEnergy * kineticEnergy

    def __str__(self) -> str:
        return f"Moon:\nx:{self.x}\ny:{self.y}\nz:{self.z}\nx velocity:{self.velX}\ny velocity:{self.velY}\nz velocity:{self.velZ}\n"
    def __repr__(self) -> str:
        return f"Moon:\nx:{self.x}\ny:{self.y}\nz:{self.z}\nx velocity:{self.velX}\ny velocity:{self.velY}\nz velocity:{self.velZ}\n"

pattern = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>"
moons: list[Moon] = []
for line in data:
    match = re.match(pattern, line)
    if match != None and isinstance(match.groups(), tuple) and len(match.groups()) == 3:
        moons.append(Moon(*map(int, match.groups())))


numSteps = 1000
for _ in range(numSteps):
    # Apply gravity
    for moon1, moon2 in permutations(moons, 2):
        moon1.Gravity(moon2)
    # Move
    for moon in moons:
        moon.Move()
totalEnergy = sum([moon.TotalEnergy() for moon in moons])
print(totalEnergy)