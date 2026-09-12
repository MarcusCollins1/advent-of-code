input_file = open("Day 6 2020.txt")
input_file = open("Day 6 2020 alt.txt")
groups = [[]]
for line in input_file:
    if line[-1] == "\n":
        line = line[:-1]
    if line == "":
        groups.append([])
        continue
    groups[-1].append(line)

total = 0
for group in groups:
    letters = set()
    for person in group:
        for letter in person:
            letters.add(letter)
    total += len(letters)
print(total)