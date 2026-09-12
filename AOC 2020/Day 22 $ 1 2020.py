input_file = open("Day 22 2020.txt")
input_file = open("Day 22 2020 alt.txt")
data = input_file.readlines()
input_file.close()
players = [[]]
for line in data[1:]:
    line = line.strip()
    if line == "":
        players.append([])
    elif line == "Player 2:":
        continue
    else:
        players[-1].append(int(line))

player_1, player_2 = players

while player_1 and player_2:
    p1Card, p2Card = player_1.pop(0), player_2.pop(0)
    if p1Card > p2Card:
        player_1.append(p1Card)
        player_1.append(p2Card)
    elif p2Card > p1Card:
        player_2.append(p2Card)
        player_2.append(p1Card)

total = 0
winner = player_1 if player_1 else player_2
for i, num in enumerate(winner[::-1]):
    total+= num*(i+1)
print(total)