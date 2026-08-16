
input_file = open("Day 2 2020.txt")

passwords = []
for line in input_file:
    if line[-1] == "\n":
        passwords.append(line[:-1])
    else:
        passwords.append(line)
#print(check)

total = 0
for i in passwords:
    curr_letter = i[i.index(":")-1]
    curr_min = int(i[:i.index("-")])
    curr_max = int(i[i.index("-")+1:i.index(" ")])
    curr_check = i[i.index(":")+2:]
    num_appear = int(curr_check.count(curr_letter))
    check_1 = curr_check[curr_min-1]
    check_2 = curr_check[curr_max-1]
    if check_1 == curr_letter or check_2 == curr_letter:
        if check_1 != curr_letter or check_2 != curr_letter:
            total += 1
print(total)