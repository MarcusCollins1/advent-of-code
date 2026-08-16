from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 05 2024.txt"
# FILE_NAME = "Day 05 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
pageOrderingRules, pagesToProduce = file.read().split("\n\n")
pageOrderingRules = [list(map(int, line.split("|"))) for line in pageOrderingRules.splitlines()]
pagesToProduce = [list(map(int, line.split(","))) for line in pagesToProduce.splitlines()]
file.close()

before: defaultdict[int, list[int]] = defaultdict(list)
for n1, n2 in pageOrderingRules:
    before[n2].append(n1)

def CheckValid(pages: list[int], rules: list[list[int]]) -> bool:
    for page1Index, page1 in enumerate(pages):
        for page2 in pages[page1Index+1:]:
            for n1, n2 in rules:
                if n1 == page2 and n2 == page1: return False
    return True

def Order(pages: list[int], before: defaultdict[int, list[int]]) -> list[int]:
    beforeInPages: defaultdict[int, list[int]] = defaultdict(list, {k: [v for v in values if v in pages] for k, values in before.items() if k in pages})
    order: list[int] = []
    while len(order) < len(pages):
        for page in pages:
            if page in order:
                continue
            values = beforeInPages[page]
            if all([v in order for v in values]):
                order.append(page)
    return order

totalValid = sum([Order(pages, before)[len(pages)//2] for pages in pagesToProduce if not CheckValid(pages, pageOrderingRules)])
print(totalValid)