from time import time
t1 = time()
import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 16 2017.txt"
# FILE_NAME = "Day 16 2017 test.txt"

order = list("abcdefghijklmnop")
# order = list("abcde")

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0].split(",")
file.close()

patternSpin = re.compile(r"s(\d+)")
patternExchange = re.compile(r"x(\d+)/(\d+)")
patternPartner = re.compile(r"p(\w+)/(\w+)")

for line in data:
    matchSpin = re.match(patternSpin, line)
    matchExchange = re.match(patternExchange, line)
    matchPartner = re.match(patternPartner, line)
    if matchSpin:
        num = int(matchSpin.groups()[0])
        order = order[-num:] + order[:-num]
    elif matchExchange:
        num1, num2 = [int(x) for x in matchExchange.groups()]
        order[num1], order[num2] = order[num2], order[num1]
    elif matchPartner:
        l1, l2 = matchPartner.groups()
        i1, i2 = order.index(l1), order.index(l2)
        order[i1], order[i2] = order[i2], order[i1]
    else:
        raise ValueError(line)

print(''.join(order))
print(f"Time Taken: {time()-t1:.2f}s")