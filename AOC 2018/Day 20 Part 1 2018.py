from time import time
t1 = time()
from collections import deque, defaultdict
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 20 2018.txt"
# FILE_NAME = "Day 20 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

class RegularMap:
    DIRECTIONS = {
        "N": (0, -1),
        "S": (0, 1),
        "E": (1, 0),
        "W": (-1, 0)
    }

    def __init__(self, regex: str) -> None:
        self.regex = regex.strip()
        self.graph = defaultdict(set)
        self.start = (0, 0)
        self.distances = {}

    def buildMap(self) -> None:
        positions = {self.start}
        stack = []

        for char in self.regex:
            if char in self.DIRECTIONS:
                dx, dy = self.DIRECTIONS[char]
                newPositions = set()

                for x, y in positions:
                    current = (x, y)
                    neighbor = (x+dx, y+dy)

                    # Doors connect rooms in both directions
                    self.graph[current].add(neighbor)
                    self.graph[neighbor].add(current)

                    newPositions.add(neighbor)
                positions = newPositions

            elif char == "(":
                # Save branch start and empty endpoints
                stack.append((positions.copy(), set()))

            elif char == "|":
                startPositions, ends = stack[-1]
                ends.update(positions)
                positions = startPositions.copy()

            elif char == ")":
                startPositions, ends = stack.pop()
                ends.update(positions)
                positions = ends
    
    def bfs(self) -> None:
        queue = deque([self.start])
        self.distances = {self.start: 0}

        while queue:
            current = queue.popleft()

            for neighbor in self.graph[current]:
                if neighbor not in self.distances:
                    self.distances[neighbor] = (self.distances[current] + 1)
                    queue.append(neighbor)

    def run(self) -> int:
        self.buildMap()
        self.bfs()
        return max(self.distances.values())

regularMap = RegularMap(data)
answer = regularMap.run()
print(answer)

print(f"Time Taken: {time()-t1:.2f}s")