FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 05 2015.txt"
# FILE_NAME = "Day 05 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

VOWELS = "aeiou"
BANNED = ["ab", "cd", "pq", "xy"]

total = 0
for line in data:
    line = line.strip()
    # check it doesnt contain a banned sub-string
    flag = False
    for banned in BANNED:
        if banned in line:
            flag = True
            break
    if flag:
        continue
    
    # check it has >= 3 vowels
    count = 0
    for vowel in VOWELS:
        count += line.count(vowel)
    if count < 3:
        continue

    # check it has a double letter
    flag = True
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            flag = False
            break
    if flag:
        continue
    total += 1
print(total)