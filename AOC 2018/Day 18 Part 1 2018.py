from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 18 2018.txt"
# FILE_NAME = "Day 18 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


class Solver:
    def __init__(self, data: list[str]) -> None:
        # 0: Open ground, 1: Trees, 2: Lumberyard
        convert = {".": 0, "|": 1, "#": 2}
        self.state = [[convert[char] for char in line] for line in data]

        self.DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        self.HEIGHT = len(self.state)
        self.WIDTH = len(self.state[0])

    def nextStateForCell(self, x: int, y: int) -> int:
        counts = {0: 0, 1: 0, 2: 0}
        for direction in self.DIRECTIONS:
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < self.WIDTH and 0 <= ny < self.HEIGHT:
                counts[self.state[ny][nx]] += 1
        cell = self.state[y][x]
        if cell == 0:
            if counts[1] >= 3: return 1
        elif cell == 1:
            if counts[2] >= 3: return 2
        elif cell == 2:
            if counts[2] >= 1 and counts[1] >= 1: return 2
            else: return 0

        return cell

    def nextState(self) -> None:
        newState = [[self.nextStateForCell(x, y) for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.state = newState

    @property
    def currentAnswer(self) -> int:
        return sum(line.count(1) for line in self.state) * sum(line.count(2) for line in self.state)

    def display(self) -> None:
        convert = {0: ".", 1: "|", 2: "#"}
        for line in self.state:
            print("".join(convert[cell] for cell in line))

    def run(self, numTrials: int = 10) -> int:
        for _ in range(numTrials): self.nextState()
        return self.currentAnswer

solver = Solver(data)
answer = solver.run()
# solver.display()
print(answer)

print(f"Time Taken: {time()-t1:.2f}s")