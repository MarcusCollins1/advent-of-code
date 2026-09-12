from itertools import permutations
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 07 2019.txt"
# FILE_NAME = "Day 07 2019 alt.txt"
# FILE_NAME = "Day 07 2019 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, file.read().split(",")))
file.close()

class Amplifier:
    def __init__(self, mode: int, intCode: list[int]) -> None:
        self.mode = mode
        self.intCode = intCode
        self.firstIn = True
        self.finished = False
        self.index = 0
    
    def Amplify(self, inputValue: int) -> int | None:
        while not self.finished:
            instruction = self.intCode[self.index]
            instructionString = str(instruction)
            instructionString = "0" * (4-len(instructionString)) + instructionString
            mode1 = int(instructionString[1])
            mode2 = int(instructionString[0])
            if instructionString.endswith("1"):
                pos1, pos2, pos3 = self.intCode[self.index+1:self.index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = num1 + num2
                self.index += 4
            elif instructionString.endswith("2"):
                pos1, pos2, pos3 = self.intCode[self.index+1:self.index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = num1 * num2
                self.index += 4
            elif instructionString.endswith("3"):
                if self.firstIn:
                    self.intCode[self.intCode[self.index + 1]] = self.mode
                    self.firstIn = False
                else:
                    self.intCode[self.intCode[self.index + 1]] = inputValue
                self.index += 2
            elif instructionString.endswith("4"):
                loadAddress = self.intCode[self.index+1]
                self.index += 2
                return self.intCode[loadAddress]
            elif instructionString.endswith("5"):
                pos1, pos2 = self.intCode[self.index+1:self.index+3]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                if num1:
                    self.index = self.intCode[pos2] if mode2 == 0 else pos2
                else:
                    self.index += 3
            elif instructionString.endswith("6"):
                pos1, pos2 = self.intCode[self.index+1:self.index+3]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                if not num1:
                    self.index = self.intCode[pos2] if mode2 == 0 else pos2
                else:
                    self.index += 3
            elif instructionString.endswith("7"):
                pos1, pos2, pos3 = self.intCode[self.index+1:self.index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = 1 if num1 < num2 else 0
                self.index += 4
            elif instructionString.endswith("8"):
                pos1, pos2, pos3 = self.intCode[self.index+1:self.index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = 1 if num1 == num2 else 0
                self.index += 4
            elif instructionString.endswith("99"):
                self.finished = True

greatest = 0
for comb in permutations([5, 6, 7, 8, 9], 5):
    signal = 0
    lastValid = None
    amplifiers = [Amplifier(phase, data[:]) for phase in comb]
    while not all([amplifier.finished for amplifier in amplifiers]):
        for i in range(5):
            signal = amplifiers[i].Amplify(signal)
            # print(signal)
            if signal is not None:
                lastValid = signal
    # quit()
    
    greatest = max([lastValid, greatest])
    
print(greatest)