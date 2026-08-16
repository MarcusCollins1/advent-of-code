# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 8 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 8 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 8 2021 test.txt", "r")
file = input_file.read().splitlines()
inputs, outputs = [], []
str_dig = {"cf":1, "acdeg":2, "acdfg":3, "bcdf":4, "abdfg":5, "abdefg":6, "acf":7, "abcdefg":8, "abcdfg":9, "abcefg":0}
total = 0
for line in file:
    inputs.append(line.split(" | ")[0])
    outputs.append(line.split(" | ")[1])
for idx in range(len(inputs)):
    curr = sorted(inputs[idx].split(), key=len)
    one = curr[0]
    seven = curr[1]
    four = curr[2]
    eight = curr[9]
    for letter in seven:
        if letter not in one:
            a = letter
    cf = one
    bd = ""
    for letter in four:
        if letter not in one:
            bd += letter
    for i in range(3,6):
        flag = True
        for letter in seven:
            if letter not in curr[i]:
                flag = False
        if flag:
            three = curr[i]
    dg = ""
    for letter in three:
        if letter not in seven:
            dg += letter
    for letter in dg:
        if letter in bd:
            d = letter
        else:
            g = letter
    b = bd.replace(d, "")
    for i in range(3,6):
        if b in curr[i]:
            five = curr[i]
    for letter in five:
        if letter not in [a, b, d, g]:
            f = letter
    for i in range(3,6):
        if curr[i] != five and curr[i] != three:
            two = curr[i]
    c = cf.replace(f, "")
    for letter in two:
        if letter not in [a, c, d, g]:
            e = letter
    curr_grid = {a:"a", b:"b", c:"c", d:"d", e:"e", f:"f", g:"g"}
    curr_num = ""
    for output in outputs[idx].split():
        curr_str = ""
        for letter in output:
            curr_str += curr_grid[letter]
        curr_num += str(str_dig["".join(sorted(curr_str))])
    total += int(curr_num)
print(total)