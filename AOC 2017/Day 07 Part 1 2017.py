FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 7 2017.txt"
# FILE_NAME = "Day 7 2017 alt.txt"
# FILE_NAME = "Day 7 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Program:
    def __init__(self, name:str, mass:int, children:list = []) -> None:
        self.name = name
        self.mass = mass
        self.children = children
        self.parent = None
    def SetParent(self, parent:str) -> None:
        self.parent = parent

programs = dict()
for line in data:
    line = line.split(" -> ")
    name = line[0].split(" ")[0]
    mass = int(line[0].split(" ")[1].replace("(", "").replace(")", ""))
    if len(line) >= 2:
        children = line[1].split(", ")
        programs[name] = Program(name, mass, children)
    else:
        programs[name] = Program(name, mass)

for program in programs.values():
    for child in program.children:
        programs[child].SetParent(program.name)

for program in programs.values():
    if program.parent == None:
        print(program.name)
        quit()