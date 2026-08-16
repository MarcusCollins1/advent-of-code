import re
from enum import Enum
from time import time
t1 = time()
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 22 2015.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

bossHitPoints, bossDamage = list(map(int, [re.findall(r"(\d+)", line)[0] for line in data]))  # type: ignore

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
        # Apply repeating actions first
        if self.poisonEffect > 0:
            self.boss.Damage(3)
        if self.rechargeEffect > 0:
            self.mana += 101
        # shield has no per-turn action; it affects damage calculation when boss attacks

        # Then decrement timers
        if self.shieldEffect > 0:
            self.shieldEffect -= 1
        if self.poisonEffect > 0:
            self.poisonEffect -= 1
        if self.rechargeEffect > 0:
            self.rechargeEffect -= 1

    def Damage(self, damage: int) -> None:
        effective_armor = self.shield if self.shieldEffect > 0 else 0
        self.hitPoints -= max(1, damage - effective_armor)

    def Heal(self, amount: int) -> None:
        self.hitPoints += amount

    def Cast(self, spell: Spell) -> int:
        self.mana -= spell.cost
        spell.Cast(self)
        return spell.cost

# queue entries: (wizard_state, costSoFar)
queue = [(Wizard(50, 500, Boss(bossHitPoints, bossDamage)), 0)]
lowestCost = float("inf")

while queue:
    wizard, costSoFar = queue.pop(0)
    if costSoFar >= lowestCost:
        continue

    # try each spell
    for spell in Spell:
        # copy state including effect timers
        newBoss = Boss(wizard.boss.hitPoints, wizard.boss.damage)
        newWizard = Wizard(wizard.hitPoints, wizard.mana, newBoss, wizard.shieldEffect, wizard.poisonEffect, wizard.rechargeEffect)

        # ---- Player turn start (HARD MODE) ----
        newWizard.hitPoints -= 1  # hard mode HP loss
        if newWizard.hitPoints <= 0:
            continue

        # apply effects at start of player's turn
        newWizard.ApplyEffects()
        if newWizard.boss.hitPoints <= 0:
            # boss died from effects before any spell is cast; cost doesn't increase
            lowestCost = min(lowestCost, costSoFar)
            continue

        # now check whether effect spells are currently active (must be after effects applied)
        if spell == Spell.SHIELD and newWizard.shieldEffect > 0:
            continue
        if spell == Spell.POISON and newWizard.poisonEffect > 0:
            continue
        if spell == Spell.RECHARGE and newWizard.rechargeEffect > 0:
            continue

        # affordability: mana may have changed due to Recharge, so check current mana
        if newWizard.mana < spell.cost:
            continue

        # cast the spell
        newCost = costSoFar + newWizard.Cast(spell)
        if newCost >= lowestCost:
            continue

        # check immediate boss death after cast
        if newWizard.boss.hitPoints <= 0:
            lowestCost = min(lowestCost, newCost)
            continue

        # ---- Boss turn start ----
        newWizard.ApplyEffects()
        if newWizard.boss.hitPoints <= 0:
            lowestCost = min(lowestCost, newCost)
            continue

        # boss attacks
        newWizard.Damage(newWizard.boss.damage)
        if newWizard.hitPoints <= 0:
            continue

        # still alive, enqueue
        if newCost < lowestCost:
            queue.append((newWizard, newCost))

print(lowestCost)
deltaT = time() - t1
print(f"Time: {deltaT:.2f}s")
