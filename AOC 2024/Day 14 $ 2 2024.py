import re
from collections import defaultdict
from math import prod
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 14 2024.txt"
# FILE_NAME = "Day 14 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

WIDTH, HEIGHT = 101, 103
# WIDTH, HEIGHT = 11, 7

class Robot:
    def __init__(self, startPosition: tuple[int, int], velocity: tuple[int, int]) -> None:
        self.position = startPosition
        self.velocity = velocity
    def Move(self) -> None:
        x, y = ((self.position[i] + self.velocity[i])%[WIDTH, HEIGHT][i] for i in range(2))
        self.position = (x, y)
    
    def __str__(self) -> str:
        return f"Robot:\nPosition: {self.position}\nVelocity: {self.velocity}\n"
    def __repr__(self) -> str:
        return self.__str__()

def PrintRobots(robots: list[Robot]) -> None:
    locations: list[tuple[int, int]] = [robot.position for robot in robots]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            num = locations.count((x, y))
            print("#" if num else " ", end="")
        print()

def PrintRobotsInQuadrants(robots: list[Robot]) -> None:
    locations: list[tuple[int, int]] = [robot.position for robot in robots]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(locations.count((x, y)) if (x != WIDTH//2) and (y != HEIGHT//2) else " ", end="")
        print()

def GetQuadrant(x: int, y: int) -> int:
    return (
        0 if x < WIDTH // 2 and y < HEIGHT // 2 else
        1 if x < WIDTH // 2 and y > HEIGHT // 2 else
        2 if x > WIDTH // 2 and y < HEIGHT // 2 else
        3 if x > WIDTH // 2 and y > HEIGHT // 2 else
        4
    )

def NoOverlap(robots: list[Robot]) -> bool:
    locations: list[tuple[int, int]] = [robot.position for robot in robots]
    return len(locations) == len(set(locations))

robots: list[Robot] = [Robot((m[0], m[1]), (m[2], m[3])) for m in (list(map(int, re.findall(r"-?\b\d+\b", line))) for line in data)]
seconds = 0
while True:
    if NoOverlap(robots):
        print(f"Seconds: {seconds}")
        PrintRobots(robots)
        break
    for robot in robots: robot.Move()
    seconds += 1