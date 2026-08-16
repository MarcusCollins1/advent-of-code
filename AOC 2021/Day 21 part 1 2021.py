# school account
input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 21 2021.txt", "r")
# home account
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 21 2021 alt.txt", "r")
# test
#input_file = open("C:/Users/mjncollins\OneDrive - The Perse School/z/Documents/AOC/AOC 2021/Day 21 2021 test.txt", "r")
start_1, start_2 = list(map(int, input_file.read().replace("Player 1 starting position: ", "").replace("Player 2 starting position: ", "").splitlines()))
score_1, score_2 = 0, 0
MAX_POS = 10
die = 1
MAX_DIE = 100
curr_player = 1
dice_rolls = 0
WIN = 1000
NUM_ROLLS_PER_TURN = 3
while score_1 < WIN and score_2 < WIN:
    curr_move = 0
    for _ in range(NUM_ROLLS_PER_TURN):
        curr_move += die
        if die == MAX_DIE:
            die = 0
        die += 1
        dice_rolls += 1
    if curr_player == 1:    
        for _ in range(curr_move):
            start_1 += 1
            if start_1 > MAX_POS:
                start_1 = 1
        score_1 += start_1
    else:
        for _ in range(curr_move):
            start_2 += 1
            if start_2 > MAX_POS:
                start_2 = 1
        score_2 += start_2
    if curr_player == 1:
        curr_player = 2
    else:
        curr_player = 1
print(min([score_1, score_2])*dice_rolls)
