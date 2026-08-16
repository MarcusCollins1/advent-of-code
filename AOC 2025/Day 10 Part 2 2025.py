from time import time
t1 = time()

from ortools.sat.python import cp_model
import re
from math import gcd
from functools import reduce
from collections import defaultdict

FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2025/"
FILE_NAME = "Day 10 2025.txt"
# FILE_NAME = "Day 10 2025 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

def parseLine(line):
    pattern = r"\[(.*?)\]|\((.*?)\)|\{(.*?)\}"
    parts = re.findall(pattern, line)
    parts = [x for group in parts for x in group if x]
    indicator = parts[0]
    buttons = []
    for item in parts[1:-1]:
        if item.strip() == "":
            buttons.append([])
        else:
            buttons.append([int(x) for x in item.split(",")])
    target = [int(x) for x in parts[-1].split(",")]
    return buttons, target

def buildMatrix(buttons, targetLen):
    m = targetLen
    n = len(buttons)
    A = [[0]*n for _ in range(m)]
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i][j] += 1
    return A

def simpleGcdPrune(A, b):
    m = len(A)
    if m == 0:
        return True
    n = len(A[0])
    for i in range(m):
        row = [A[i][j] for j in range(n) if A[i][j] != 0]
        if not row:
            if b[i] != 0:
                return False
            else: continue
        g = reduce(gcd, row)
        if b[i] % g != 0:
            return False
    return True

def solveMachineOrtools(buttons, target, timeLimitSeconds=30):
    m = len(target)
    A = buildMatrix(buttons, m)
    if not simpleGcdPrune(A, target):
        return None
    model = cp_model.CpModel()
    n = len(buttons)
    bound = sum(target)
    xs = [model.NewIntVar(0, bound, f"x_{j}") for j in range(n)]
    for i in range(m):
        coeffs = [A[i][j] for j in range(n)]
        if all(c == 0 for c in coeffs):
            continue
        model.Add(sum(coeffs[j] * xs[j] for j in range(n)) == target[i])
    model.Minimize(sum(xs))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = timeLimitSeconds
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        total = sum(int(solver.Value(x)) for x in xs)
        return total
    else:
        return None


def solveAllLines(lines, perMachineTimeLimit = 5):
    total = 0
    for idx, line in enumerate(lines):
        if not line.strip(): continue
        buttons, target = parseLine(line)
        res = solveMachineOrtools(buttons, target, perMachineTimeLimit)
        if res is None:
            raise ValueError(f"Machine {idx} is infeasible or unsolved")
        total += res
    return total

print(solveAllLines(data))

print(f"Time Taken: {time()-t1:.3f}s")