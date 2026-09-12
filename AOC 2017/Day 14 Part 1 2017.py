from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 14 2017.txt"
# FILE_NAME = "Day 14 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()

def knotHash(string: str) -> str:
    lengths = [ord(c) for c in string]
    lengths += [17, 31, 73, 47, 23]

    nums = list(range(256))
    pos = 0
    skip = 0

    for _ in range(64):
        for length in lengths:
            # Reverse the section, wrapping around
            indices = [(pos+i) % 256 for i in range(length)]
            values = [nums[i] for i in indices]

            values.reverse()

            for i, value in zip(indices, values):
                nums[i] = value

            pos = (pos+length+skip) % 256
            skip += 1

    # Dense hash
    dense = []
    for start in range(0, 256, 16):
        value = nums[start]
        for i in range(start+1, start+16):
            value ^= nums[i]

        dense.append(value)

    return ''.join(f'{x:02x}' for x in dense)

def makeGrid(key: str) -> list[str]:
    grid: list[str] = []

    for row in range(128):
        h = knotHash(f"{key}-{row}")

        bits = ''.join(f"{int(c, 16):04b}" for c in h)
        grid.append(bits)
    return grid

grid = makeGrid(data)
used = sum(row.count("1") for row in grid)
print(used)

print(f"Time Taken: {time()-t1:.2f}s")