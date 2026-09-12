FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 7 2017.txt"
FILE_NAME = "Day 7 2017 alt.txt"
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
        self.totalMass = None
    def SetParent(self, parent:str) -> None:
        self.parent = parent
    def GetTotalMass(self) -> int:
        global programs
        self.totalMass = self.mass + sum([programs[child].GetTotalMass() for child in self.children])
        return self.totalMass
    def IsBalanced(self):
        global programs
        masses = [programs[child].totalMass for child in self.children]
        if len(set(masses)) == 1:
            return 0
        else:
            unique_masses = list(set(masses))
            if masses.count(unique_masses[0]) < masses.count(unique_masses[1]):
                wrong_child = self.children[masses.index(unique_masses[0])]
                return [unique_masses[1], wrong_child, unique_masses[1]-(programs[wrong_child].totalMass-programs[wrong_child].mass)]
            elif masses.count(unique_masses[0]) > masses.count(unique_masses[1]):
                wrong_child = self.children[masses.index(unique_masses[1])]
                return [unique_masses[0], wrong_child, unique_masses[0]-(programs[wrong_child].totalMass-programs[wrong_child].mass)]
            else:
                print("AHHHHH")
                return 1
    
    def __repr__(self) -> str:
        return f"Program: Name: {self.name}, Mass: {self.mass}, Total Mass: {self.totalMass}, Parent: {self.parent if self.parent != None else 'Root'}, Children: {', '.join(self.children)}"

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

root = Program("", 0)
for program in programs.values():
    if program.parent == None:
        root = program
        break

root.GetTotalMass()

queue = [root]
while queue:
    curr = queue.pop()
    balanced = curr.IsBalanced()
    children_balanced = True
    unbalanced_child = ""
    for child in curr.children:
        if programs[child].IsBalanced() != 0:
            unbalanced_child = child
            children_balanced = False
    if not (balanced == 0) and children_balanced:
        print(balanced[2]) # type:ignore
        break
    else:
        queue.append(programs[unbalanced_child])