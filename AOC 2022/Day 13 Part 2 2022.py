FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 13 2022.txt"
# FILE_NAME = "Day 13 2022 alt.txt"
# FILE_NAME = "Day 13 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

packets = []
for line in data:
    line = line.strip()
    if line != "":
        packets.append(eval(line))
packets.append([[2]])
packets.append([[6]])

def check(ls1, ls2):
    for item1, item2 in zip(ls1, ls2):
        if type(item1) != type(item2):
            if type(item1) != list:
                item1 = [item1]
            else:
                item2 = [item2]
        if type(item1) == int:
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
        if type(item1) == list:
            x = check(item1, item2)
            if x != None:
                if x:
                    return True
                else:
                    return False
    if len(ls1) < len(ls2):
        return True
    elif len(ls1) > len(ls2):
        return False


sorted_packets = []
while packets:
    curr_packet = packets.pop(0)
    count = 0
    for packet in sorted_packets:
        # will return true if the current packet comes before the packet
        if check(curr_packet, packet):
            break
        count += 1
    sorted_packets.insert(count, curr_packet)

print((sorted_packets.index([[2]])+1)*(sorted_packets.index([[6]])+1))