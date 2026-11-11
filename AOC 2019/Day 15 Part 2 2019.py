from time import time
t1 = time()
from collections import defaultdict, deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 15 2019.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Intcode:
    def __init__(self, program: list[int]) -> None:
        self.memory = defaultdict(int, enumerate(program))
        self.pointer: int = 0
        self.relativeBase: int = 0
        self.halted: bool = False

    def copy(self) -> "Intcode":
        computer = Intcode([])
        computer.memory = self.memory.copy()
        computer.pointer = self.pointer
        computer.relativeBase = self.relativeBase
        computer.halted = self.halted
        return computer

    def run(self, inputValue: int) -> int:
        while not self.halted:
            instruction = self.memory[self.pointer]
            opcode = instruction % 100

            modes = [instruction // 100 % 10, instruction // 1000 % 10, instruction // 10000 % 10]

            def read(n) -> int:
                value = self.memory[self.pointer + n]
                mode = modes[n - 1]

                if mode == 0:
                    return self.memory[value]
                if mode == 1:
                    return value
                if mode == 2:
                    return self.memory[self.relativeBase + value]

                raise ValueError("Invalid parameter mode")

            def address(n) -> int:
                value = self.memory[self.pointer + n]
                mode = modes[n - 1]

                if mode == 0:
                    return value
                if mode == 2:
                    return self.relativeBase + value

                raise ValueError("Invalid write mode")

            if opcode == 99:
                self.halted = True
                break

            elif opcode == 1:
                self.memory[address(3)] = read(1) + read(2)
                self.pointer += 4

            elif opcode == 2:
                self.memory[address(3)] = read(1) * read(2)
                self.pointer += 4

            elif opcode == 3:
                self.memory[address(1)] = inputValue
                self.pointer += 2

            elif opcode == 4:
                output = read(1)
                self.pointer += 2
                return output

            elif opcode == 5:
                self.pointer = read(2) if read(1) != 0 else self.pointer + 3

            elif opcode == 6:
                self.pointer = read(2) if read(1) == 0 else self.pointer + 3

            elif opcode == 7:
                self.memory[address(3)] = int(read(1) < read(2))
                self.pointer += 4

            elif opcode == 8:
                self.memory[address(3)] = int(read(1) == read(2))
                self.pointer += 4

            elif opcode == 9:
                self.relativeBase += read(1)
                self.pointer += 2

            else:
                raise ValueError(f"Unknown opcode: {opcode}")

        raise RuntimeError("Intcode halted without output")

class Solver:
    def __init__(self, data: list[str]) -> None:
        self.program = list(map(int, data[0].split(",")))

    def solve(self) -> int:
        directions = {
            1: (0, -1),
            2: (0, 1),
            3: (-1, 0),
            4: (1, 0)
        }

        computer = Intcode(self.program)

        queue = deque([(0, 0, computer)])
        visited = {(0, 0)}
        openSpaces = {(0, 0)}
        oxygen = None

        # EXPLORE THE ENTIRE  MAZE
        while queue:
            x, y, computer = queue.popleft()

            for command, (dx, dy) in directions.items():
                nx = x + dx
                ny = y + dy

                if (nx, ny) in visited: continue

                visited.add((nx, ny))

                newComputer = computer.copy()
                result = newComputer.run(command)

                if result == 0:
                    continue

                openSpaces.add((nx, ny))

                if result == 2:
                    oxygen = (nx, ny)

                queue.append((nx, ny, newComputer))

        if oxygen is None: return -1

        # SPREAD OXYGEN THROUGH THE MAZE
        queue = deque([(oxygen[0], oxygen[1], 0)])
        visited = {oxygen}
        maxMinutes = 0

        while queue:
            x, y, minutes = queue.popleft()
            maxMinutes = max(maxMinutes, minutes)

            for dx, dy in directions.values():
                nx = x + dx
                ny = y + dy

                if (nx, ny) not in openSpaces: continue

                if (nx, ny) in visited: continue

                visited.add((nx, ny))
                queue.append((nx, ny, minutes + 1))

        return maxMinutes

solver = Solver(data)
print(solver.solve())

print(f"Time Taken: {time()-t1:.2f}s")