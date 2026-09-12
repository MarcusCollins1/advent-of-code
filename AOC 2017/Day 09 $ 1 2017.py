FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 09 2017.txt"
# FILE_NAME = "Day 09 2017 alt.txt"
# FILE_NAME = "Day 09 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.read().strip()
file.close()

class Group:
    def __init__(self, parent: "Group|None") -> None:
        self.parent = parent
        self.children: list[Group] = []
    
    def AddChild(self, child: "Group") -> None:
        self.children.append(child)
    
    def GetScore(self, score: int) -> int:
        return score + sum([child.GetScore(score+1) for child in self.children])
    
    def __repr__(self) -> str:
        x = ''.join([child.__repr__() for child in self.children])
        return f"[{x}]"

root: Group

openGroups: list[Group] = []
currentGroup: Group|None = None
inGarbage: bool = False
ignore: bool = False
for character in data:
    if ignore:
        ignore = False
        continue
    if inGarbage:
        if character == ">":
            inGarbage = False
        elif character == "!":
            ignore = True
    else:
        if character == "<":
            inGarbage = True
        elif character == "{":
            newGroup = Group(currentGroup)
            openGroups.append(newGroup)
            if currentGroup:
                currentGroup.AddChild(newGroup)
            else:
                root = newGroup
            currentGroup = newGroup
        elif character == "}":
            openGroups.pop(-1)
            if openGroups: currentGroup = openGroups[-1]


print(root.GetScore(1))