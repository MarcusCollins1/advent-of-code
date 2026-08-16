from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 15 2023.txt"
# FILE_NAME = "Day 15 2023 alt.txt"
# FILE_NAME = "Day 15 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().split(",")
file.close()

class Lens:
    def __init__(self, label:str, focal_length:int) -> None:
        self.label = label
        self.focal_length = focal_length
    
    def __repr__(self) -> str:
        return f"{self.label} {self.focal_length}"

def Hash(s:str) -> int:
    value = 0
    for letter in s:
        value += ord(letter)
        value *= 17
        value %= 256
    return value

boxes = defaultdict(list[Lens])

for line in data:
    if "-" in line:
        label = line.split("-")[0]
        box = Hash(label)
        output = []
        for lens in boxes[box]:
            if lens.label != label:
                output.append(lens)
        boxes[box] = output
    else:
        label, focal_length = line.split("=")
        focal_length = int(focal_length)
        box = Hash(label)
        for i, lens in enumerate(boxes[box]):
            if lens.label == label:
                boxes[box][i].focal_length = focal_length
                break
        else:
            boxes[box].append(Lens(label, focal_length))

total = 0
for key, val in boxes.items():
    box_score = key+1
    for i, lens in enumerate(val):
        total += box_score*(i+1)*lens.focal_length
print(total)