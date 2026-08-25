from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 20 2017.txt"
# FILE_NAME = "Day 20 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Particle:
    def __init__(self, pos: tuple[int, int, int], vel: tuple[int, int, int], acc: tuple[int, int, int]) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def tick(self) -> None:
        self.vel = tuple(self.vel[i] + self.acc[i] for i in range(3))
        self.pos = tuple(self.pos[i] + self.vel[i] for i in range(3))

    def distance(self) -> int:
        return sum(abs(x) for x in self.pos)

particles: list[Particle] = []

pattern = r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>"
for line in data:
    match = re.match(pattern, line)
    if match:
        numbers: tuple[int, int, int, int, int, int, int, int, int] = tuple(map(int, match.groups())) # type: ignore
        particles.append(Particle(numbers[0:3], numbers[3:6], numbers[6:9]))



for _ in range(1000):
    for p in particles: p.tick()

closest = min(range(len(particles)), key=lambda i: particles[i].distance())

print(closest)

print(f"Time Taken: {time()-t1:.2f}s")