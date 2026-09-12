from copy import deepcopy
# input_file = open("Day 4 2020.txt")
input_file = open("Day 4 2020 alt.txt")
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
        key, value = line.split(":")
        if key == "byr":
            if 1920 <= int(value) <= 2002:
                fields.remove(key)
        elif key == "iyr":
            if 2010 <= int(value) <= 2020:
                fields.remove(key)
        elif key == "eyr":
            if 2020 <= int(value) <= 2030:
                fields.remove(key)
        elif key == "hgt":
            num = value[:-2]
            unit = value[-2:]
            if (unit == "cm" and 150 <= int(num) <= 193) or (unit == "in" and 59 <= int(num) <= 76):
                fields.remove(key)
        elif key == "hcl":
            if value[0] ==  "#":
                value = value[1:]
                flag = True
                for letter in value:
                    if letter not in "0987654321abcdef":
                        flag = False
                        break
                if flag:
                    fields.remove(key)
        elif key == "ecl":
            if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                fields.remove(key)
        elif key == "pid":
            try:
                if len(value) == 9:
                    int(value)
                    fields.remove(key)
            except:
                pass
        elif key == "cid":
            fields.remove(key)
    if fields == [] or fields == ["cid"]:
        count += 1
print(count)