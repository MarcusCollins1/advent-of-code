from collections import Counter
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 6 2016.txt"
FILE_NAME = "Day 6 2016 alt.txt"
input_file = open(FOLDER_PATH+FILE_NAME, "r")
messages = input_file.readlines()
input_file.close()
LENGTH = len(messages[0])
message = ""
columns = [""]*LENGTH
for i in messages:
    for j in range(len(i)):
        columns[j] += i[j]

for column in columns:
    message += Counter(column).most_common(1)[0][0]
print(message.strip())