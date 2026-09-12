from collections import deque
import re
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 09 2018.txt"
# FILE_NAME = "Day 09 2018 alt.txt"
# FILE_NAME = "Day 09 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

numbers = list(map(int, re.findall(r"\d+", data)))
if len(numbers) != 2:
    print("Couldn't process input")
    quit()
NUM_PLAYERS, MAX_MARBLE = numbers
MAX_MARBLE *= 100

def Solve(numPlayers: int, maxMarbles: int) -> int:
    placedMarbles: deque[int] = deque([0])
    scores = [0] * numPlayers
    for marble in range(1, maxMarbles+1):
        if marble % 23 == 0:
            placedMarbles.rotate(7)
            scores[marble % numPlayers] += marble + placedMarbles.pop()
            placedMarbles.rotate(-1)
        else:
            placedMarbles.rotate(-1)
            placedMarbles.append(marble)
    return max(scores)


print(Solve(NUM_PLAYERS, MAX_MARBLE))