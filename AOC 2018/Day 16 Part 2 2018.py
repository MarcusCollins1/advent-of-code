from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 16 2018.txt"
# FILE_NAME = "Day 16 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

samplesText, programText = re.split(r"\n\s*\n\s*\n", data, maxsplit=1)

samples = []
for block in samplesText.split("\n\n"):
    before, instruction, after = block.splitlines()

    before = list(map(int, re.findall(r"\d+", before)))
    instruction = list(map(int, instruction.split()))
    after = list(map(int, re.findall(r"\d+", after)))

    samples.append((before, instruction, after))

program = [list(map(int, line.split())) for line in programText.splitlines()]


class Computer:
    def __init__(self, samples: list[tuple[list[int], list[int], list[int]]], program: list[list[int]]) -> None:
        self.samples = samples
        self.program = program

        self.registers: dict[int, int] = {i: 0 for i in range(4)}

        self.funs = [self.addr, self.addi, self.mulr, self.muli, self.banr, self.bani, self.borr, self.bori, self.setr, self.seti, self.gtir, self.gtri, self.gtrr, self.eqir, self.eqri, self.eqrr]

        self.possibilities = {i: self.funs.copy() for i in range(16)}

    # region: operations
    def addr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 3")
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = self.registers[a] + b

    def mulr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 3")
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = self.registers[a] * b

    def banr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 3")
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = self.registers[a] & b

    def borr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 3")
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = self.registers[a] | b

    def setr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = self.registers[a]

    def seti(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [c]):
            raise ValueError("Value of c must be between 0 and 3")
        self.registers[c] = a

    def gtir(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [b, c]):
            raise ValueError("Values of b and c must be between 0 and 3")
        self.registers[c] = 1 if a > self.registers[b] else 0

    def gtri(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = 1 if self.registers[a] > b else 0

    def gtrr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 3")
        self.registers[c] = 1 if self.registers[a] > self.registers[b] else 0

    def eqir(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [b, c]):
            raise ValueError("Values of b and c must be between 0 and 3")
        self.registers[c] = 1 if a == self.registers[b] else 0

    def eqri(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 3")
        self.registers[c] = 1 if self.registers[a] == b else 0

    def eqrr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 3")
        self.registers[c] = 1 if self.registers[a] == self.registers[b] else 0
    # endregion

    def testAllOperations1(self, before, instruction, after) -> int:
        passed = 0
        inst, a, b, c = instruction
        for fun in self.funs:
            # Reset registers
            for i in range(4):
                self.registers[i] = before[i]
            try:
                fun(a, b, c)
                if list(self.registers.values()) == after: passed += 1
            except: pass

        return passed

    def testAllOperations2(self, before, instruction, after) -> None:
        inst, a, b, c = instruction
        passed = []
        for fun in self.possibilities[inst]:
            # Reset registers
            for i in range(4): self.registers[i] = before[i]
            try:
                fun(a, b, c)
                if list(self.registers.values()) == after: passed.append(fun)
            except: pass
        self.possibilities[inst] = passed

    def SolvePart1(self) -> int:
        return sum(1 for sample in self.samples if self.testAllOperations1(*sample) >= 3)

    def SolvePart2(self) -> int:
        # Work out what each number means
        for before, instruction, after in self.samples:
            self.testAllOperations2(before, instruction, after)

        while any(len(poss) > 1 for poss in self.possibilities.values()):
            known = {poss[0] for poss in self.possibilities.values() if len(poss) == 1}
            for inst in self.possibilities:
                if len(self.possibilities[inst]) > 1:
                    self.possibilities[inst] = [fun for fun in self.possibilities[inst] if fun not in known]

        # Reset all registers
        for i in range(4): self.registers[i] = 0

        for inst, a, b, c in program:
            self.possibilities[inst][0](a, b, c)

        return self.registers[0]

computer = Computer(samples, program)

print(computer.SolvePart2())

print(f"Time Taken: {time()-t1:.2f}s")