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

class Player:
    def __init__(self) -> None:
        self.score = 0
    
    def AddToScore(self, score: int) -> None:
        self.score += score
    
    def GetScore(self) -> int:
        return self.score

placedMarbles = [0]
placedMarblesIndex = 0
players = [Player() for i in range(NUM_PLAYERS)]
playerIndex = 0
currMarble = 1
while currMarble <= MAX_MARBLE:
    if len(placedMarbles) < 2:
        placedMarbles.append(currMarble)
        placedMarblesIndex = placedMarbles.index(currMarble)
    elif currMarble%23 == 0:
        placedMarblesIndex = (placedMarblesIndex-7) % len(placedMarbles)
        players[playerIndex].AddToScore(currMarble + placedMarbles.pop(placedMarblesIndex))
    else:
        placedMarblesIndex = (placedMarblesIndex+2) % len(placedMarbles)
        placedMarblesIndex = len(placedMarbles) if placedMarblesIndex == 0 else placedMarblesIndex
        placedMarbles.insert(placedMarblesIndex, currMarble)
    
    currMarble += 1
    playerIndex = (playerIndex+1) % NUM_PLAYERS

print(max([player.GetScore() for player in players]))