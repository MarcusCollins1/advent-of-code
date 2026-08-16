from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 11 2018.txt"
# FILE_NAME = "Day 11 2018 alt.txt"
# FILE_NAME = "Day 11 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
gridSerialNumber = int(file.read().strip())
file.close()

def SummedAreaTable(serialNumber: int) -> defaultdict[tuple[int, int], int]:
    summedGrid: defaultdict[tuple[int, int], int] = defaultdict(int)
    for y in range(1, 301):
        for x in range(1, 301):
            rackID = x + 10
            powerLevel = rackID * y
            powerLevel += serialNumber
            powerLevel *= rackID
            powerLevel = 0 if powerLevel < 100 else int(str(powerLevel)[-3])
            powerLevel -= 5
            summedGrid[(x, y)] = powerLevel + summedGrid[(x-1, y)] + summedGrid[(x, y-1)] - summedGrid[(x-1, y-1)]
    return summedGrid

def GetAreaValue(grid: defaultdict[tuple[int, int], int], x: int, y: int, size: int) -> int:
    x0, y0, x1, y1 = x-1, y-1, x+size-1, y+size-1
    return grid[(x0, y0)] + grid[(x1, y1)] - grid[(x0, y1)] - grid[(x1, y0)]

def BestFuel(grid: defaultdict[tuple[int, int], int], size: int) -> tuple[int, int, int, int]:
    fuels: list[tuple[int, int, int, int]] = []
    for y in range(1, 302-size):
        for x in range(1, 302-size):
            fuel = GetAreaValue(grid, x, y, size)
            fuels.append((fuel, x, y, size))
    return max(fuels)

summedGrid: defaultdict[tuple[int, int], int] = SummedAreaTable(gridSerialNumber)

answer = max(BestFuel(summedGrid, size) for size in range(1, 301))
print(answer[1], answer[2], answer[3], sep=",")