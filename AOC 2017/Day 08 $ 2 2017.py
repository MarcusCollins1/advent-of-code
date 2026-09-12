from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 08 2017.txt"
# FILE_NAME = "Day 08 2017 alt.txt"
# FILE_NAME = "Day 08 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

registers: defaultdict[str, int] = defaultdict(int)
biggestRegisterValue = -float("inf")

for line in data:
    modifyRegister, incDec, changeBy, _, registerToCheck, symbol, number = line.split()
    changeBy, number = int(changeBy), int(number)
    registerToCheckValue = registers[registerToCheck]
    if eval(f"{registerToCheckValue}{symbol}{number}"):
        registers[modifyRegister] += changeBy if incDec == "inc" else -changeBy
    biggestRegisterValue = max([biggestRegisterValue, max(registers.values())])

print(biggestRegisterValue)