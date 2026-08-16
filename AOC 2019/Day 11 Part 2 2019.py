from collections import defaultdict
from typing import Callable
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 11 2019.txt"
# FILE_NAME = "Day 11 2019 alt.txt"
# FILE_NAME = "Day 11 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, file.read().split(",")))
file.close()

class Computer:
    def __init__(self, data:list[int], outputFunc: Callable[[int], None]) -> None:
        self.data = data
        self.outputFunc = outputFunc
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
        dataLength = len(self.data)
        if index < dataLength:
            return self.data[index]
        self.data = self.data + [0 for _ in range(index-dataLength+1)]
        return self.data[index]
    def SetDatum(self, index: int, value: int) -> None:
        # self.data[index] = value
        # return
        dataLength = len(self.data)
        if index >= dataLength:
            self.data = self.data + [0 for _ in range(index-dataLength+1)]
        self.data[index] = value
    def GetInput(self) -> int:
        return int(input("Input: "))

    def Run(self, prog: list[int]|None = None, resetIndex: bool = True):
        if prog:
            self.data = prog
        if resetIndex:
            self.index = 0
        while self.data[self.index] != 99:
            opcode, mode1, mode2, mode3 = self.ParseInstruction(self.data[self.index])
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
                self.outputFunc(self.ReadValue(op1, mode1))
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

class EmergencyHullPaintingRobot(Computer):
    def __init__(self, data: list[int]) -> None:
        super().__init__(data, self.PaintOrMove)
        self.grid: defaultdict[tuple[int, int], int] = defaultdict(int)
        self.x = 0
        self.y = 0
        self.grid[(self.x, self.y)] = 1
        self.dirIndex = 0
        # Up, Right, Down, Left
        self.dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.painting = True
    
    def GetInput(self) -> int:
        return self.grid[(self.x, self.y)]

    def PaintOrMove(self, value: int) -> None:
        if self.painting:
            self.grid[(self.x, self.y)] = value
        else:
            # Left
            if value == 0:
                self.dirIndex = (self.dirIndex-1)%len(self.dirs)
            # Right
            else:
                self.dirIndex = (self.dirIndex+1)%len(self.dirs)
            dir = self.dirs[self.dirIndex]
            self.x += dir[0]
            self.y += dir[1]
        self.painting = not self.painting

emergencyHullPaintingRobot = EmergencyHullPaintingRobot(data)
emergencyHullPaintingRobot.Run()
minX, maxX = min([pos[0] for pos in emergencyHullPaintingRobot.grid.keys()]), max([pos[0] for pos in emergencyHullPaintingRobot.grid.keys()])
minY, maxY = min([pos[1] for pos in emergencyHullPaintingRobot.grid.keys()]), max([pos[1] for pos in emergencyHullPaintingRobot.grid.keys()])
for y in range(minY, maxY+1):
    for x in range(minX, maxX+1):
        print("#" if emergencyHullPaintingRobot.grid[(x, y)] else " ", end="")
    print()