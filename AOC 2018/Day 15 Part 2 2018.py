from time import time
t1 = time()
from collections import deque

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 15 2018.txt"
# FILE_NAME = "Day 15 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()


class Unit:
    def __init__(self, gridWidth: int, gridHeight: int, startX: int, startY: int, id: int, char: str, attackPower: int = 3, hitPoints: int = 200) -> None:
        self.x = startX
        self.y = startY
        self.id = id
        self.char = char
        self.attackPower = attackPower
        self.hitPoints = hitPoints
        self.GRID_WIDTH = gridWidth
        self.GRID_HEIGHT = gridHeight

    @property
    def readingPosition(self) -> int:
        return self.y * self.GRID_WIDTH + self.x

    def damage(self, amount: int) -> bool:
        self.hitPoints -= amount
        return self.hitPoints <= 0


class Wall:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.char = "#"


class Solver:
    def __init__(self, data: list[str], elfAttackPower: int, debugMode: bool = True) -> None:
        self.elves: list[Unit] = []
        self.goblins: list[Unit] = []
        self.walls: list[Wall] = []

        self.elfAttackPower: int = elfAttackPower
        self.debugMode: bool = debugMode

        self.grid: dict[tuple[int, int], Unit | Wall] = {}
        self.unitsById: dict[int, Unit] = {}

        self.GRID_WIDTH: int = 0
        self.GRID_HEIGHT: int = 0

        self.UP: tuple[int, int] = (0, -1)
        self.DOWN: tuple[int, int] = (0, 1)
        self.LEFT: tuple[int, int] = (-1, 0)
        self.RIGHT: tuple[int, int] = (1, 0)
        self.directions: list[tuple[int, int]] = [self.UP, self.LEFT, self.RIGHT, self.DOWN]

        self.loadFromData(data)

    def loadFromData(self, data: list[str]) -> None:
        self.elves = []
        self.goblins = []
        self.walls = []
        self.grid = {}
        self.unitsById = {}

        id = 0
        self.GRID_WIDTH = len(data[0])
        self.GRID_HEIGHT = len(data)

        for y, line in enumerate(data):
            for x, cell in enumerate(line):
                if cell == "#":
                    wall = Wall(x, y)
                    self.walls.append(wall)
                    self.grid[(x, y)] = wall

                elif cell == "E":
                    elf = Unit(self.GRID_WIDTH, self.GRID_HEIGHT, x, y, id, "E", self.elfAttackPower)
                    self.elves.append(elf)
                    self.grid[(x, y)] = elf
                    self.unitsById[id] = elf
                    id += 1

                elif cell == "G":
                    goblin = Unit(self.GRID_WIDTH, self.GRID_HEIGHT, x, y, id, "G")
                    self.goblins.append(goblin)
                    self.grid[(x, y)] = goblin
                    self.unitsById[id] = goblin
                    id += 1

    def getUnitFromId(self, id: int) -> Unit | None:
        return self.unitsById.get(id)

    def getItemFromXY(self, x: int, y: int) -> Unit | Wall | None:
        return self.grid.get((x, y))

    def display(self) -> None:
        for y in range(self.GRID_HEIGHT):
            for x in range(self.GRID_WIDTH):
                item = self.getItemFromXY(x, y)
                print(item.char if item else ".", end="")

            for unit in sorted([u for u in self.elves + self.goblins if u.y == y], key= lambda u: u.x):
                print(f"\t {unit.char}({unit.hitPoints})", end="")
            print()

    def getOrder(self) -> list[int]:
        return [item.id for item in sorted(self.elves + self.goblins, key=lambda item: item.readingPosition)]

    def addTuples(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return (a[0] + b[0], a[1] + b[1])

    def xyToReadingPos(self, x: int, y: int) -> int:
        return y * self.GRID_WIDTH + x

    def readingPosToXy(self, readingPos: int) -> tuple[int, int]:
        x = readingPos % self.GRID_WIDTH
        y = readingPos // self.GRID_WIDTH
        return (x, y)

    def getTargetPath(self, unit: Unit, enemies: list[Unit]) -> list[tuple[int, int]] | None:
        targets: set[tuple[int, int]] = set()

        for enemy in enemies:
            for direction in self.directions:
                newX = enemy.x + direction[0]
                newY = enemy.y + direction[1]

                item = self.getItemFromXY(newX, newY)

                if not item or item is unit:
                    targets.add((newX, newY))

        if not targets:
            return None

        start = (unit.x, unit.y)

        # Already in range of an enemy
        if start in targets:
            return [start]

        # BFS from the unit to all reachable target squares
        queue: deque[tuple[int, int]] = deque([start])
        visited: set[tuple[int, int]] = {start}

        distances: dict[tuple[int, int], int] = {start: 0}
        previous: dict[tuple[int, int], tuple[int, int]] = {}

        bestDistance: int | None = None
        reachableTargets: list[tuple[int, int]] = []

        while queue:
            currPos = queue.popleft()
            currDistance = distances[currPos]

            if bestDistance is not None and currDistance > bestDistance:
                break

            if currPos in targets:
                reachableTargets.append(currPos)
                bestDistance = currDistance
                continue

            if bestDistance is not None:
                continue

            for direction in self.directions:
                newPos = self.addTuples(currPos, direction)

                if newPos in visited:
                    continue

                if newPos in self.grid:
                    continue

                visited.add(newPos)
                distances[newPos] = currDistance + 1
                previous[newPos] = currPos
                queue.append(newPos)

        if not reachableTargets:
            return None

        # Choose destination in reading order
        target = min(reachableTargets, key=lambda pos: self.xyToReadingPos(*pos))

        # Reconstruct the shortest path
        path = [target]

        while path[-1] != start:
            path.append(previous[path[-1]])

        path.reverse()

        return path

    def removeElfById(self, id: int) -> None:
        self.elves = [elf for elf in self.elves if elf.id != id]
        self.unitsById.pop(id, None)

    def removeGoblinById(self, id: int) -> None:
        self.goblins = [goblin for goblin in self.goblins if goblin.id != id]
        self.unitsById.pop(id, None)

    def round(self) -> bool:
        order = self.getOrder()

        for id in order:
            unit = self.getUnitFromId(id)
            if unit is None:
                continue


            if unit.char == "E":
                enemies = self.goblins
            elif unit.char == "G":
                enemies = self.elves
            else:
                raise ValueError("Unit must be Elf or Goblin")

            # Check whether an enemy is already adjacent
            targets: list[Unit] = []

            for direction in self.directions:
                newX, newY = self.addTuples((unit.x, unit.y), direction)
                item = self.getItemFromXY(newX, newY)

                if type(item) is Unit and item.char != unit.char:
                    targets.append(item)

            # Handle moving
            if not targets:
                path = self.getTargetPath(unit, enemies)

                if path and len(path) >= 2:
                    del self.grid[(unit.x, unit.y)]

                    unit.x, unit.y = path[1]

                    self.grid[(unit.x, unit.y)] = unit

                # Check for enemies after moving
                for direction in self.directions:
                    newX, newY = self.addTuples((unit.x, unit.y), direction)
                    item = self.getItemFromXY(newX, newY)

                    if type(item) is Unit and item.char != unit.char:
                        targets.append(item)

            # Handle attacking
            if targets:
                target = min(targets, key=lambda t: (t.hitPoints, t.readingPosition))

                if target.damage(unit.attackPower):
                    del self.grid[(target.x, target.y)]

                    if target.char == "E":
                        return False
                    else:
                        self.removeGoblinById(target.id)

        return True

    def solve(self) -> int:
        round = 0

        while self.goblins:
            if self.debugMode:
                print(f"After {round} Rounds (Elf Attack Power: {self.elfAttackPower}):")
                self.display()
                print()

            completed = self.round()

            if not completed:
                return 0

            round += 1

        if self.debugMode:
            print(f"After {round} Rounds (Elf Attack Power: {self.elfAttackPower}):")
            self.display()

        return sum(e.hitPoints for e in self.elves) * (round-1)

elfAttackPower = 4
while True:
    solver = Solver(data, elfAttackPower, False)
    result = solver.solve()
    if result: break
    elfAttackPower += 1

print(result)

print(f"Time Taken: {time()-t1:.2f}s")
