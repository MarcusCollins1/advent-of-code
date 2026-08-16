from collections import defaultdict
from math import ceil
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 14 2019.txt"
FILE_NAME = "Day 14 2019 alt.txt"
# FILE_NAME = "Day 14 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


def OreRequired(fuel: int = 1) -> int:
    chemNeeds = defaultdict(int, {"FUEL": fuel})
    chemHave = defaultdict(int)
    numOre = 0
    while chemNeeds:
        item = list(chemNeeds.keys())[0]
        if chemNeeds[item] <= chemHave[item]:
            chemHave[item] -= chemNeeds[item]
            del chemNeeds[item]
            continue

        numNeeded = chemNeeds[item] - chemHave[item]
        del chemHave[item]
        del chemNeeds[item]
        numProduced = reactions[item]["out"]

        numReactions = ceil(numNeeded / numProduced)
        chemHave[item] += (numReactions * numProduced) - numNeeded
        for chem in reactions[item]["in"]:
            if chem == "ORE":
                numOre += reactions[item]["in"][chem] * numReactions
            else:
                chemNeeds[chem] += reactions[item]["in"][chem] * numReactions
    
    return numOre

reactions = {}
for line in data:
    reactantsString, product = line.split(" => ")
    productNum, productChem = product.split()
    reactants = {}
    for reactantString in reactantsString.split(", "):
        reactantNum, reactantChem = reactantString.split()
        reactants[reactantChem] = int(reactantNum)
    reactions[productChem] = {"out": int(productNum), "in": reactants}

lowerBound = int(1e12 // OreRequired())
upperBound = lowerBound * 10

while OreRequired(upperBound) < 1e12:
    lowerBound = upperBound
    upperBound *= 10

while lowerBound < upperBound - 1:
    mid = (lowerBound + upperBound) // 2
    ore = OreRequired(mid)
    if ore < 1e12:
        lowerBound = mid
    elif ore > 1e12:
        upperBound = mid
    else:
        break
print(mid)