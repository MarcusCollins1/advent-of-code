import re
from enum import Enum
from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 22 2015.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

bossHitPoints, bossDamage = list(map(int, [re.findall(r"(\d+)",line)[0] for line in data])) #type:ignore
class Spell(Enum):
    MAGIC_MISSILE = (53, lambda wizard: wizard.boss.Damage(4))
    DRAIN = (73, lambda wizard: (wizard.boss.Damage(2), wizard.Heal(2)))
    SHIELD = (113, lambda wizard: setattr(wizard, 'shieldEffect', 6))
    POISON = (173, lambda wizard: setattr(wizard, 'poisonEffect', 6))
    RECHARGE = (229, lambda wizard: setattr(wizard, 'rechargeEffect', 5))

    def __init__(self, cost: int, effect) -> None:
        self.cost = cost
        self.effect = effect

    def Cast(self, wizard: 'Wizard') -> None:
        self.effect(wizard)

class Boss:
    def __init__(self, hitPoints: int, damage: int) -> None:
        self.hitPoints = hitPoints
        self.damage = damage
    
    def Damage(self, damage: int) -> None:
        self.hitPoints -= damage

class Wizard:
    def __init__(self, hitPoints: int, mana: int, boss: Boss, shieldEffect: int = 0, poisonEffect: int = 0, rechargeEffect: int = 0) -> None:
        self.hitPoints = hitPoints
        self.mana = mana
        self.boss = boss

        self.shield = 7
        self.shieldEffect = shieldEffect
        self.poisonEffect = poisonEffect
        self.rechargeEffect = rechargeEffect
    
    def ApplyEffects(self) -> None:
        if self.shieldEffect > 0:
            self.shieldEffect -= 1
        if self.poisonEffect > 0:
            self.boss.Damage(3)
            self.poisonEffect -= 1
        if self.rechargeEffect > 0:
            self.mana += 101
            self.rechargeEffect -= 1

    def Damage(self, damage: int) -> None:
        self.hitPoints -= max(1, damage - (self.shield if self.shieldEffect > 0 else 0))

    def Heal(self, amount: int) -> None:
        self.hitPoints += amount

    def Cast(self, spell: Spell) -> int:
        self.mana -= spell.cost
        spell.Cast(self)
        return spell.cost

queue = [(Wizard(50, 500, Boss(bossHitPoints, bossDamage)), 0, 0)]
lowestCost = float("inf")
while queue:
    wizard, costSoFar, numTurns = queue.pop(0)
    if costSoFar >= lowestCost: continue
    # print(wizard.boss.hitPoints, costSoFar, numTurns)
    for spell in Spell:
        if wizard.mana < spell.cost: continue
        if spell == Spell.SHIELD and wizard.shieldEffect > 1: continue
        if spell == Spell.POISON and wizard.poisonEffect > 1: continue
        if spell == Spell.RECHARGE and wizard.rechargeEffect > 1: continue
        newWizard = Wizard(wizard.hitPoints, wizard.mana, Boss(wizard.boss.hitPoints, wizard.boss.damage), wizard.shieldEffect, wizard.poisonEffect, wizard.rechargeEffect)
        newWizard.ApplyEffects()
        newCost = costSoFar + newWizard.Cast(spell)
        if newCost >= lowestCost: continue

        if newWizard.boss.hitPoints <= 0:
            lowestCost = min(lowestCost, newCost)
            continue

        newWizard.ApplyEffects()
        newWizard.Damage(newWizard.boss.damage)
        if newWizard.hitPoints <= 0:
            continue

        if newWizard.boss.hitPoints <= 0:
            lowestCost = min(lowestCost, newCost)
            continue
        
        if newCost < lowestCost:
            queue.append((newWizard, newCost, numTurns + 2))
print(lowestCost)
deltaT = time() - t1
print(f"Time: {deltaT:.2f}s")