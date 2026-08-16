from copy import deepcopy
input_file = open("Day 4 2020.txt")
# input_file = open("Day 4 2020 alt.txt")
# input_file = open("Day 4 2020 test.txt")

passports = [[]]
for line in input_file:
    if line[-1] == "\n":
        line = line[:-1]
    
    if line == "":
        passports.append([])
    else:
        if " " in line:
            passports[-1] += line.split(" ")
        else:
            passports[-1].append(line)

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

count = 0
for passport in passports:
    fields = deepcopy(REQUIRED_FIELDS)
    for line in passport:
        fields.remove(line[:3])
    if fields == [] or fields == ["cid"]:
        count += 1
print(count)