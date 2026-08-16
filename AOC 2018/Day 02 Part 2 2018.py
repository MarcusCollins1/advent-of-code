input_file = open("AOC 2018 Day 2.txt")
id_list = []
for line in input_file:
    if line[-1] == "\n":
        id_list.append(line[:-1])
    else:
        id_list.append(line)
#print(id_list)
#id_list = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
for i in id_list:
    for j in id_list:
        if i != j:
            num_changes = 0
            for a in range(len(i)):
                if i[a] != j[a]:
                    num_changes += 1
            if num_changes == 1:
                # to do find what they have in common
                #print(i)
                #print(j)
                common = []
                for k in range(len(i)):
                    if i[k] == j[k]:
                        common.append(i[k])
                break
print(*common, sep="")
