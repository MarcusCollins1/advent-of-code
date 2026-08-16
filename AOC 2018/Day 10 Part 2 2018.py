import re
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 10 2018.txt"
FILE_NAME = "Day 10 2018 alt.txt"
# FILE_NAME = "Day 10 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Light:
    def __init__(self, pos: tuple[int, int], vel: tuple[int, int]) -> None:
        self.pos = pos
        self.vel = vel
    
    def Move(self) -> None:
        self.pos = (self.pos[0]+self.vel[0], self.pos[1]+self.vel[1])
    
    def GetPos(self) -> tuple[int, int]:
        return self.pos

lights: list[Light] = []

for line in data:
    numbers = list(map(int, re.findall(r"-?\d+", line)))
    if len(numbers) != 4:
        print(f"Couldn't process: {line}")
        quit()
    lights.append(Light((numbers[0], numbers[1]), (numbers[2], numbers[3])))

def PrintLights(positions: list[tuple[int, int]], minX: int, maxX: int, minY: int, maxY: int) -> None:
    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            print("#" if (x, y) in positions else " ", end="")
        print()

secs = 0
while True:
    positions = [light.GetPos() for light in lights]
    minX, maxX = min([pos[0] for pos in positions]), max([pos[0] for pos in positions])
    minY, maxY = min([pos[1] for pos in positions]), max([pos[1] for pos in positions])
    if (maxX - minX < 100) and (maxY - minY < 100):
        print(f"Seconds: {secs}")
        PrintLights(positions, minX, maxX, minY, maxY)
        if input() != "":
            quit()
    for light in lights:
        light.Move()
    secs += 1