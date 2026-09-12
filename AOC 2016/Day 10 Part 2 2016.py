import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 10 2016.txt"
# FILE_NAME = "Day 10 2016 alt.txt"
# FILE_NAME = "Day 10 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Bot:
    def __init__(self, number: int, giveLowTo: tuple[str,int], giveHighTo: tuple[str,int]) -> None:
        self.number = number
        self.low: int|None = None
        self.high: int|None = None
        self.giveLowTo = giveLowTo
        self.giveHighTo = giveHighTo
    
    def receive(self, value: int) -> None:
        global bots, outputs
        if self.low == None: self.low = value
        else:
            if value < self.low: self.low, self.high = value, self.low
            else: self.high = value
            if self.giveLowTo[0] == "bot": bots[self.giveLowTo[1]].receive(self.low)
            else: outputs[self.giveLowTo[1]] = self.low
            self.low = None
            if self.giveHighTo[0] == "bot": bots[self.giveHighTo[1]].receive(self.high)
            else: outputs[self.giveHighTo[1]] = self.high
            self.high = None
    
    def __str__(self) -> str:
        return f"Bot: {self.number}\nLow: {self.low}\nHigh: {self.high}\nGive low to: {self.giveLowTo}\nGive high to: {self.giveHighTo}"

bots: dict[int, Bot] = dict()
outputs: dict[int, int] = dict()
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
            bots[botNum] = Bot(botNum, (botOutputLow, lowNum), (botOutputHigh, highNum))
    else:
        print("Unknown line start:", line)

for value, botNum in startingValues:
    bots[botNum].receive(value)

print(outputs[0] * outputs[1] * outputs[2])