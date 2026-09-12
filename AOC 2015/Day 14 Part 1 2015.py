import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 14 2015.txt"
# FILE_NAME = "Day 14 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

NUM_SECONDS = 2503
# NUM_SECONDS = 1000

class Reindeer:
    def __init__(self, name: str, flySpeed: int, flyTime: int, restTime: int) -> None:
        self.name = name
        self.flySpeed = flySpeed
        self.flyTime = flyTime
        self.restTime = restTime

        self.distance = 0
        self.isFlying = True
        self.timeInState = 0
    def iterate(self) -> None:
        self.distance += self.flySpeed if self.isFlying else 0
        self.timeInState += 1
        if (self.timeInState >= self.flyTime and self.isFlying) or (self.timeInState >= self.restTime and not self.isFlying):
            self.isFlying = not self.isFlying
            self.timeInState = 0
    def __repr__(self) -> str:
        return f"{self.name}, {self.distance}"

def getReindeerFromLine(line: str) -> Reindeer:
    pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    match = re.match(pattern, line)
    if match != None:
        name, speed, fTime, rTime = match.groups()
        return Reindeer(name, int(speed), int(fTime), int(rTime))
    raise Exception("line in incorrect format")

reindeers: list[Reindeer] = [getReindeerFromLine(line) for line in data]

for _ in range(NUM_SECONDS):
    for r in reindeers: r.iterate()
print(max(r.distance for r in reindeers))