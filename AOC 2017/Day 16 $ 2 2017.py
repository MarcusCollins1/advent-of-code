from time import time
import re

t1 = time()

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 16 2017.txt"
# FILE_NAME = "Day 16 2017 test.txt"

with open(FOLDER_PATH + FILE_NAME, "r") as file:
    data = file.readline().strip().split(",")

def dance(order):
    for move in data:
        if move[0] == "s":
            num = int(move[1:])
            order = order[-num:] + order[:-num]

        elif move[0] == "x":
            a, b = map(int, move[1:].split("/"))
            order[a], order[b] = order[b], order[a]

        elif move[0] == "p":
            a, b = move[1:].split("/")

            ia = order.index(a)
            ib = order.index(b)

            order[ia], order[ib] = order[ib], order[ia]

    return order


start = list("abcdefghijklmnop")

seen = {}
states = []

order = start.copy()
i = 0

while ''.join(order) not in seen:
    state = ''.join(order)

    seen[state] = i
    states.append(state)

    order = dance(order)
    i += 1

cycle_start = seen[''.join(order)]
cycle_length = i - cycle_start

print("Cycle start:", cycle_start)
print("Cycle length:", cycle_length)

target = 1_000_000_000

index = cycle_start + (target - cycle_start) % cycle_length

print(states[index])
print(f"Time Taken: {time() - t1:.2f}s")