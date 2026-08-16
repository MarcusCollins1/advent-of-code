FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 13 2022.txt"
# FILE_NAME = "Day 13 2022 alt.txt"
# FILE_NAME = "Day 13 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()


pairs = []
curr = []
for line in data:
    line = line.strip()
    if line != "":
        curr.append(eval(line))
    else:
        pairs.append(curr)
        curr = []
pairs.append(curr)

def check(ls1, ls2):
    for item1, item2 in zip(ls1, ls2):
        if type(item1) != type(item2):
            if type(item1) != list:
                item1 = [item1]
            else:
                item2 = [item2]
        if type(item1) == int:
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
        if type(item1) == list:
            x = check(item1, item2)
            if x != None:
                if x:
                    return True
                else:
                    return False
    if len(ls1) < len(ls2):
        return True
    elif len(ls1) > len(ls2):
        return False

count = 0
for pair, i in zip(pairs, range(1, len(pairs)+1)):
    left, right = pair
    count += i if check(left, right) else 0
print(count)
