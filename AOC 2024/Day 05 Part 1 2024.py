FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2024/"
FILE_NAME = "Day 05 2024.txt"
# FILE_NAME = "Day 05 2024 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
pageOrderingRules, pagesToProduce = file.read().split("\n\n")
pageOrderingRules = [list(map(int, line.split("|"))) for line in pageOrderingRules.splitlines()]
pagesToProduce = [list(map(int, line.split(","))) for line in pagesToProduce.splitlines()]
file.close()

def CheckValid(pages: list[int], rules: list[list[int]]) -> bool:
    for page1Index, page1 in enumerate(pages):
        for page2 in pages[page1Index+1:]:
            for n1, n2 in rules:
                if n1 == page2 and n2 == page1: return False
    return True

totalValid = sum([pages[len(pages)//2] for pages in pagesToProduce if CheckValid(pages, pageOrderingRules)])
print(totalValid)