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
def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

total = 0
for i in pass_phrases:
    words = []
    flag = True
    for j in i:
        flag_2 = True
        for k in words:
            
            if isAnagram(j,k) == True:
                flag = False
                flag_2 = False
        if flag_2 == True:
            words.append(j)
    if flag == True:
        total+=1
print(total)