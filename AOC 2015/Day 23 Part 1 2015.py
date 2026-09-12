FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 23 2015.txt"
# FILE_NAME = "Day 23 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Computer:
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = instructions
        self.registers = {"a": 0, "b": 0}
        self.pointer = 0
    
    def run(self) -> dict[str, int]:
        while 0 <= self.pointer < len(self.instructions):
            line = self.instructions[self.pointer]
            instruction, *arguments = line.replace(",","").split()
            if instruction == "hlf":
                self.registers[arguments[0]] //= 2
                self.pointer += 1
            elif instruction == "tpl":
                self.registers[arguments[0]] *= 3
                self.pointer += 1
            elif instruction == "inc":
                self.registers[arguments[0]] += 1
                self.pointer += 1
            elif instruction == "jmp":
                self.pointer += int(arguments[0])
            elif instruction == "jie":
                if self.registers[arguments[0]] % 2 == 0:
                    self.pointer += int(arguments[1])
                else:
                    self.pointer += 1
            elif instruction == "jio":
                if self.registers[arguments[0]] == 1:
                    self.pointer += int(arguments[1])
                else:
                    self.pointer += 1
        return self.registers

computer = Computer(data)
registers = computer.run()
print(f"Register a: {registers['a']}, Register b: {registers['b']}")