from time import time
t1 = time()
from collections import deque
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2017/"
FILE_NAME = "Day 18 2017.txt"
# FILE_NAME = "Day 18 2017 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip().split() for x in file.readlines()]
file.close()

queues = [deque(), deque()]

programs = [
    {
        "regs": {"p": 0},
        "ip": 0,
        "sent": 0
    },
    {
        "regs": {"p": 1},
        "ip": 0,
        "sent": 0
    }
]

def getValue(x, regs):
    try:
        return int(x)
    except:
        return regs.get(x, 0)

def runProgram(program, pid, queues, instructions):
    regs = program["regs"]
    ip = program["ip"]

    while 0 <= ip < len(instructions):
        parts = instructions[ip]
        op = parts[0]

        if op == "snd":
            value = getValue(parts[1], regs)
            queues[1 - pid].append(value)
            program["sent"] += 1
            ip += 1

        elif op == "set":
            regs[parts[1]] = getValue(parts[2], regs)
            ip += 1

        elif op == "add":
            regs[parts[1]] = regs.get(parts[1], 0) + getValue(parts[2], regs)
            ip += 1

        elif op == "mul":
            regs[parts[1]] = regs.get(parts[1], 0) * getValue(parts[2], regs)
            ip += 1

        elif op == "mod":
            regs[parts[1]] = regs.get(parts[1], 0) % getValue(parts[2], regs)
            ip += 1

        elif op == "rcv":
            if not queues[pid]:
                program["ip"] = ip
                return "waiting"

            regs[parts[1]] = queues[pid].popleft()
            ip += 1

        elif op == "jgz":
            x = getValue(parts[1], regs)

            ip += getValue(parts[2], regs) if x > 0 else 1

    program["ip"] = ip
    return "terminated"

while True:
    status0 = runProgram(programs[0], 0, queues, data)
    status1 = runProgram(programs[1], 1, queues, data)

    if (
        status0 == "waiting"
        and status1 == "waiting"
        and not queues[0]
        and not queues[1]
    ): break

    if status0 == "terminated" and status1 == "terminated": break

print(programs[1]["sent"])
print(f"Time Taken: {time()-t1:.2f}s")