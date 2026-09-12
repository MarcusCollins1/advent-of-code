FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 12 2015.txt"
# FILE_NAME = "Day 12 2015 alt.txt"
# FILE_NAME = "Day 12 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()][0]
file.close()

data = eval(data)

def getValue(item) -> int:
    if isinstance(item, int): return item
    if isinstance(item, str): return 0
    if isinstance(item, list): return sum([getValue(x) for x in item])
    if isinstance(item, dict):
        if "red" in item.values(): return 0
        else: return sum([getValue(x) for x in item.values()])
    return 0

print(getValue(data))