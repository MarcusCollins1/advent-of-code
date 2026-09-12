from time import time

t1 = time()

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 23 2016.txt"

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

    def tryOptimize(self) -> bool:
        """
        Optimise:

            cpy b c
            inc a
            dec c
            jnz c -2
            dec d
            jnz d -5

        into:

            a += b * d
            c = 0
            d = 0
        """

        if self.index + 5 >= len(self.instructions):
            return False

        if self.instructions[self.index:self.index + 6] == [
            "cpy b c",
            "inc a",
            "dec c",
            "jnz c -2",
            "dec d",
            "jnz d -5",
        ]:
            self.registers["a"] += (
                self.registers["b"] * self.registers["d"]
            )

            self.registers["c"] = 0
            self.registers["d"] = 0

            self.index += 6
            return True

        return False

    def run(self) -> None:
        while 0 <= self.index < len(self.instructions):

            # Skip the enormous multiplication loop
            if self.tryOptimize():
                continue

            instruction = self.instructions[self.index].split()
            instructionName = instruction[0]

            if instructionName == "cpy":
                if instruction[2] in self.registers:
                    self.registers[instruction[2]] = (
                        self.getValue(instruction[1])
                    )
                self.index += 1

            elif instructionName == "inc":
                if instruction[1] in self.registers:
                    self.registers[instruction[1]] += 1
                self.index += 1

            elif instructionName == "dec":
                if instruction[1] in self.registers:
                    self.registers[instruction[1]] -= 1
                self.index += 1

            elif instructionName == "jnz":
                if self.getValue(instruction[1]) == 0:
                    self.index += 1
                else:
                    self.index += self.getValue(instruction[2])

            elif instructionName == "tgl":
                idx = self.index + self.getValue(instruction[1])

                # tgl outside the program does nothing
                if 0 <= idx < len(self.instructions):
                    target = self.instructions[idx].split()

                    if len(target) == 2:
                        # inc -> dec
                        # everything else -> inc
                        if target[0] == "inc":
                            target[0] = "dec"
                        else:
                            target[0] = "inc"

                    elif len(target) == 3:
                        # jnz -> cpy
                        # everything else -> jnz
                        if target[0] == "jnz":
                            target[0] = "cpy"
                        else:
                            target[0] = "jnz"

                    self.instructions[idx] = " ".join(target)

                self.index += 1

            else:
                raise ValueError(
                    f"Unknown instruction: {instructionName}"
                )


computer = Computer(data)

# Part 1: 7
# Part 2: 12
computer.registers["a"] = 12

computer.run()

print("Registers:", computer.registers)
print("Answer:", computer.registers["a"])
print(f"Time taken: {time() - t1:.3f}s")