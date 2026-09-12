FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 05 2015.txt"
FILE_NAME = "Day 05 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()


total = 0
for line in data:
    line = line.strip()
    # check it has 2 of a pair
    flag = True
    for i in range(len(line)-1):
        if line.count(line[i]+line[i+1]) > 1:
            flag = False
            break
    if flag:
        continue

    # check it has a double letter with 1 letter between
    flag = True
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            flag = False
            break
    if flag:
        continue
    total += 1
print(total)