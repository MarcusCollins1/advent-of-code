import re
from itertools import permutations
from math import lcm
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 12 2019.txt"
# FILE_NAME = "Day 12 2019 alt.txt"
# FILE_NAME = "Day 12 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Moon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]
    
    def TotalEnergy(self) -> int:
        return sum(map(abs, self.pos)) * sum(map(abs, self.vel))
    
    def Gravity(self, otherMoon:"Moon") -> None:
        for i in range(3):
            self.vel[i] += 1 if self.pos[i] < otherMoon.pos[i] else -1 if self.pos[i] > otherMoon.pos[i] else 0
    
    def Move(self) -> None:
        for i in range(3):
            self.pos[i] += self.vel[i]

pattern = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>"
moons: list[Moon] = []
for line in data:
    match = re.match(pattern, line)
    if match != None and isinstance(match.groups(), tuple) and len(match.groups()) == 3:
        moons.append(Moon(*map(int, match.groups())))

startPositions = [[moon.pos[i] for moon in moons] for i in range(3)]
startVelocities = [[moon.vel[i] for moon in moons] for i in range(3)]
repeatNumbers: list[int] = [0, 0, 0]
steps = 0
while not all(repeatNumbers):
    for moon1, moon2 in permutations(moons, 2):
        moon1.Gravity(moon2)
    for moon in moons:
        moon.Move()
    steps += 1
    # Check if positions have repeated
    for i in range(3):
        if repeatNumbers[i] > 0:
            continue
        if ([moon.pos[i] for moon in moons] == startPositions[i]) and ([moon.vel[i] for moon in moons] == startVelocities[i]):
            repeatNumbers[i] = steps
# print(repeatNumbers)
print(lcm(*repeatNumbers))
