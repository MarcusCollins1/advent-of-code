import re
FOLDER_PATH = "C:/Users/mjdj2/OneDrive/Documents/AOC/AOC 2015/"
FILE_NAME = "Day 15 2015.txt"
# FILE_NAME = "Day 15 2015 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int) -> None:
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

def cookieScore(ingredients: list[tuple[int, Ingredient]]) -> int:
    if cookieCalories(ingredients) != 500: return -1
    totalCapacity = sum(amount*ingredient.capacity for amount, ingredient in ingredients)
    totalDurability = sum(amount*ingredient.durability for amount, ingredient in ingredients)
    totalFlavor = sum(amount*ingredient.flavor for amount, ingredient in ingredients)
    totalTexture = sum(amount*ingredient.texture for amount, ingredient in ingredients)
    if (totalCapacity <= 0) or (totalDurability <= 0) or (totalFlavor <= 0) or (totalTexture <= 0): return 0
    return totalCapacity*totalDurability*totalFlavor*totalTexture

def cookieCalories(ingredients: list[tuple[int, Ingredient]]) -> int:
    return sum(ingredient.calories*amount for amount, ingredient in ingredients)

def getIngredientFromLine(line: str) -> Ingredient:
    pattern = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    match = re.match(pattern, line)
    if match != None:
        name, capacity, durability, flavor, texture, calories = match.groups()
        return Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories))
    raise Exception("Line does not match pattern")

def getWaysToSumTo(target: int, n: int) -> list[list[int]]:
    results = []
    def backtrack(remaining: int, slots: int, current: list) -> None:
        if slots == 0:
            if remaining == 0:
                results.append(current[:])
            return
        for val in range(remaining+1):
            current.append(val)
            backtrack(remaining-val, slots-1, current)
            current.pop()
    backtrack(target, n, [])
    return results

ingredients = [getIngredientFromLine(line) for line in data]

proportions = getWaysToSumTo(100, len(ingredients))
best = max([cookieScore(list(zip(proportion, ingredients))) for proportion in proportions])
print(best)