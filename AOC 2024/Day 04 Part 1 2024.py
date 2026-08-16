FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 04 2024.txt"
# FILE_NAME = "Day 04 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

SEARCH_WORD = "XMAS"
SEARCH_WORD_LENGTH = len(SEARCH_WORD)

total = 0

# Horizontal
for line in data:
    for i in range(len(line)-(SEARCH_WORD_LENGTH-1)):
        test = "".join(line[i:i+SEARCH_WORD_LENGTH])
        if test == SEARCH_WORD or test[::-1] == SEARCH_WORD:
            total += 1

# Vertical
for col in range(len(data[0])):
    for row in range(len(data)-(SEARCH_WORD_LENGTH-1)):
        test = "".join([data[row+i][col] for i in range(SEARCH_WORD_LENGTH)])
        if test == SEARCH_WORD or test[::-1] == SEARCH_WORD:
            total += 1

# \
for row in range(len(data)-(SEARCH_WORD_LENGTH-1)):
    for col in range(len(data[0])-(SEARCH_WORD_LENGTH-1)):
        test = "".join(data[row+i][col+i] for i in range(SEARCH_WORD_LENGTH))
        if test == SEARCH_WORD or test[::-1] == SEARCH_WORD:
            total += 1
# /
for row in range((SEARCH_WORD_LENGTH-1), len(data)):
    for col in range(len(data[0])-(SEARCH_WORD_LENGTH-1)):
        test = "".join(data[row-i][col+i] for i in range(SEARCH_WORD_LENGTH))
        if test == SEARCH_WORD or test[::-1] == SEARCH_WORD:
            total += 1
print(total)