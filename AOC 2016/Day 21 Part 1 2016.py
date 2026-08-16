import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 21 2016.txt"
# FILE_NAME = "Day 21 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

patterns = {
    "swap_position": re.compile(r"swap position (\d+) with position (\d+)"),
    "swap_letter": re.compile(r"swap letter ([a-z]) with letter ([a-z])"),
    "rotate": re.compile(r"rotate (left|right) (\d+) steps?"),
    "rotate_based": re.compile(r"rotate based on position of letter ([a-z])"),
    "reverse": re.compile(r"reverse positions (\d+) through (\d+)"),
    "move": re.compile(r"move position (\d+) to position (\d+)"),
}


pwd = list("abcdefgh")
# pwd = list("abcde")

for line in data:
    for instruction, pattern in patterns.items():
        match = pattern.fullmatch(line)

        if match:
            groups = match.groups()
            if instruction == "swap_position":
                p1, p2 = [int(x) for x in groups]
                pwd[p1], pwd[p2] = pwd[p2], pwd[p1]
            elif instruction == "swap_letter":
                p1, p2 = [pwd.index(x) for x in groups]
                pwd[p1], pwd[p2] = pwd[p2], pwd[p1]
            elif instruction == "rotate":
                num = int(groups[1]) % len(pwd)
                if groups[0] == "left":
                    pwd = pwd[num:] + pwd[:num]
                else:
                    pwd = pwd[-num:] + pwd[:-num]
            elif instruction == "rotate_based":
                idx = pwd.index(groups[0])
                num = (idx + (1 if idx < 4 else 2)) % len(pwd)
                pwd = pwd[-num:] + pwd[:-num]
            elif instruction == "reverse":
                p1, p2 = [int(x) for x in groups]
                pwd[p1:p2+1] = pwd[p1:p2+1][::-1]
            elif instruction == "move":
                p1, p2 = [int(x) for x in groups]
                letter = pwd.pop(p1)
                pwd.insert(p2, letter)
            break

    # print(instruction, groups)
    # print("".join(pwd))

print("".join(pwd))