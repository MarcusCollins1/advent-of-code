import functools

FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 12 2023.txt"
# FILE_NAME = "Day 12 2023 alt.txt"
# FILE_NAME = "Day 12 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

@functools.cache
def count_matches(pattern, size, splits):
    if len(splits) == 0:
        if all(c in '.?' for c in pattern):
            return 1
        return 0

    a = splits[0]
    rest = splits[1:]
    after = sum(rest) + len(rest)
    count = 0
    for before in range(size-after-a+1):
        cand = '.' * before + '#' * a + '.'
        if all(c0 == c1 or c0=='?' for c0,c1 in zip(pattern, cand)):
            count += count_matches(pattern[len(cand):], size-a-before-1, rest)
    return count

answer = 0
for line in data:
    pattern, splits = line.split()
    pattern = "?".join((pattern,) * 5)
    splits = tuple(map(int, splits.split(','))) * 5
    answer += count_matches(pattern, len(pattern), tuple(splits))
print(answer)