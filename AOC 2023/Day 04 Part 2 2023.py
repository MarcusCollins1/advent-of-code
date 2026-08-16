from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 04 2023.txt"
# FILE_NAME = "Day 04 2023 alt.txt"
# FILE_NAME = "Day 04 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

cards = dict()

for line in data:
    card, line = line.split(": ")
    card = int(card.replace("Card ", ""))
    line = line.split(" | ")
    line = [list(map(int, x.split())) for x in line]
    score = len(set(line[0]).intersection(set(line[1])))
    cards[card] = score

num_of_cards = defaultdict(lambda:1)
for i in range(1, max(cards.keys())+1):
    curr = num_of_cards[i]
    curr_score = cards[i]
    for j in range(i+1, i+curr_score+1):
        num_of_cards[j] += curr
print(sum(num_of_cards.values()))