import re
from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 7 2018.txt"
# FILE_NAME = "Day 7 2018 alt.txt"
# FILE_NAME = "Day 7 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

order = defaultdict(list)
for line in data:
    match = re.search(r'Step (\w) must be finished before step (\w) can begin.', line)
    if match:
        order[match.group(1)].append(match.group(2))

def GetNext():
    alp = "".join(sorted("".join(order.keys())))
    for value in order.values():
        for letter in value:
            alp = alp.replace(letter, "")
    return alp[0]

output = ""
while len(order.keys()) > 1:
    next = GetNext()
    order.pop(next)
    output += next
output += list(order.keys())[0]
for x in list(order.values())[0]:
    output += x
print(output)