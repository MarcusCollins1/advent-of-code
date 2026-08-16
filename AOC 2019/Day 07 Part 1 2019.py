from itertools import permutations
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 07 2019.txt"
# FILE_NAME = "Day 07 2019 alt.txt"
# FILE_NAME = "Day 07 2019 test 1.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, file.read().split(",")))
file.close()

class Amplifier:
    def __init__(self, mode: int, intCode: list[int]) -> None:
        self.mode = mode
        self.intCode = intCode
    
    def Amplify(self, inputValue: int) -> int:
        inputs = [self.mode, inputValue]
        index = 0
        while True:
            instruction = self.intCode[index]
            instructionString = str(instruction)
            instructionString = "0" * (4-len(instructionString)) + instructionString
            mode1 = int(instructionString[1])
            mode2 = int(instructionString[0])
            if instructionString.endswith("1"):
                pos1, pos2, pos3 = self.intCode[index+1:index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = num1 + num2
                index += 4
            elif instructionString.endswith("2"):
                pos1, pos2, pos3 = self.intCode[index+1:index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = num1 * num2
                index += 4
            elif instructionString.endswith("3"):
                num = inputs.pop(0)
                saveAddress = self.intCode[index+1]
                self.intCode[saveAddress] = num
                index += 2
            elif instructionString.endswith("4"):
                loadAddress = self.intCode[index+1]
                return self.intCode[loadAddress] if mode1 == 0 else loadAddress
            elif instructionString.endswith("5"):
                pos1, pos2 = self.intCode[index+1:index+3]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                if num1:
                    index = self.intCode[pos2] if mode2 == 0 else pos2
                else:
                    index += 3
            elif instructionString.endswith("6"):
                pos1, pos2 = self.intCode[index+1:index+3]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                if not num1:
                    index = self.intCode[pos2] if mode2 == 0 else pos2
                else:
                    index += 3
            elif instructionString.endswith("7"):
                pos1, pos2, pos3 = self.intCode[index+1:index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = 1 if num1 < num2 else 0
                index += 4
            elif instructionString.endswith("8"):
                pos1, pos2, pos3 = self.intCode[index+1:index+4]
                num1 = self.intCode[pos1] if mode1 == 0 else pos1
                num2 = self.intCode[pos2] if mode2 == 0 else pos2
                self.intCode[pos3] = 1 if num1 == num2 else 0
                index += 4
            elif instructionString.endswith("99"):
                quit()

greatest = 0
for a, b, c, d, e in permutations([0, 1, 2, 3, 4], 5):
    amplifierA = Amplifier(a, data)
    amplifierB = Amplifier(b, data)
    amplifierC = Amplifier(c, data)
    amplifierD = Amplifier(d, data)
    amplifierE = Amplifier(e, data)
    outputA = amplifierA.Amplify(0)
    outputB = amplifierB.Amplify(outputA)
    outputC = amplifierC.Amplify(outputB)
    outputD = amplifierD.Amplify(outputC)
    outputE = amplifierE.Amplify(outputD)
    greatest = max([greatest, outputE])
print(greatest)