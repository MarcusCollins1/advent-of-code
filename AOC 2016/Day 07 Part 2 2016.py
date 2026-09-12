FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 7 2016.txt"
FILE_NAME = "Day 7 2016 alt.txt"
input_file = open(FOLDER_PATH+FILE_NAME, "r")
data = input_file.readlines()
input_file.close()
addresses = []
for i in data:
    if i[-1] == "\n":
        addresses.append(i[:-1])
    else:
        addresses.append(i)
#addresses = ["aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb"]
total = 0
valid = []
for address in addresses:
    curr_address = address.replace("]", "[")
    list = curr_address.split("[")
    ssl = False
    outside_bab, inside_bab = [], []
    for _ in range(len(list)):
        outside, inside = list[_], list[_]
        if _ % 2 == 0:
            for i in range(len(outside)-2):
                curr = outside[i] + outside[i+1] + outside[i+2]
                if (curr[0] == curr[2]) and (curr[0] != curr[1]):
                    bab = curr[1] + curr[0] + curr[1]
                    outside_bab.append(bab)
        else:
            for i in range(len(inside)-2):
                curr = inside[i] + inside[i+1] + inside[i+2]
                if (curr[0] == curr[2]) and (curr[0] != curr[1]):
                    bab = curr
                    inside_bab.append(bab)
    
    for bab in outside_bab:
        if bab in inside_bab:
            ssl = True
    if ssl:
        total += 1
        valid.append(address)
print(total)
#print(valid)