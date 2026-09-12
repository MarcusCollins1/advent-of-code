from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 25 2016.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Computer:
    def __init__(self, instructions: list[str], startA: int) -> None:
        self.startA = startA
        self.instructions = instructions
        self.registers = {"a":startA, "b":0, "c":0, "d":0}
        self.index = 0
        self.expected = 0
        self.outputCount = 0
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
            elif instructionName == "out":
                val = self.getValue(instruction[1])
                self.outputCount += 1
                if self.outputCount > 100:
                    print(self.startA)
                    print(f"Time Taken: {time()-t1:.2f}s")
                    quit()
                if val != self.expected: break
                self.expected = 0 if val == 1 else 1
                self.index += 1

a = 0
while True:
    computer = Computer(data, a)
    computer.run()
    a+=1