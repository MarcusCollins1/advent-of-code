from time import time

t1 = time()

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 23 2016.txt"

# FILE_NAME = "Day 23 2016 test.txt"

with open(FOLDER_PATH + FILE_NAME, "r") as file:
    data = [x.strip() for x in file.readlines()]


class Computer:
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = instructions.copy()
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.index = 0

    def getValue(self, value: str) -> int:
        try:
            return int(value)
        except ValueError:
            return self.registers[value]

    def run(self) -> None:
        while 0 <= self.index < len(self.instructions):
            instruction = self.instructions[self.index].split()
            instructionName = instruction[0]

            if instructionName == "cpy":
                # cpy X Y
                # Y must be a register
                if instruction[2] in self.registers:
                    self.registers[instruction[2]] = self.getValue(instruction[1])

                self.index += 1

            elif instructionName == "inc":
                # inc X
                if instruction[1] in self.registers:
                    self.registers[instruction[1]] += 1

                self.index += 1

            elif instructionName == "dec":
                # dec X
                if instruction[1] in self.registers:
                    self.registers[instruction[1]] -= 1

                self.index += 1

            elif instructionName == "jnz":
                # jnz X Y
                if self.getValue(instruction[1]) == 0:
                    self.index += 1
                else:
                    self.index += self.getValue(instruction[2])

            elif instructionName == "tgl":
                # tgl X
                idx = self.index + self.getValue(instruction[1])

                if 0 <= idx < len(self.instructions):
                    target = self.instructions[idx].split()
                    targetName = target[0]

                    if len(target) == 2:
                        # inc -> dec
                        # dec -> inc
                        # tgl -> inc
                        if targetName == "inc":
                            target[0] = "dec"
                        else:
                            target[0] = "inc"

                    elif len(target) == 3:
                        # jnz -> cpy
                        # cpy -> jnz
                        if targetName == "jnz":
                            target[0] = "cpy"
                        else:
                            target[0] = "jnz"

                    self.instructions[idx] = " ".join(target)

                self.index += 1

            else:
                raise ValueError(f"Unknown instruction: {instructionName}")


computer = Computer(data)

# Day 23 Part 1
computer.registers["a"] = 7

computer.run()

print(computer.registers["a"])
print(f"Time taken: {time() - t1:.3f}s")