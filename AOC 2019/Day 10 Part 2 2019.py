from math import gcd, atan2, pi
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 10 2019.txt"
# FILE_NAME = "Day 10 2019 alt.txt"
# FILE_NAME = "Day 10 2019 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()
WIDTH, HEIGHT = len(data[0]), len(data)

def GetDirections(x: int, y: int, asteroidMap:list[list[str]]) -> set[tuple[int, int]]:
    distToTop, distToBottom, distToLeft, distToRight = y, (HEIGHT-1) - y, x, (WIDTH-1) - x
    directions:set[tuple[int, int]] = set()
    for dy in range(-distToTop, distToBottom+1):
        for dx in range(-distToLeft, distToRight+1):
            if dy == dx == 0:
                continue
            g = gcd(dx, dy)
            simplified_dx, simplified_dy = dx // g, dy // g
            directions.add((simplified_dx, simplified_dy))
    return directions

def NumAsteroids(x: int, y: int, asteroidMap:list[list[str]]) -> int:
    count = 0
    directions:set[tuple[int, int]] = GetDirections(x, y, asteroidMap)
    for dx, dy in directions:
        currX, currY = x+dx, y+dy
        while 0 <= currX < WIDTH and 0 <= currY < HEIGHT:
            if asteroidMap[currY][currX] == "#":
                count += 1
                break
            currX += dx
            currY += dy
    return count

def AngleFromTop(direction: tuple[int, int]):
    x, y = direction
    angle = atan2(-y, x)
    adjustedAngle = (pi / 2 - angle) % (2 * pi)
    return adjustedAngle

stations = {(x, y) : NumAsteroids(x, y, data) for y in range(HEIGHT) for x in range(WIDTH) if data[y][x] == "#"}
greatestNumAsteroids = max(stations.values())
bestStation = [stationPos for stationPos in stations.keys() if stations[stationPos] == greatestNumAsteroids][0]
# print(f"Best station: {bestStation}")

destroyedAsteroids: list[tuple[int, int]] = []
directions = sorted(GetDirections(bestStation[0], bestStation[1], data), key=AngleFromTop)
# print(f"Directions: {directions}")
stationX, stationY = bestStation
# print(stationX, stationY)
directionsIndex = 0
while sum([row.count("#") for row in data]) > 1:
    currDirection = directions[directionsIndex]
    dx, dy = currDirection
    # print(dx, dy)
    currX, currY = stationX + dx, stationY + dy
    while 0 <= currX < WIDTH and 0 <= currY < HEIGHT:
        # print(currX, currY)
        if data[currY][currX] == "#":
            destroyedAsteroids.append((currX, currY))
            data[currY][currX] = "."
            break
        currX += dx
        currY += dy
    directionsIndex = (directionsIndex+1)%len(directions)
# print(destroyedAsteroids)
# print(destroyedAsteroids[199])
print(destroyedAsteroids[199][0]*100+destroyedAsteroids[199][1])