from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 21 2017.txt"
# FILE_NAME = "Day 21 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def rotate(grid):
    n = len(grid)
    return tuple(
        tuple(grid[n-1-r][c] for r in range(n))
        for c in range(n)
    )

def flip(grid):
    return tuple(row[::-1] for row in grid)

def variants(grid):
    result = set()
    current = grid

    for _ in range(4):
        result.add(current)
        result.add(flip(current))
        current = rotate(current)

    return result

def parseGrid(s: str):
    return tuple(tuple(row) for row in s.split("/"))

def parseRules(text):
    rules = {}

    for line in text:
        left, right = line.split(" => ")

        source = parseGrid(left)
        target = parseGrid(right)

        for variant in variants(source):
            rules[variant] = target

    return rules

def enhance(grid, rules):
    n = len(grid)

    if n % 2 == 0:
        blockSize = 2
    elif n % 3 == 0:
        blockSize = 3
    else:
        raise ValueError("Grid size must be divisible by 2 or 3")

    blocksPerSide = n // blockSize
    newBlockSize = blockSize+1

    newN = blocksPerSide * newBlockSize
    result = [
        [None] * newN
        for _ in range(newN)
    ]

    for blockY in range(blocksPerSide):
        for blockX in range(blocksPerSide):

            block = tuple(
                tuple(
                    grid[blockY * blockSize + y]
                    [blockX * blockSize:
                     blockX * blockSize + blockSize]
                )
                for y in range(blockSize)
            )

            replacement = rules[block]

            for y in range(newBlockSize):
                for x in range(newBlockSize):
                    result[
                        blockY * newBlockSize + y
                    ][
                        blockX * newBlockSize + x
                    ] = replacement[y][x]

    return tuple(tuple(row) for row in result)

def solve(rulesText: list[str], iterations: int):
    rules = parseRules(rulesText)

    grid = parseGrid(".#./..#/###")

    for _ in range(iterations):
        grid = enhance(grid, rules)

    return sum(row.count("#") for row in grid)

print(solve(data, 5))

print(f"Time Taken: {time()-t1:.2f}s")