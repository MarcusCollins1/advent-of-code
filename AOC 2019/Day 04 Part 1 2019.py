FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2019/"
FILE_NAME = "Day 4 2019.txt"
FILE_NAME = "Day 4 2019 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()[0]
file.close()

def test(num):
    num = str(num)
    flag = True
    for let1, let2 in zip(num[:-1], num[1:]):
        if let1 == let2:
            flag = False
            break
    if flag:
        return False
    for let1, let2 in zip(num[:-1], num[1:]):
        if int(let1) > int(let2):
            return False
    return True

count = 0

for i in range(int(data.split("-")[0]), int(data.split("-")[1])+1):
    count += 1 if test(i) else 0

print(count)