import hashlib
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 04 2015.txt"
FILE_NAME = "Day 04 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

data = data[0]

count = 1
while True:
    string = data+str(count)
    if hashlib.md5(string.encode()).hexdigest()[:6] == "000000":
        print(count)
        break
    count += 1