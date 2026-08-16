FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 08 2018.txt"
# FILE_NAME = "Day 08 2018 alt.txt"
# FILE_NAME = "Day 08 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = list(map(int, file.read().split()))
file.close()

class Node:
    def __init__(self) -> None:
        self.metadata: list[int] = []
        self.children: list[Node] = []
    
    def AddChild(self, child: "Node") -> None:
        self.children.append(child)
    
    def SetMetadata(self, metadata: list[int]) -> None:
        self.metadata = metadata
    
    def GetMetadata(self) -> list[int]:
        return self.metadata
    
    def GetMetadataAndChildrenMetadata(self) -> list[list[int]]:
        allMetadata: list[list[int]] = [self.GetMetadata()]
        for child in self.children:
            allMetadata += child.GetMetadataAndChildrenMetadata()
        return allMetadata

class Tree:
    def __init__(self, data: list[int]) -> None:
        self.root: Node|None = None
        self.data = data
        self.index = 0
    
    def GetNextNode(self) -> Node:
        currNode = Node()
        numChildren, numMetadata = self.data[self.index:self.index+2]
        self.index += 2
        for i in range(numChildren):
            currNode.AddChild(self.GetNextNode())
        metadata = self.data[self.index:self.index+numMetadata]
        self.index += numMetadata
        currNode.SetMetadata(metadata)
        return currNode
    
    def ProcessData(self) -> None:
        self.root = self.GetNextNode()

tree = Tree(data)
tree.ProcessData()
if tree.root:
    # print(tree.root.GetMetadataAndChildrenMetadata())
    print(sum([sum (lst) for lst in tree.root.GetMetadataAndChildrenMetadata()]))