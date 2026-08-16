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
#addresses = ["abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn"]
total = 0
valid = []
for address in addresses:
    curr_address = address.replace("]", "[")
    list = curr_address.split("[")
    tls_inside = True
    tls_outside = False
    for _ in range(len(list)):
        outside, inside = list[_], list[_]
        if _ % 2 == 0:
            for i in range(len(outside)-3):
                curr = outside[i] + outside[i+1] + outside[i+2] + outside[i+3]
                if (curr[0] == curr[3]) and (curr[1] == curr[2]) and (curr[0] != curr[1]):
                    tls_outside = True
        else:
            for i in range(len(inside)-3):
                curr = inside[i] + inside[i+1] + inside[i+2] + inside[i+3]
                if (curr[0] == curr[3]) and (curr[1] == curr[2]) and (curr[0] != curr[1]):
                    tls_inside = False
    
        
    if tls_inside and tls_outside:
        total += 1
        valid.append(address)
print(total)
#print(valid)