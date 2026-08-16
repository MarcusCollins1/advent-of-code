FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 05 2023.txt"
# FILE_NAME = "Day 05 2023 alt.txt"
# FILE_NAME = "Day 05 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

lines = []
curr = []
for line in data:
    if line == "":
        lines.append(curr)
        curr = []
    else:
        curr.append(line)
if curr != []:
    lines.append(curr)

# dest source range
def Convert(curr_ranges:list, curr_map:list) -> list:
    output = []
    for r in curr_ranges:
        for m in curr_map:
            source, dest = [m[1], m[1]+m[2]-1], [m[0], m[0]+m[2]-1]
            offset = dest[0]-source[0]
            # all fits in
            if source[0] <= r[0] <= r[1] <= source[1]:
                output.append([r[0] + offset, r[1]+offset])
                break
            # split range
            # split in map, not in map
            elif source[0] < r[0] < source[1] < r[1]:
                output += Convert([[r[0], source[1]], [source[1]+1, r[1]]], curr_map)
                break
            # split not in map, in map, not in map
            elif r[0] < source[0] < source[1] < r[1]:
                output += Convert([[r[0], source[0]-1], [source[0], source[1]], [source[1]+1, r[1]]], curr_map)
                break
            # split not in map, in map
            elif r[0] < source[0] < r[1] < source[1]:
                output += Convert([[r[0], source[0]-1], [source[0], r[1]]], curr_map)
                break
        else:
            output.append(r)
    return output

x = lines[0][0].split(" ")[1:]
ranges = []
for i in range(len(x)//2):
    ranges.append([int(x[i*2]), int(x[i*2])+int(x[i*2+1])-1])

for section in lines[1:]:
    curr_map = [list(map(int, x.split())) for x in section[1:]]
    ranges = Convert(ranges, curr_map)

lowest = min([x[0] for x in ranges])
print(lowest)