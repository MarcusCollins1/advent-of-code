from copy import deepcopy
# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 4 2021.txt", "r")
# home account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 4 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 4 2021 test.txt", "r")

file = input_file.readlines()
nums = file[0][:-1].split(",")
file = file[2:]
data = []
curr = []
for line in file:
    if line == "\n" or line == "":
        data.append(curr)
        curr = []
    elif line[-1] == "\n":
        curr.append(line[:-1].split())
    else:
        curr.append(line.split())
data.append(curr)


def display(set):
    for card in set:
        for row in card:
            print(*row)
        print()

def has_won(card):
    rows  = deepcopy(card)
    cols = [[]]*len(rows[0])
    for i in rows:
        for j in range(len(i)):
            cols[j].append(i[j])
    for row in rows:
        if row.count("x") == len(row):
            return True
    for col in cols:
        if (col).count("x") == len(col):
            return True
    return False
flag = True
while flag:
    curr_num = nums.pop(0)
    for card_index in range(len(data)):
        for row_index in range(len(data[card_index])):
            curr_row = deepcopy(data[card_index][row_index])
            for num_index in range(len(curr_row)):
                if curr_row[num_index] == curr_num:
                    curr_row[num_index] = "x"
            data[card_index][row_index] = deepcopy(curr_row)
    
    # check if a card has won
    for card in data:
        if has_won(card):
            flag = False
            break
            

total = 0
for row in card:
    for num in row:
        if num != "x":
            total += int(num)
print(total*int(curr_num))
