import re
from collections import defaultdict
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 7 2018.txt"
FILE_NAME = "Day 7 2018 alt.txt"
# FILE_NAME = "Day 7 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

tasks = set()
order = defaultdict(set)
for line in data:
    match = re.search(r'Step (\w) must be finished before step (\w) can begin.', line)
    if match:
        order[match.group(1)].add(match.group(2))
        tasks.add(match.group(1))
        tasks.add(match.group(2))

done = set()
seconds = 0
counts = [0]*5
work = ['']*5
while True:
    for i, count in enumerate(counts):
        if count == 1:
            done.add(work[i])
        counts[i] = max(0, count-1)
    
    while 0 in counts:
        i = counts.index(0)
        candidates = [x for x in tasks if order[x] <= done]
        if not candidates:
            break
        task = min(candidates)
        tasks.remove(task)
        counts[i] = ord(task)-ord('A')+61
        work[i] = task
    if sum(counts) == 0:
        break
    seconds += 1
print(seconds)