import re
from itertools import permutations
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 22 2016.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Node:
    def __init__(self, x: int, y: int, size: int, used: int, avail: int) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail

pattern = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")

nodes: list[Node] = []
for line in data:
    match = pattern.fullmatch(line)
    if match:
        x, y, size, used, avail, percent = map(int, match.groups())
        nodes.append(Node(x, y, size, used, avail))


print(sum(1 for n1, n2 in permutations(nodes, 2) if (0 < n1.used <= n2.avail)))