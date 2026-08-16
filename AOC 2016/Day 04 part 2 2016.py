from collections import Counter
import heapq
FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 4 2016.txt"
FILE_NAME = "Day 4 2016 alt.txt"
input_file = open(FOLDER_PATH+FILE_NAME, "r")
rooms = input_file.readlines()
input_file.close()
alphabet = list("abcdefghijklmnopqrstuvwxyz")

valid = []
for room in rooms:
    room = room.replace("]", "")
    room = room.replace("[", "-")
    room_list = room.split("-")
    name, id, checksum = "".join(room_list[:-2]), int(room_list[-2]), sorted(room_list[-1])
    checksum = "".join(sorted(list(checksum[1:])))
    top5 = heapq.nsmallest(5, Counter(list(name)).items(),key=lambda kv: (-kv[1], kv[0]))
    check = ""
    for i in top5:
        check += i[0]
    check = "".join(sorted(check))
    if check == checksum:
        valid.append(room)

for room in valid:
    room = room.replace("]", "")
    room = room.replace("[", "-")
    room_list = room.split("-")
    name, id, checksum = "".join(room_list[:-2]), int(room_list[-2]), sorted(room_list[-1])
    checksum = "".join(sorted(list(checksum[1:])))
    new_name = ""
    for _ in range(id):
        new_name = ""
        for j in range(len(name)):
            curr_letter = name[j]
            try:
                new_letter = alphabet[(alphabet.index(curr_letter)+1)%26]
            except:
                new_letter = " "
            new_name += new_letter
        name = new_name
    if "northpole" in name:
        print(name, id)