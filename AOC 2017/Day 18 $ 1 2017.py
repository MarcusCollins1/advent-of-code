from time import time
t1 = time()
from collections import defaultdict
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 18 2017.txt"
# FILE_NAME = "Day 18 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Computer:
    def __init__(self, instructions: list[str]) -> None:
        self.registers = defaultdict(int)
        self.instructions = instructions

    def getValue(self, num: str) -> int:
        if num.replace("-","").isdigit(): return int(num)
        return self.registers[num]

    def run(self) -> int:
        currentIdx = 0
        lastPlayed: int|None = None
        while 0 <= currentIdx < len(self.instructions):
            currentInstruction = self.instructions[currentIdx].split()
            currentInstructionName = currentInstruction[0]
            if currentInstructionName == "snd":
                lastPlayed = self.getValue(currentInstruction[1])
                currentIdx += 1
            elif currentInstructionName == "set":
                self.registers[currentInstruction[1]] = self.getValue(currentInstruction[2])
                currentIdx += 1
            elif currentInstructionName == "add":
                self.registers[currentInstruction[1]] += self.getValue(currentInstruction[2])
                currentIdx += 1
            elif currentInstructionName == "mul":
                self.registers[currentInstruction[1]] *= self.getValue(currentInstruction[2])
                currentIdx += 1
            elif currentInstructionName == "mod":
                self.registers[currentInstruction[1]] %= self.getValue(currentInstruction[2])
                currentIdx += 1
            elif currentInstructionName == "rcv":
                if self.getValue(currentInstruction[1]) and lastPlayed: return lastPlayed
                currentIdx += 1
            elif currentInstructionName == "jgz":
                if self.getValue(currentInstruction[1]) > 0:
                    currentIdx += self.getValue(currentInstruction[2])
                else: currentIdx += 1
        return 0

computer = Computer(data)
print(computer.run())

print(f"Time Taken: {time()-t1:.2f}s")