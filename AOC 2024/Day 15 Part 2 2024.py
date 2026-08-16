FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 15 2024.txt"
# FILE_NAME = "Day 15 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
map, moves = [x.strip() for x in file.read().split("\n\n")]
file.close()
map = map.split("\n")
moves = list(moves.replace("\n", ""))

MOVE_TO_DIRECTION: dict[str, tuple[int, int]] = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

class Item:
    def __init__(self, startPosition: tuple[int, int]) -> None:
        self.position = startPosition
    def __str__(self) -> str:
        return f"Item:\nPosition: {self.position}\n"
    def __repr__(self) -> str:
        return self.__str__()

class Wall(Item):
    def __init__(self, startPosition: tuple[int, int]) -> None:
        super().__init__(startPosition)
    def __str__(self) -> str:
        return f"Wall:\nPosition: {self.position}\n"

class Box(Item):
    def __init__(self, startPosition: tuple[int, int], endPosition: tuple[int, int], boxId: int) -> None:
        super().__init__(startPosition)
        self.endPosition = endPosition
        self.boxId = boxId
    
    def CanMove(self, direction: tuple[int, int], items: list[Item]) -> bool:
        newPosition1 = (self.position[0] + direction[0], self.position[1] + direction[1])
        newPosition2 = (self.endPosition[0] + direction[0], self.endPosition[1] + direction[1])
        itemAtNewPosition1 = GetItemAtPosition(items, newPosition1)
        if type(itemAtNewPosition1) == Box and itemAtNewPosition1.boxId == self.boxId: itemAtNewPosition1 = None
        itemAtNewPosition2 = GetItemAtPosition(items, newPosition2)
        if type(itemAtNewPosition2) == Box and itemAtNewPosition2.boxId == self.boxId: itemAtNewPosition2 = None
        itemAtNewPosition1Type = type(itemAtNewPosition1)
        itemAtNewPosition2Type = type(itemAtNewPosition2)
        if itemAtNewPosition1 == None and itemAtNewPosition2 == None: return True
        elif itemAtNewPosition1Type == Wall or itemAtNewPosition2Type == Wall: return False
        elif type(itemAtNewPosition1) == Box and type(itemAtNewPosition2) == Box:
            # Same box
            if itemAtNewPosition1.boxId == itemAtNewPosition2.boxId:
                return itemAtNewPosition1.CanMove(direction, items)
            # Different boxes
            else:
                return all([itemAtNewPosition1.CanMove(direction, items), itemAtNewPosition2.CanMove(direction, items)])
        elif type(itemAtNewPosition1) == Box:
            return itemAtNewPosition1.CanMove(direction, items)
        elif type(itemAtNewPosition2) == Box:
            return itemAtNewPosition2.CanMove(direction, items)
        print(itemAtNewPosition1Type)
        print(itemAtNewPosition2Type)
        raise Exception("Something went wrong")

    
    def Move(self, direction: tuple[int, int], items: list[Item]) -> None:
        newPosition1 = (self.position[0] + direction[0], self.position[1] + direction[1])
        newPosition2 = (self.endPosition[0] + direction[0], self.endPosition[1] + direction[1])
        itemAtNewPosition1 = GetItemAtPosition(items, newPosition1)
        if type(itemAtNewPosition1) == Box and itemAtNewPosition1.boxId == self.boxId: itemAtNewPosition1 = None
        itemAtNewPosition2 = GetItemAtPosition(items, newPosition2)
        if type(itemAtNewPosition2) == Box and itemAtNewPosition2.boxId == self.boxId: itemAtNewPosition2 = None
        
        self.position = newPosition1
        self.endPosition = newPosition2
        
        if type(itemAtNewPosition1) == Box and type(itemAtNewPosition2) == Box:
            # Same box
            if itemAtNewPosition1.boxId == itemAtNewPosition2.boxId:
                itemAtNewPosition1.Move(direction, items)
            # Different boxes
            else:
                itemAtNewPosition1.Move(direction, items)
                itemAtNewPosition2.Move(direction, items)
        elif type(itemAtNewPosition1) == Box: itemAtNewPosition1.Move(direction, items)
        elif type(itemAtNewPosition2) == Box: itemAtNewPosition2.Move(direction, items)
    
    def __str__(self) -> str:
        return f"Box:\nPosition: {self.position}\nId: {self.boxId}\n"

class Robot(Item):
    def __init__(self, startPosition: tuple[int, int]) -> None:
        super().__init__(startPosition)
    
    def Move(self, direction: tuple[int, int], items: list[Item]) -> None:
        newPosition = (self.position[0] + direction[0], self.position[1] + direction[1])
        itemAtNewPosition = GetItemAtPosition(items, newPosition)
        if itemAtNewPosition == None:
            self.position = newPosition
            return
        elif type(itemAtNewPosition) == Wall: return
        elif type(itemAtNewPosition) == Box:
            result = itemAtNewPosition.CanMove(direction, items)
            if result:
                self.position = newPosition
                itemAtNewPosition.Move(direction, items)
            return
        raise Exception("Something's gone wrong")
    def __str__(self) -> str:
        return f"Robot:\nPosition: {self.position}\n"

def GetItemAtPosition(items: list[Item], position: tuple[int, int]) -> Item | None:
    for item in items:
        if type(item) == Box:
            if position in [item.position, item.endPosition]: return item
        elif item.position == position: return item
    return None

def GetRobot(items: list[Item]) -> Robot:
    for item in items:
        if type(item) == Robot: return item
    raise Exception("Couldn't find robot")

def PrintGrid(items: list[Item]) -> None:
    boxIds: set[int] = set()
    maxX, maxY = max([item.position[0] for item in items]), max([item.position[1] for item in items])
    for y in range(maxY+1):
        for x in range(maxX+1):
            item = GetItemAtPosition(items, (x, y))
            itemType = type(item)
            if type(item) == Box:
                print("]" if item.boxId in boxIds else "[", end="")
                boxIds.add(item.boxId)
            else:
                print("#" if itemType == Wall else "@" if itemType == Robot else ".", end="")
        print()

items: list[Item] = []
boxId = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        symbol = map[y][x]
        if symbol == "#":
            items.append(Wall((x*2, y)))
            items.append(Wall((x*2+1, y)))
        elif symbol == "O":
            items.append(Box((x*2, y), (x*2+1, y), boxId))
            boxId += 1
        elif symbol == "@": items.append(Robot((x*2, y)))

# print("Initial")
# PrintGrid(items)

for move in moves:
    # print(f"Move {move}")
    direction = MOVE_TO_DIRECTION[move]
    GetRobot(items).Move(direction, items)
    # PrintGrid(items)


print(sum([box.position[0] + box.position[1]*100 for box in items if type(box) == Box]))