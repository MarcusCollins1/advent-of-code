from time import time
t1 = time()
import re
from copy import deepcopy
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 24 2018.txt"
# FILE_NAME = "Day 24 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Group:
    def __init__(self, army: str, units: int, hp: int, damage: int, attackType: str, initiative: int, weak: set[str], immune: set[str]) -> None:
        self.army = army
        self.units = units
        self.hp = hp
        self.damage = damage
        self.attackType = attackType
        self.initiative = initiative
        self.weak = weak
        self.immune = immune

    @property
    def power(self) -> int:
        return self.units * self.damage

    def damageDone(self, attacker: "Group") -> int:
        if attacker.attackType in self.immune: return 0
        
        damage = attacker.power

        if attacker.attackType in self.weak: damage *= 2

        return damage

class SolverPart1:
    def __init__(self, groups: list[Group], boost: int) -> None:
        self.groups: list[Group] = deepcopy(groups)
        for group in self.groups:
            if group.army == "Immune System": group.damage += boost
        
    def doesImmuneSystemWin(self) -> tuple[bool, int]:
        groups = self.groups

        while len(set(g.army for g in groups)) > 1:

            # TARGET SELECTION
            order = sorted(groups, key=lambda g: (g.power, g.initiative), reverse=True)
            targets: dict[int, Group] = {}
            chosen = set()

            for attacker in order:
                enemies = [g for g in groups if g.army != attacker.army and id(g) not in chosen and g.damageDone(attacker) > 0]

                if not enemies: continue

                target = max(enemies, key=lambda g: (g.damageDone(attacker), g.power, g.initiative))

                targets[id(attacker)] = target
                chosen.add(id(target))

            # ATTACKING
            attackOrder = sorted(groups, key=lambda g: g.initiative, reverse=True)

            totalKilled = 0

            for attacker in attackOrder:
                if attacker.units <= 0: continue

                if id(attacker) not in targets: continue

                target = targets[id(attacker)]

                if target.units <= 0: continue

                dealt = target.damageDone(attacker)
                killed = min(target.units, dealt // target.hp)

                target.units -= killed
                totalKilled += killed

            groups = [g for g in groups if g.units > 0]

            # Prevent an infinite battle
            if totalKilled == 0: break

        return (all(g.army == "Immune System" for g in groups), sum(g.units for g in groups))

class Solver:
    def __init__(self, data: list[str]) -> None:
        self.groups: list[Group] = []

        army = ""
        for line in data:
            if not line: continue

            if line.endswith(":"):
                army = line[:-1]
                continue

            nums = list(map(int, re.findall(r"\d+", line)))
            units = nums[0]
            hp = nums[1]
            damage = nums[2]
            initiative = nums[3]

            attackType = re.search(r"(\w+) damage", line).group(1) # type: ignore

            weak = set()
            immune = set()

            if "(" in line:
                extra = line.split("(")[1].split(")")[0]

                for part in extra.split("; "):
                    if part.startswith("weak to "):
                        weak = set(part[8:].split(", "))
                    elif part.startswith("immune to "):
                        immune = set(part[10:].split(", "))

            self.groups.append(Group(army, units, hp, damage, attackType, initiative, weak, immune))

    def solve(self) -> int:
        boost = 0
        while True:
            solver = SolverPart1(self.groups, boost)
            result = solver.doesImmuneSystemWin()
            if result[0]:
                return result[1]
            boost += 1

solver = Solver(data)
print(solver.solve())

print(f"Time Taken: {time()-t1:.2f}s")