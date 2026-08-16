from collections import defaultdict

FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 07 2023.txt"
# FILE_NAME = "Day 07 2023 alt.txt"
# FILE_NAME = "Day 07 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def card_score(card:str) -> int:
    cards = "23456789TJQKA"
    return cards.find(card)

def score(hand:str) -> int:
    output = 0
    freq = defaultdict(int)
    for l in hand:
        freq[l] += 1
    # 5 of a kind
    if 5 in freq.values():
        output = 6
    # 4 of a kind
    elif 4 in freq.values():
        output = 5
    # full house
    elif 3 in freq.values() and 2 in freq.values():
        output = 4
    # 3 of a kind
    elif 3 in freq.values():
        output = 3
    # 2 pairs
    elif list(freq.values()).count(2) == 2:
        output = 2
    # pair
    elif 2 in freq.values():
        output = 1
    return output

cards = [[line.split()[0], int(line.split()[1])] for line in data]
cards = sorted(cards, key= lambda x: (score(x[0]), card_score(x[0][0]), card_score(x[0][1]), card_score(x[0][2]), card_score(x[0][3]), card_score(x[0][4])))

total = sum([x[1]*(i+1) for i, x in enumerate(cards)])
print(total)