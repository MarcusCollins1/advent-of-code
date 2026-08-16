from typing import Callable
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 13 2019.txt"
# FILE_NAME = "Day 13 2019 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
intCode = list(map(int, file.read().split(",")))
file.close()

class Computer:
    def __init__(self, intCode:list[int]) -> None:
        self.intCode = intCode
        self.relativeBase = 0
        self.index = 0
    
    def ParseInstruction(self, instruction: int) -> tuple[int, int, int, int]:
        instructionString = str(instruction).zfill(5)
        opcode = int(instructionString[-2:])
        mode1 = int(instructionString[-3])
        mode2 = int(instructionString[-4])
        mode3 = int(instructionString[-5])
        return opcode, mode1, mode2, mode3
    def ReadValue(self, op: int, mode: int) -> int:
        if mode == 0:
            return self.GetDatum(op)
        elif mode == 1:
            return op
        elif mode == 2:
            return self.GetDatum(self.relativeBase + op)
        return -1
    def ReadWriteAddress(self, op: int, mode: int) -> int:
        if mode == 2:
            return self.relativeBase + op
        return op
    def GetValue(self, mode: int, value: int) -> int:
        # position mode
        if mode == 0:
            return self.GetDatum(value)
        # immediate mode
        elif mode == 1:
            return value
        # relative mode
        elif mode == 2:
            return self.GetDatum(self.relativeBase + value)
        return -1
    def GetDatum(self, index: int) -> int:
        # return self.data[index]
        dataLength = len(self.intCode)
        if index < dataLength:
            return self.intCode[index]
        self.intCode = self.intCode + [0 for _ in range(index-dataLength+1)]
        return self.intCode[index]
    def SetDatum(self, index: int, value: int) -> None:
        dataLength = len(self.intCode)
        if index >= dataLength:
            self.intCode = self.intCode + [0 for _ in range(index-dataLength+1)]
        self.intCode[index] = value
    def GetInput(self) -> int:
        return int(input("Input: "))
    def Output(self, value: int) -> None:
        print(value)
    def Final(self) -> None:
        return

    def Run(self, prog: list[int]|None = None, resetIndex: bool = True):
        if prog:
            self.intCode = prog
        if resetIndex:
            self.index = 0
        while self.intCode[self.index] != 99:
            opcode, mode1, mode2, mode3 = self.ParseInstruction(self.intCode[self.index])
            # Add
            if opcode == 1:
                op1, op2, op3 = self.GetDatum(self.index+1), self.GetDatum(self.index+2), self.GetDatum(self.index+3)
                self.SetDatum(self.ReadWriteAddress(op3, mode3), self.ReadValue(op1, mode1) + self.ReadValue(op2, mode2))
                self.index += 4
            # Multiply
            elif opcode == 2:
                op1, op2, op3 = self.GetDatum(self.index+1), self.GetDatum(self.index+2), self.GetDatum(self.index+3)
                self.SetDatum(self.ReadWriteAddress(op3, mode3), self.ReadValue(op1, mode1) * self.ReadValue(op2, mode2))
                self.index += 4
            # Input
            elif opcode == 3:
                op1 = self.GetDatum(self.index+1)
                self.SetDatum(self.ReadWriteAddress(op1, mode1), self.GetInput())
                self.index += 2
            # Output
            elif opcode == 4:
                op1 = self.GetDatum(self.index+1)
                self.Output(self.ReadValue(op1, mode1))
                self.index += 2
            # Jump-if
            elif opcode == 5:
                op1, op2 = self.GetDatum(self.index+1), self.GetDatum(self.index+2)
                if self.ReadValue(op1, mode1) != 0:
                    self.index = self.ReadValue(op2, mode2)
                else:
                    self.index += 3
            # Jump-if-not
            elif opcode == 6:
                op1, op2 = self.GetDatum(self.index+1), self.GetDatum(self.index+2)
                if self.ReadValue(op1, mode1) == 0:
                    self.index = self.ReadValue(op2, mode2)
                else:
                    self.index += 3
            # Less than
            elif opcode == 7:
                op1, op2, op3 = self.GetDatum(self.index+1), self.GetDatum(self.index+2), self.GetDatum(self.index+3)
                self.SetDatum(self.ReadWriteAddress(op3, mode3), 1 if self.ReadValue(op1, mode1) < self.ReadValue(op2, mode2) else 0)
                self.index += 4
            # Equal to
            elif opcode == 8:
                op1, op2, op3 = self.GetDatum(self.index+1), self.GetDatum(self.index+2), self.GetDatum(self.index+3)
                self.SetDatum(self.ReadWriteAddress(op3, mode3), 1 if self.ReadValue(op1, mode1) == self.ReadValue(op2, mode2) else 0)
                self.index += 4
            # Adjust relative base
            elif opcode == 9:
                op1 = self.GetDatum(self.index+1)
                self.relativeBase += self.ReadValue(op1, mode1)
                self.index += 2
        self.Final()

class BlockBreaker(Computer):
    def __init__(self, intCode: list[int]) -> None:
        super().__init__(intCode)
        self.screen: dict[tuple[int, int], int] = {}
        self.cycle = 0
        self.currX, self.currY = 0, 0
    
    def Output(self, value: int) -> None:
        if self.cycle == 0:
            self.currX = value
        elif self.cycle == 1:
            self.currY = value
        elif self.cycle == 2:
            self.screen[(self.currX, self.currY)] = value
        self.cycle = (self.cycle+1)%3
    
    def Final(self) -> None:
        print(f"Number of blocks: {list(self.screen.values()).count(2)}")

blockBreaker = BlockBreaker(intCode)
blockBreaker.Run()