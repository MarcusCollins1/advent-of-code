import re
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 13 2024.txt"
# FILE_NAME = "Day 13 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip().splitlines() for x in file.read().split("\n\n")]
file.close()

A_COST, B_COST = 3, 1

class Button:
    def __init__(self, dx: int, dy: int, cost: int) -> None:
        self.dx = dx
        self.dy = dy
        self.cost = cost
    
    def __str__(self) -> str:
        return f"dx: {self.dx} | dy: {self.dy} | cost: {self.cost}"
    def __repr__(self) -> str:
        return self.__str__()

class Machine:
    def __init__(self, aButton: Button, bButton: Button, prizeLocation: tuple[int, int]) -> None:
        self.aButton = aButton
        self.bButton = bButton
        self.prizeLocation = prizeLocation
    
    def MinCostToWin(self) -> int:
        waysToPrize: set[tuple[int, int]] = set()
        for numAPresses in range(101):
            for numBPresses in range(101):
                x = self.aButton.dx * numAPresses + self.bButton.dx * numBPresses
                y = self.aButton.dy * numAPresses + self.bButton.dy * numBPresses
                if (x, y) == self.prizeLocation: waysToPrize.add((numAPresses, numBPresses))
        if len(waysToPrize) == 0: return 0
        return min([a*self.aButton.cost + b*self.bButton.cost for a, b in waysToPrize])
    
    def __str__(self) -> str:
        return f"Machine:\nA Button: {self.aButton}\nB Button: {self.bButton}\nPrize: {self.prizeLocation}\n"
    def __repr__(self) -> str:
        return self.__str__()

def GetMachine(data: list[str]) -> Machine:
    pattern = r'(\d+)'
    aMatches = list(map(int, re.findall(pattern, data[0])))
    buttonA = Button(aMatches[0], aMatches[1], A_COST)
    bMatches = list(map(int, re.findall(pattern, data[1])))
    buttonB = Button(bMatches[0], bMatches[1], B_COST)
    prizeMatches = list(map(int, re.findall(pattern, data[2])))
    return Machine(buttonA, buttonB, (prizeMatches[0], prizeMatches[1]))
    

print(sum([GetMachine(d).MinCostToWin() for d in data]))
# print(*[GetMachine(d) for d in data], sep="\n")