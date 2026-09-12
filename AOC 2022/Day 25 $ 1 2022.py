FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 25 2022.txt"
# FILE_NAME = "Day 25 2022 alt.txt"
# FILE_NAME = "Day 25 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

s_d = {"2":2, "1":1, "0":0, "-":-1, "=":-2}

def snafu_dec(num:str) -> int:
    total = 0
    for i, digit in enumerate(num[::-1]):
        total += s_d[digit]*5**i
    return total

def dec_snafu(num:int) -> str:
    snafu_digit = {v%5:k for k,v in s_d.items()}
    snafu_number = ""
    while num != 0:
        remainder = num%5
        digit = snafu_digit[remainder]
        snafu_number = digit + snafu_number
        value = s_d[digit]
        num = (num-value)//5
    return snafu_number

total = 0
for num in data:
    total += snafu_dec(num.strip())

print(dec_snafu(total))