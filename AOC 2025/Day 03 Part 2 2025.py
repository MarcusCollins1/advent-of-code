from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 03 2025.txt"
# FILE_NAME = "Day 03 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def getMaxJoltage(bank: list[int]) -> int:
    batteriesChosen = [max(bank[:-11])]
    batteriesChosenIndexes = [bank.index(batteriesChosen[-1])]
    for i in range(-10,1):
        if i == 0:
            batteriesChosen.append(max(bank[batteriesChosenIndexes[-1]+1:]))
            batteriesChosenIndexes.append(bank[batteriesChosenIndexes[-1]+1:].index(batteriesChosen[-1])+batteriesChosenIndexes[-1]+1)
        else:
            batteriesChosen.append(max(bank[batteriesChosenIndexes[-1]+1:i]))
            batteriesChosenIndexes.append(bank[batteriesChosenIndexes[-1]+1:i].index(batteriesChosen[-1])+batteriesChosenIndexes[-1]+1)
    return int("".join([str(b) for b in batteriesChosen]))

print(sum([getMaxJoltage(list(map(int, list(bank)))) for bank in data]))

print(f"Time Taken: {time()-t1:.3f}s")