from time import time
t1 = time()
from copy import deepcopy
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 13 2018.txt"
# FILE_NAME = "Day 13 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x) for x in file.read().splitlines()]
file.close()

HEIGHT, WIDTH = len(data), len(data[0])
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

LEFT_TURN: dict[tuple[int, int], tuple[int, int]] = {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP}
RIGHT_TURN: dict[tuple[int, int], tuple[int, int]] = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}

class Cart:
    def __init__(self, x: int, y: int, dir: tuple[int, int]) -> None:
        self.x = x
        self.y = y
        self.dir = dir
        self.num = 0

    def move(self, tracks: list[list[str]]) -> None:
        self.x += self.dir[0]
        self.y += self.dir[1]
        newCell = tracks[self.y][self.x]
        if newCell == " ": raise ValueError("Cart off track")
        elif newCell == "\\":
            self.dir = DOWN if self.dir == RIGHT else RIGHT if self.dir == DOWN else LEFT if self.dir == UP else UP
        elif newCell == "/":
            self.dir = UP if self.dir == RIGHT else RIGHT if self.dir == UP else LEFT if self.dir == DOWN else DOWN
        elif newCell == "+":
            self.dir = LEFT_TURN[self.dir] if self.num == 0 else self.dir if self.num == 1 else RIGHT_TURN[self.dir]
            self.num = (self.num+1) % 3

    @property
    def pos(self) -> int:
        return self.y*WIDTH + self.x

    def __repr__(self) -> str:
        return f"Cart: ({self.x}, {self.y}), {self.dir}, {self.num}"

def checkCrash(carts: list[Cart]) -> bool:
    positions = [cart.pos for cart in carts]
    return len(positions) > len(set(positions))

def printTracks(tracks: list[list[str]], carts: list[Cart]):
    for cart in carts:
        tracks[cart.y][cart.x] = "^" if cart.dir == UP else ">" if cart.dir == RIGHT else "v" if cart.dir == DOWN else "<" if cart.dir == LEFT else "#"
    for line in tracks:
        print("".join(line))

carts: list[Cart] = []
tracks: list[list[str]] = []

for y, row in enumerate(data):
    newRow: list[str] = []
    for x, cell in enumerate(row):
        dir = UP if cell == "^" else RIGHT if cell == ">" else DOWN if cell == "v" else LEFT if cell == "<" else None
        if dir: carts.append(Cart(x, y, dir))
        newRow.append(cell.replace("^", "|").replace("v", "|").replace(">", "-").replace("<", "-"))
    tracks.append(newRow)

crashed = False
while not crashed:
    carts = sorted(carts, key=lambda x: x.pos)
    # printTracks(deepcopy(tracks), deepcopy(carts))
    for cart in carts:
        cart.move(tracks)
        if checkCrash(carts):
            crashed = True
            break

cartPositions = [cart.pos for cart in carts]
for cart in carts:
    if cartPositions.count(cart.pos) > 1:
        print(f"{cart.x},{cart.y}")
        break
print(f"Time Taken: {time()-t1:.2f}s")