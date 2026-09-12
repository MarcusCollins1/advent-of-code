import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 10 2016.txt"
# FILE_NAME = "Day 10 2016 alt.txt"
# FILE_NAME = "Day 10 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

TARGET = (2, 5) if FILE_NAME == "Day 10 2016 test.txt" else (17, 61)

class Bot:
    def __init__(self, number: int, giveLowTo: int|None = None, giveHighTo: int|None = None) -> None:
        self.number = number
        self.low: int|None = None
        self.high: int|None = None
        self.giveLowTo = giveLowTo
        self.giveHighTo = giveHighTo
    
    def receive(self, value: int) -> None:
        global bots, TARGET
        if self.low == None: self.low = value
        else:
            if value < self.low: self.low, self.high = value, self.low
            else: self.high = value
            if (self.low, self.high) == TARGET:
                print(self.number)
                quit()
            if self.giveLowTo != None:
                bots[self.giveLowTo].receive(self.low)
                self.low = None
            if self.giveHighTo != None:
                bots[self.giveHighTo].receive(self.high)
                self.high = None
    
    def __str__(self) -> str:
        return f"Bot: {self.number}\nLow: {self.low}\nHigh: {self.high}\nGive low to: {self.giveLowTo}\nGive high to: {self.giveHighTo}"

bots: dict[int, Bot] = dict()
startingValues:list[tuple[int, int]] = []
for line in data:
    if line[0] == "v":
        match = re.match(r'^value (\d+) goes to bot (\d+)$', line)
        if match:
            value, bot = map(int, match.groups())
            startingValues.append((value, bot))
    elif line[0] == "b":
        match = re.match(r'^bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', line)
        if match:
            botNum, botOutputLow, lowNum, botOutputHigh, highNum = match.groups()
            botNum, lowNum, highNum = int(botNum), int(lowNum), int(highNum)
            bots[botNum] = Bot(botNum, lowNum if botOutputLow == "bot" else None, highNum if botOutputHigh == "bot" else None)
    else:
        print("Unknown line start:", line)

for value, botNum in startingValues:
    bots[botNum].receive(value)