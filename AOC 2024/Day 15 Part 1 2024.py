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
    def __init__(self, startPosition: tuple[int, int]) -> None:
        super().__init__(startPosition)
    def Move(self, direction: tuple[int, int], items: list[Item]) -> bool:
        newPosition = (self.position[0] + direction[0], self.position[1] + direction[1])
        itemAtNewPosition = GetItemAtPosition(items, newPosition)
        if itemAtNewPosition == None:
            self.position = newPosition
            return True
        elif type(itemAtNewPosition) == Wall: return False
        elif type(itemAtNewPosition) == Box:
            result = itemAtNewPosition.Move(direction, items)
            if result:
                self.position = newPosition
                return True
            return False
        print("Something's gone wrong")
        return False
    def __str__(self) -> str:
        return f"Box:\nPosition: {self.position}\n"

class Robot(Item):
    def __init__(self, startPosition: tuple[int, int]) -> None:
        super().__init__(startPosition)
    def Move(self, direction: tuple[int, int], items: list[Item]) -> bool:
        newPosition = (self.position[0] + direction[0], self.position[1] + direction[1])
        itemAtNewPosition = GetItemAtPosition(items, newPosition)
        if itemAtNewPosition == None:
            self.position = newPosition
            return True
        elif type(itemAtNewPosition) == Wall: return False
        elif type(itemAtNewPosition) == Box:
            result = itemAtNewPosition.Move(direction, items)
            if result:
                self.position = newPosition
                return True
            return False
        print("Something's gone wrong")
        return False
    def __str__(self) -> str:
        return f"Robot:\nPosition: {self.position}\n"

def GetItemAtPosition(items: list[Item], position: tuple[int, int]) -> Item | None:
    for item in items:
        if item.position == position: return item
    return None

def GetRobot(items: list[Item]) -> Robot:
    for item in items:
        if type(item) == Robot: return item
    raise Exception("Couldn't find robot")

items: list[Item] = [item for item in [Wall((x, y)) if map[y][x] == "#" else Box((x, y)) if map[y][x] == "O" else Robot((x, y)) if map[y][x] == "@" else None for y in range(len(map)) for x in range(len(map[0]))] if item != None]
for move in moves:
    direction = MOVE_TO_DIRECTION[move]
    GetRobot(items).Move(direction, items)


print(sum([box.position[0] + box.position[1]*100 for box in items if type(box) == Box]))