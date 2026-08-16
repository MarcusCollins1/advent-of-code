import re
import heapq
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 17 2024.txt"
# FILE_NAME = "Day 17 2024 test 2.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.read().split("\n\n")]
file.close()

program = list(map(int, re.findall(r"(\d+)", data[1])))

def Step(A: int) -> tuple[int, int]:
    B = A % 8
    B = B ^ 5
    C = A >> B
    B = B ^ 6 ^ C
    return B, C
def Search3Bits(pA: int):
    validAs = []
    for Ashift in range(8):
        A = (pA << 3) + Ashift
        B, C = Step(A)
        if (B%8) == program[-(A.bit_length()//3 + 1)]: validAs.append(A)
    return validAs

queue: list[int] = [0]
minA: int = 1 << (3*(len(program)-1))
while queue:
    A = heapq.heappop(queue)
    if A >= minA:
        print(A)
        break
    if (A.bit_length()//3+1) < len(program):
        for nA in Search3Bits(A): heapq.heappush(queue, nA)