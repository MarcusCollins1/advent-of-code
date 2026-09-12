import time
start = time.time()
input_file = open("Day 2 2020.txt")

passwords = []
for line in input_file:
    if line[-1] == "\n":
        passwords.append(line[:-1])
    else:
        passwords.append(line)
#print(passwords)

total = 0
for i in passwords:
    i =  i.replace(":", "")
    curr_list = i.split()
    curr_letter = curr_list[1]
    curr_min = int(curr_list[0].split("-")[0])
    curr_max = int(curr_list[0].split("-")[1])
    curr_password = curr_list[2]
    num_appear = int(curr_password.count(curr_letter))
    if curr_min <= num_appear <= curr_max:
        total += 1
print(total)
end = time.time()
print(start)