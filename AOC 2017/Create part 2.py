from os import getcwd, path
FOLDER_PATH = (getcwd()+"\\").replace("\\", "/")
YEAR = int(FOLDER_PATH.split("/")[-2].replace("AOC ", ""))
day = int(input("What day? "))
day = f"0{day}" if day < 10 else str(day)
INPUT_FILE_NAME = f"Day {day} Part 1 {YEAR}.py"
OUTPUT_FILE_NAME = f"Day {day} Part 2 {YEAR}.py"

if path.isfile(FOLDER_PATH+OUTPUT_FILE_NAME):
    x = input("This day already has a part 2 are you sure you would like to replace it (y/n)? ").lower()
    if x != "y":
        quit()

input_file = open(FOLDER_PATH+INPUT_FILE_NAME, "r")
output_file = open(FOLDER_PATH+OUTPUT_FILE_NAME, "w")
output_file.write(input_file.read())
input_file.close()
output_file.close()
