import re
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 17 2024.txt"
# FILE_NAME = "Day 17 2024 test 1.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.read().split("\n\n")]
file.close()

registers: dict[str, int] = {"A": 0, "B": 0, "C": 0}
index = 0
for i, line in enumerate(data[0].splitlines()): registers[["A", "B", "C"][i]] = int(re.findall(r"(\d+)", line)[0])

program = list(map(int, re.findall(r"(\d+)", data[1])))

def GetCombo(operand: int) -> int:
    if 0 <= operand <= 3: return operand
    elif operand == 4: return registers["A"]
    elif operand == 5: return registers["B"]
    elif operand == 6: return registers["C"]
    raise Exception("Invalid operand")

# 0
def adv(operand: int) -> None:
    registers["A"] = (registers["A"]) // (2**GetCombo(operand))
# 1
def bxl(operand: int) -> None:
    registers["B"] = registers["B"] ^ operand
# 2
def bst(operand: int) -> None:
    registers["B"] = GetCombo(operand) % 8
# 3 - Jump
def jnx(operand: int) -> None:
    global index
    if registers["A"] != 0: index = operand-2
# 4
def bxc(operand: int) -> None:
    registers["B"] = registers["B"] ^ registers["C"]
# 5
def out(operand: int) -> None:
    print(GetCombo(operand)%8, end=",")
# 6
def bdv(operand: int) -> None:
    registers["B"] = (registers["A"]) // (2**GetCombo(operand))
# 7
def cdv(operand: int) -> None:
    registers["C"] = (registers["A"]) // (2**GetCombo(operand))

while 0 <= index < len(program)-1:
    opcode, operand = program[index:index+2]
    if opcode == 0: adv(operand)
    if opcode == 1: bxl(operand)
    if opcode == 2: bst(operand)
    if opcode == 3: jnx(operand)
    if opcode == 4: bxc(operand)
    if opcode == 5: out(operand)
    if opcode == 6: bdv(operand)
    if opcode == 7: cdv(operand)
    index += 2