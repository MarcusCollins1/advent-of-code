# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 10 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 10 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 10 2021 test.txt", "r")
file = input_file.read().splitlines()
points = {")":3, "]":57, "}":1197, ">":25137}
open_close = {")":"(", "]":"[", "}":"{", ">":"<"}
total = 0
for line in file:
    curr = []
    for char in line:
        if char in "([{<":
            curr.append(char)
        else:
            if curr[-1] != open_close[char]:
                total += points[char]
                break
            curr.pop(-1)
print(total)