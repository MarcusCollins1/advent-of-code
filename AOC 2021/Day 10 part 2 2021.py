# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 10 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 10 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 10 2021 test.txt", "r")
file = input_file.read().splitlines()
points = {"(":1, "[":2, "{":3, "<":4}
open_close = {")":"(", "]":"[", "}":"{", ">":"<"}
totals = []
for line in file:
    curr = []
    corrupt = False
    for char in line:
        if char in "([{<":
            curr.append(char)
        else:
            if curr[-1] != open_close[char]:
                corrupt = True
                break
            curr.pop(-1)
    if not corrupt:
        val = 0
        for char in curr[::-1]:
            val *= 5
            val += points[char]
        totals.append(val)
print(sorted(totals)[len(totals)//2])