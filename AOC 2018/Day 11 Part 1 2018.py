FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 11 2018.txt"
# FILE_NAME = "Day 11 2018 alt.txt"
# FILE_NAME = "Day 11 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
gridSerialNumber = int(file.read().strip())
file.close()

class Grid:
    def __init__(self, serialNumber: int) -> None:
        self.serialNumber = serialNumber
        self.grid = self.MakeGrid()
    
    def MakeGrid(self) -> list[list[int]]:
        grid: list[list[int]] = []
        for y in range(1, 301):
            row: list[int] = []
            for x in range(1, 301):
                rackID = x + 10
                powerLevel = rackID * y
                powerLevel += self.serialNumber
                powerLevel *= rackID
                powerLevel = 0 if powerLevel < 100 else int(str(powerLevel)[-3])
                powerLevel -= 5
                row.append(powerLevel)
            grid.append(row)
        return grid
    
    def __getitem__(self, index: tuple[int, int]) -> int:
        x, y = index
        return self.grid[y-1][x-1 ]

grid = Grid(gridSerialNumber)

greatestFuel: int = 0
topLeft: tuple[int, int] = (0, 0)

for y in range(1, 299):
    for x in range(1, 299):
        total = sum([grid[x+x_, y+y_] for x_ in range(3) for y_ in range(3)])
        if total > greatestFuel:
            greatestFuel = total
            topLeft = (x, y)
print(f"{topLeft[0]},{topLeft[1]}")