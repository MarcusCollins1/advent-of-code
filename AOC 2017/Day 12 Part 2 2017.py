FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 12 2017.txt"
FILE_NAME = "Day 12 2017 alt.txt"
FILE_NAME = "Day 12 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

TUNNELS = {int(line.split(" <-> ")[0]) : set(map(int, line.split(" <-> ")[1].split(", "))) for line in data}

def getGroup(tunnels: dict[int, set[int]], start: int) -> set[int]:
    connectedTunnels = {start}
    connectedTunnelsLength = 0
    while len(connectedTunnels) > connectedTunnelsLength:
        connectedTunnelsLength = len(connectedTunnels)
        for k,v in tunnels.items():
            if k in connectedTunnels: continue
            if v & connectedTunnels: connectedTunnels.add(k)
    return connectedTunnels

inGroup: set[int] = set()
numGroups = 0

start = 0
while start < max(TUNNELS.keys()):
    if start not in inGroup:
        numGroups += 1
        inGroup = inGroup.union(getGroup(TUNNELS, start))
    start += 1

print(numGroups)