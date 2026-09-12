FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 3 2022.txt"
FILE_NAME = "Day 3 2022 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

PRIORITIES = dict()
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter, num in zip(LETTERS, range(1, 53)):
    PRIORITIES[letter] = num

total = 0
for bag in data:
    bag = bag.strip()
    bag = [bag[:len(bag)//2], bag[len(bag)//2:]]
    total += PRIORITIES[(list(set(bag[0]).intersection(set(bag[1]))))[0]]
print(total)