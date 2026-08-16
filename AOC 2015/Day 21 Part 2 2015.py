import re
from itertools import combinations
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 21 2015.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

bossHitPoints, bossDamage, bossArmor = list(map(int, [re.findall(r"(\d+)",line)[0] for line in data])) #type:ignore

class Player:
    def __init__(self, hitPoints: int, damage: int, armor: int) -> None:
        self.hitPoints = hitPoints
        self.damage = damage
        self.armor = armor
    
    def Damage(self, damage: int) -> None:
        self.hitPoints -= max(1, damage-self.armor)

WEAPONS = {8: (4, 0), 10: (5, 0), 25: (6, 0), 40: (7, 0), 74: (8, 0)}
ARMOR = {0: (0, 0), 13: (0, 1), 31: (0, 2), 53: (0, 3), 75: (0, 4), 102: (0, 5)}
RINGS = {25: (1, 0), 50: (2, 0), 100: (3, 0), 20: (0, 1), 40: (0, 2), 80: (0, 3)}

def DoesPlayerWin(player: Player, boss: Player) -> bool:
    playerTurn = True
    while player.hitPoints > 0 and boss.hitPoints > 0:
        if playerTurn:
            boss.Damage(player.damage)
        else:
            player.Damage(boss.damage)
        playerTurn = not playerTurn
    return player.hitPoints > 0

greatestCost = 0
for weaponCost, weaponBonus in WEAPONS.items():
    for armorCost, armorBonus in ARMOR.items():
        for numRings in range(3):
            for rings in combinations(RINGS.items(), numRings):
                totalRingCost = sum(ring[0] for ring in rings)
                totalCost = weaponCost+armorCost+totalRingCost
                if totalCost <= greatestCost: continue
                playerDamage = weaponBonus[0] + armorBonus[0] + sum(ring[1][0] for ring in rings)
                playerArmor = weaponBonus[1] + armorBonus[1] + sum(ring[1][1] for ring in rings)
                player = Player(100, playerDamage, playerArmor)
                boss = Player(bossHitPoints, bossDamage, bossArmor)
                if not DoesPlayerWin(player, boss): greatestCost = max(greatestCost, totalCost)
print(greatestCost)