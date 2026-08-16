from time import time
t1 = time()
import re
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 10 2025.txt"
# FILE_NAME = "Day 10 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


class Machine:
    def __init__(self, line: str) -> None:
        pattern = r"\[(.*?)\]|\((.*?)\)|\{(.*?)\}"
        match = re.findall(pattern, line)
        if match:
            match: list[str] = [x for group in match for x in group if x]
            self.indicatorLightDiagram = match[0]
            self.buttonWiringSchematics = [[int(x) for x in item.split(",")] for item in match[1:-1]]
            self.joltageRequirements = [int(x) for x in match[-1].split(",")]
        else:
            raise ValueError("Invalid line")
    
    def pressButton(self, button: list[int], lights: str) -> str:
        lightsLst = list(lights)
        for idx in button:
            lightsLst[idx] = "#" if lights[idx] == "." else "."
        return "".join(lightsLst)
    
    def minNumPresses(self) -> int:
        queue: deque[tuple[str, int]] = deque()
        queue.append(("."*len(self.indicatorLightDiagram), 0))
        visited: set[str] = set()
        visited.add("."*len(self.indicatorLightDiagram))
        while queue:
            currLights, currPresses = queue.popleft()
            for presses in self.buttonWiringSchematics:
                newLights = self.pressButton(presses, currLights)
                if newLights == self.indicatorLightDiagram: return currPresses+1
                if newLights in visited: continue
                visited.add(newLights)
                queue.append((newLights, currPresses+1))
        return -1

machines: list[Machine] = [Machine(line) for line in data]

print(sum([machine.minNumPresses() for machine in machines]))


print(f"Time Taken: {time()-t1:.3f}s")