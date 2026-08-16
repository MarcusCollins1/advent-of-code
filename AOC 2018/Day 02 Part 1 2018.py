input_file = open("AOC 2018 Day 2.txt", "r")
id_list = []
for line in input_file:
    if line[-1] == "\n":
        id_list.append(line[:-1])
    else:
        id_list.append(line)
#print(id_list)
#id_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
twice_total = 0
thrice_total = 0
for i in id_list:
    flag = True
    for j in i:
        if i.count(j) == 2 and flag:
            twice_total += 1
            flag = False
    flag = True
    for j in i:
        if i.count(j) == 3 and flag:
            thrice_total += 1 
            flag = False
print(thrice_total*twice_total)