from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 12 2016.txt"
# FILE_NAME = "Day 12 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Computer:
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = instructions
        self.registers = {"a":0, "b":0, "c":0, "d":0}
        self.index = 0
    def getValue(self, value: str) -> int:
        try:
            int(value)
            return int(value)
        except:
            return self.registers[value]
    def run(self) -> None:
        while 0 <= self.index < len(self.instructions):
            instruction = self.instructions[self.index].split()
            instructionName = instruction[0]
            if instructionName == "cpy":
                self.registers[instruction[2]] = self.getValue(instruction[1])
                self.index += 1
            elif instructionName == "inc":
                self.registers[instruction[1]] += 1
                self.index += 1
            elif instructionName == "dec":
                self.registers[instruction[1]] -= 1
                self.index += 1
            elif instructionName == "jnz":
                if self.getValue(instruction[1]) == 0: self.index += 1
                else: self.index += self.getValue(instruction[2])
        print(self.registers["a"])

computer = Computer(data)
computer.run()

print(f"Time taken: {time()-t1:.3f}s")