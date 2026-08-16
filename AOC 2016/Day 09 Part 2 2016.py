FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 9 2016.txt"
# FILE_NAME = "Day 9 2016 alt.txt"
# FILE_NAME = "Day 9 2016 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def Decompress(data:str) -> int:
    if "(" not in data:
        return len(data)
    length = 0
    while "(" in data:
        length += data.find("(")
        data = data[data.find("("):]
        marker = data[1:data.find(")")].split("x")
        data = data[data.find(")")+1:]
        length += Decompress(data[:int(marker[0])] * int(marker[1]))
        data = data[int(marker[0]):]
    length += len(data)
    return length

data = data[0]
print(Decompress(data))