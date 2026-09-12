FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 12 2017.txt"
# FILE_NAME = "Day 12 2017 alt.txt"
# FILE_NAME = "Day 12 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

TUNNELS = {int(line.split(" <-> ")[0]) : set(map(int, line.split(" <-> ")[1].split(", "))) for line in data}

connectedTunnels = {0}
connectedTunnelsLength = 0
while len(connectedTunnels) > connectedTunnelsLength:
    connectedTunnelsLength = len(connectedTunnels)
    for k,v in TUNNELS.items():
        if k in connectedTunnels: continue
        if v & connectedTunnels: connectedTunnels.add(k)

print(len(connectedTunnels))