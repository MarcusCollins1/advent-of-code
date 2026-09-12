FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 9 2016.txt"
# FILE_NAME = "Day 9 2016 alt.txt"
# FILE_NAME = "Day 9 2016 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Marker:
    def __init__(self, num_char:int, num_repeats:int, length:int) -> None:
        self.num_char = num_char
        self.num_repeats = num_repeats
        self.length = length

def GetMarker(data:str, i:int) -> Marker:
    num_chars = ""
    num_repeats = ""
    i += 1
    while True:
        if data[i] == "x":
            i += 1
            break
        num_chars += data[i]
        i += 1
    while True:
        if data[i] == ")":
            break
        num_repeats += data[i]
        i += 1
    return Marker(int(num_chars), int(num_repeats), len(num_chars)+len(num_repeats)+3)

data = data[0]
output = ""
i = 0
while i < len(data):
    if data[i] != "(":
        output += data[i]
        i += 1
    else:
        marker = GetMarker(data, i)
        i += marker.length
        output += data[i:i+marker.num_char]*marker.num_repeats
        i += marker.num_char

print(len(output))