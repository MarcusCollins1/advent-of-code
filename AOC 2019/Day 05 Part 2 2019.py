FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 05 2019.txt"
FILE_NAME = "Day 05 2019 alt.txt"
# FILE_NAME = "Day 05 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, file.read().split(",")))
file.close()

index = 0
while True:
    instruction = data[index]
    instructionString = str(instruction)
    instructionString = "0" * (5-len(instructionString)) + instructionString
    mode1 = int(instructionString[2])
    mode2 = int(instructionString[1])
    mode3 = int(instructionString[0])
    if instructionString.endswith("1"):
        pos1, pos2, pos3 = data[index+1:index+4]
        num1 = data[pos1] if mode1 == 0 else pos1
        num2 = data[pos2] if mode2 == 0 else pos2
        data[pos3] = num1 + num2
        index += 4
    elif instructionString.endswith("2"):
        pos1, pos2, pos3 = data[index+1:index+4]
        num1 = data[pos1] if mode1 == 0 else pos1
        num2 = data[pos2] if mode2 == 0 else pos2
        num3 = data[pos3] if mode3 == 0 else pos3
        data[pos3] = num1 * num2
        index += 4
    elif instructionString.endswith("3"):
        num = int(input())
        saveAddress = data[index + 1]
        data[saveAddress] = num
        index += 2
    elif instructionString.endswith("4"):
        saveAddress = data[index + 1]
        print(data[saveAddress] if mode1 == 0 else saveAddress)
        index += 2
    elif instructionString.endswith("5"):
        pos1, pos2 = data[index+1:index+3]
        num1 = data[pos1] if mode1 == 0 else pos1
        if num1:
            index = data[pos2] if mode2 == 0 else pos2
        else:
            index += 3
    elif instructionString.endswith("6"):
        pos1, pos2 = data[index+1:index+3]
        num1 = data[pos1] if mode1 == 0 else pos1
        if not num1:
            index = data[pos2] if mode2 == 0 else pos2
        else:
            index += 3
    elif instructionString.endswith("7"):
        pos1, pos2, pos3 = data[index+1:index+4]
        num1 = data[pos1] if mode1 == 0 else pos1
        num2 = data[pos2] if mode2 == 0 else pos2
        data[pos3] = 1 if num1 < num2 else 0
        index += 4
    elif instructionString.endswith("8"):
        pos1, pos2, pos3 = data[index+1:index+4]
        num1 = data[pos1] if mode1 == 0 else pos1
        num2 = data[pos2] if mode2 == 0 else pos2
        data[pos3] = 1 if num1 == num2 else 0
        index += 4
    elif instructionString.endswith("99"):
        quit()