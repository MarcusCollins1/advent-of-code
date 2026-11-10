from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 21 2018.txt"

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

    def run(self) -> int:
        ip = 0

        seen = set()
        first = None

        haltIp = None
        haltRegister = None

        for i, (inst, a, b, c) in enumerate(self.instructions):
            if inst.__name__ == "eqrr" and (a == 0 or b == 0):
                haltIp = i
                haltRegister = b if a == 0 else a
                break

        if haltIp is None or haltRegister is None:
            raise ValueError("No eqrr instruction compares register 0")

        while 0 <= ip < len(self.instructions):
            if ip == haltIp:
                value = self.registers[haltRegister]

                if first is None:
                    first = value

                if value in seen:
                    return first

                seen.add(value)

            self.registers[self.boundRegisterKey] = ip

            inst, a, b, c = self.instructions[ip]
            inst(a, b, c)

            ip = self.registers[self.boundRegisterKey] + 1
        return first if first else 0

    def runOptimised(self) -> int:
        first = None

        r3 = 0

        while True:
            r1 = r3 | 65536
            r3 = 14906355

            while True:
                r3 += r1 & 255
                r3 &= 16777215
                r3 *= 65899
                r3 &= 16777215

                if r1 < 256: break

                r1 //= 256

            if first is None: first = r3
            return r3

computer = Computer(data)
print(computer.runOptimised())

print(f"Time Taken: {time()-t1:.2f}s")