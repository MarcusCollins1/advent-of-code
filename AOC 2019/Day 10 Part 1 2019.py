from math import gcd
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 10 2019.txt"
# FILE_NAME = "Day 10 2019 alt.txt"
# FILE_NAME = "Day 10 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()
WIDTH, HEIGHT = len(data[0]), len(data)

def NumAsteroids(x: int, y: int, asteroidMap:list[str]) -> int:
    count = 0
    distToTop, distToBottom, distToLeft, distToRight = y, (HEIGHT-1) - y, x, (WIDTH-1) - x
    directions:set[tuple[int, int]] = set()
    for dy in range(-distToTop, distToBottom+1):
        for dx in range(-distToLeft, distToRight+1):
            if dy == dx == 0:
                continue
            g = gcd(dx, dy)
            simplified_dx, simplified_dy = dx // g, dy // g
            directions.add((simplified_dx, simplified_dy))
    for dx, dy in directions:
        currX, currY = x+dx, y+dy
        while 0 <= currX < WIDTH and 0 <= currY < HEIGHT:
            if asteroidMap[currY][currX] == "#":
                count += 1
                break
            currX += dx
            currY += dy
    return count

greatestNumAsteroids = max([NumAsteroids(x, y, data) for y in range(HEIGHT) for x in range(WIDTH) if data[y][x] == "#"])
print(greatestNumAsteroids)