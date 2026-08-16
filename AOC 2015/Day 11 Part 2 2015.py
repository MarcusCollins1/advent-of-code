FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 11 2015.txt"
FILE_NAME = "Day 11 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
BANNED = "iol"

def increment():
    global pwd
    for i in range(1, len(pwd)+1):
        letter = pwd[-i]
        if ALPHABET.index(letter) == 25:
            if i == 1:
                pwd = pwd[:-i]+"a"
            else:
                pwd = pwd[:-i]+"a"+pwd[-i+1:]
            continue
        if i == 1:
            pwd = pwd[:-i]+ALPHABET[ALPHABET.index(letter)+1]
        else:
            pwd = pwd[:-i]+ALPHABET[ALPHABET.index(letter)+1]+pwd[-i+1:]
        break

def check(pwd):
    # check if pwd has a banned letter
    flag = False
    for letter in BANNED:
        if letter in pwd:
            flag = True
            break
    if flag:
        return False

    # check if pwd has 2 pairs
    count = 0
    for letter in ALPHABET:
        if pwd.count(letter*2) > 0:
            count += 1
    if count < 2:
        return False

    # check if it has 3 in a row
    flag = True
    for i in range(len(pwd)-2):
        if ALPHABET.index(pwd[i]) == ALPHABET.index(pwd[i+1])-1 == ALPHABET.index(pwd[i+2])-2:
            flag = False
            break

    if flag:
        return False
    
    return True

pwd = data[0]

def solve():
    global pwd
    while True:
        increment()
        if check(pwd):
            break
for i in range(2):
    solve()
print(pwd)