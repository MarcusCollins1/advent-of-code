FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 04 2024.txt"
# FILE_NAME = "Day 04 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [list(x.strip()) for x in file.readlines()]
file.close()

SEARCH_WORD = "MAS"
SEARCH_WORD_LENGTH = len(SEARCH_WORD)

total = 0

for row in range(len(data)-(SEARCH_WORD_LENGTH-1)):
    for col in range(len(data[0])-(SEARCH_WORD_LENGTH-1)):
        test1 = "".join([data[row+i][col+i] for i in range(SEARCH_WORD_LENGTH)])
        test2 = "".join([data[row+(SEARCH_WORD_LENGTH-1)-i][col+i] for i in range(SEARCH_WORD_LENGTH)])
        if (SEARCH_WORD in [test1, test1[::-1]]) and (SEARCH_WORD in [test2, test2[::-1]]): total += 1
print(total)

print(sum([1 for col in range(len(data[0])-(SEARCH_WORD_LENGTH-1)) for row in range(len(data)-(SEARCH_WORD_LENGTH-1)) if ("".join([data[row+i][col+i] for i in range(SEARCH_WORD_LENGTH)]) in [SEARCH_WORD, SEARCH_WORD[::-1]]) and ("".join([data[row+(SEARCH_WORD_LENGTH-1)-i][col+i] for i in range(SEARCH_WORD_LENGTH)]) in [SEARCH_WORD, SEARCH_WORD[::-1]])]))