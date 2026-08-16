# input_file = open("Day 4 2017.txt")
input_file = open("Day 4 2017 alt.txt")
pass_phrases = []
for line in input_file:
    if line[-1] == "\n":
        curr_phrase = line[:-1].split()
    else:
        curr_phrase = line.split()
    pass_phrases.append(curr_phrase)
#print(pass_phrases)
#pass_phrases = [["aa","bb","cc","dd"],["aa","bb","cc","aa"]]

total = 0
for i in pass_phrases:
    words = set()
    flag = True
    for j in i:
        if j not in words:
            words.add(j)
        else:
            flag = False
    if flag == True:
        total+=1
print(total)