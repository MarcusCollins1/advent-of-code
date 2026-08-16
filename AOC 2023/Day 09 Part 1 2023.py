FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 09 2023.txt"
# FILE_NAME = "Day 09 2023 alt.txt"
# FILE_NAME = "Day 09 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def get_next(nums:list) -> int:
    differences = [n2-n1 for n1, n2 in zip(nums[:-1], nums[1:])]
    if list(set(differences)) == [0]:
        return 0
    return differences[-1]+get_next(differences)

lines = [list(map(int, line.split())) for line in data]
total = 0
for line in lines:
    curr = line[-1]+get_next(line)
    total += curr
print(total)