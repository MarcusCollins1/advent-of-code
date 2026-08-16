import re
from collections import defaultdict, Counter
FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2018/"
FILE_NAME = "Day 4 2018.txt"
# FILE_NAME = "Day 4 2018 alt.txt"
# FILE_NAME = "Day 4 2018 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Entry:
    def __init__(self, year, month, day, hour, minute, action):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.action = action
    def __str__(self) -> str:
        return f"{self.year}, {self.month}, {self.day}, {self.hour}, {self.minute}, {self.action}"

entries = []

for line in data:
    matches = re.search(r'(\d+)-(\d+)-(\d+)\s(\d+).(\d+).\s(.+)$', line)
    year, month, day, hour, min, action = matches.groups()
    entries.append(Entry(year, month, day, hour, min, action))
entries = sorted(entries, key=lambda x: (x.year, x.month, x.day, x.hour, x.minute))


guards = defaultdict(list)

currGuard = 0
start_min = 0
for entry in entries:
    if entry.action.startswith("Guard"):
        currGuard = int(entry.action.replace("Guard #", "").split()[0])
    elif entry.action == "falls asleep":
        start_min = entry.minute
    elif entry.action == "wakes up":
        guards[currGuard] += list(range(start_min, entry.minute))


guard_min = dict()

for guard, sleeps in guards.items():
    guard_min[guard] = Counter(sleeps).most_common()[0][1]



guard = max(guard_min, key=guard_min.get)
print(guard * Counter(guards[guard]).most_common()[0][0])