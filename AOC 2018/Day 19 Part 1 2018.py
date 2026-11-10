from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 19 2018.txt"
# FILE_NAME = "Day 19 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Computer:
    def __init__(self, data: list[str]) -> None:
        self.registers: dict[int, int] = {i: 0 for i in range(6)}
        self.boundRegisterKey: int = 0
        self.instructions: list[tuple] = []

        self.STRING_FUNCTION = {"addr": self.addr, "addi": self.addi, "mulr": self.mulr, "muli": self.muli, "banr": self.banr, "bani": self.bani, "borr": self.borr, "bori": self.bori, "setr": self.setr, "seti": self.seti, "gtir": self.gtir, "gtri": self.gtri, "gtrr": self.gtrr, "eqir": self.eqir, "eqri": self.eqri, "eqrr": self.eqrr}

        self.parseData(data)

    def parseData(self, data: list[str]) -> None:
        binding = data[0]
        self.instructions = []
        for line in data[1:]:
            inst, a, b, c = line.split()
            self.instructions.append((self.STRING_FUNCTION[inst], int(a), int(b), int(c)))

        match = re.search(r"#ip\s+(\d+)", binding)
        if match:
            self.boundRegisterKey = int(match.group(1))
        else:
            raise ValueError("Binding does not match #ip 0")

    # region: operations
    def addr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 5")
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = self.registers[a] + b

    def mulr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 5")
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = self.registers[a] * b

    def banr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 5")
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = self.registers[a] & b

    def borr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 5")
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = self.registers[a] | b

    def setr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = self.registers[a]

    def seti(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [c]):
            raise ValueError("Value of c must be between 0 and 5")
        self.registers[c] = a

    def gtir(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [b, c]):
            raise ValueError("Values of b and c must be between 0 and 5")
        self.registers[c] = 1 if a > self.registers[b] else 0

    def gtri(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = 1 if self.registers[a] > b else 0

    def gtrr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 5")
        self.registers[c] = 1 if self.registers[a] > self.registers[b] else 0

    def eqir(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [b, c]):
            raise ValueError("Values of b and c must be between 0 and 5")
        self.registers[c] = 1 if a == self.registers[b] else 0

    def eqri(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, c]):
            raise ValueError("Values of a and c must be between 0 and 5")
        self.registers[c] = 1 if self.registers[a] == b else 0

    def eqrr(self, a: int, b: int, c: int) -> None:
        if not all(x in self.registers.keys() for x in [a, b, c]):
            raise ValueError("Values must be between 0 and 5")
        self.registers[c] = 1 if self.registers[a] == self.registers[b] else 0
    # endregion

    @property
    def index(self) -> int:
        return self.registers[self.boundRegisterKey]

    def run(self) -> int:
        while 0 <= self.index < len(self.instructions):
            inst, a, b, c = self.instructions[self.index]
            # print(f"ip={self.index} {list(self.registers.values())} {inst.__name__} {a} {b} {c}", end="")
            inst(a, b, c)
            # print(list(self.registers.values()))
            self.registers[self.boundRegisterKey] += 1
        return self.registers[0]

computer = Computer(data)
answer = computer.run()
print(answer)

print(f"Time Taken: {time()-t1:.2f}s")