FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 06 2023.txt"
# FILE_NAME = "Day 06 2023 alt.txt"
# FILE_NAME = "Day 06 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

times, distances = list(map(int, data[0].split()[1:])), list(map(int, data[1].split()[1:]))

def Margin(time:int, distance:int) -> int:
    start, end = -1, -1
    for i in range(time):
        if i * (time-i) > distance:
            if start == -1:
                start = i
            else:
                end = i
    return end-start + 1

total = 1

for time, distance in zip(times, distances):
    total *= Margin(time, distance)

print(total)
