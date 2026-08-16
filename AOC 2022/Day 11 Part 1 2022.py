FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 11 2022.txt"
# FILE_NAME = "Day 11 2022 alt.txt"
# FILE_NAME = "Day 11 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()


class Monkey:
    def __init__(self, starting_items, operation, test, monkey_true, monkey_false):
        self.items = list(map(int, starting_items.split(", ")))
        self.operation = operation
        self.test = int(test)
        self.monkey_true = int(monkey_true)
        self.monkey_false = int(monkey_false)
        self.num_inspects = 0
    
    def goThroughItems(self):
        global monkeys
        for item in self.items:
            self.num_inspects += 1
            item = eval(self.operation)//3
            if item%self.test == 0:
                monkeys[self.monkey_true].items.append(item)
            else:
                monkeys[self.monkey_false].items.append(item)
        self.items = []
        


monkeys = []
curr_monkey = []
for line in data:
    line = line.strip()
    if line == "":
        continue
    if line.split()[0] == "Monkey":
        if curr_monkey != []:
            monkeys.append(Monkey(curr_monkey[0], curr_monkey[1], curr_monkey[2], curr_monkey[3], curr_monkey[4]))
        curr_monkey = []
    elif line.split()[0] == "Starting":
        curr_monkey.append(line.replace("Starting items: ", ""))
    elif line.split()[0] == "Operation:":
        curr_monkey.append(line.replace("Operation: new = ", "").replace("old", "item"))
    elif line.split()[0] == "Test:":
        curr_monkey.append(line.split()[-1])
    elif line.split()[0] == "If":
        curr_monkey.append(int(line.split()[-1]))
monkeys.append(Monkey(curr_monkey[0], curr_monkey[1], curr_monkey[2], curr_monkey[3], curr_monkey[4]))

for _ in range(20):
    for monkey in monkeys:
        monkey.goThroughItems()

inspects = []
for monkey in monkeys:
    inspects.append(monkey.num_inspects)
inspects = sorted(inspects)

print(inspects[-2]*inspects[-1])