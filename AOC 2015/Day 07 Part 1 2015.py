FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 07 2015.txt"
FILE_NAME = "Day 07 2015 alt.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

wires = dict()
for line in data:
    wire = line.strip().split(" -> ")
    wires[wire[-1]] = wire[0].split()

solved = {}

def solve(node):
    
    if node.isnumeric():
        return int(node)
    
    if node not in solved:
        ops = wires[node]

        if len(ops) == 1:
            n = solve(ops[0])
        
        else:
            op = ops[-2]
            if op == "AND":
                n = solve(ops[0]) & solve(ops[2])
            elif op == 'OR':
                n = solve(ops[0]) | solve(ops[2])
            elif op == 'NOT':
              n = ~solve(ops[1]) & 65535
            elif op == 'RSHIFT':
              n = solve(ops[0]) >> solve(ops[2])
            else: #    'LSHIFT':
              n = solve(ops[0]) << solve(ops[2]) & 65535
        
        solved[node] = n

    return solved[node]

print(solve("a"))