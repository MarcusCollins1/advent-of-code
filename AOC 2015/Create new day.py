import webbrowser
from os import getcwd, path
FOLDER_PATH = (getcwd()+"\\").replace("\\", "/")
YEAR = int(FOLDER_PATH.split("/")[-2].replace("AOC ", ""))
day = int(input("What day? "))
day = f"0{day}" if day < 10 else str(day)
FILE_PATHS = [f"Day {day} {YEAR}.txt", f"Day {day} {YEAR} alt.txt", f"Day {day} {YEAR} test.txt"]
PYTHON_FILE_PATH = f"Day {day} Part 1 {YEAR}.py"
if path.isfile(FOLDER_PATH+PYTHON_FILE_PATH):
    x = input("This day already exists are you sure you would like to replace it (y/n)? ").lower()
    if x != "y":
        quit()
for file_path in FILE_PATHS:
    file = open(FOLDER_PATH+file_path, "w")
    file.close()
file = open(FOLDER_PATH+PYTHON_FILE_PATH, "w")
file.write(f'FOLDER_PATH = "{FOLDER_PATH}"\nFILE_NAME = "Day {day} {YEAR}.txt"\nFILE_NAME = "Day {day} {YEAR} alt.txt"\nFILE_NAME = "Day {day} {YEAR} test.txt"\n\nfile = open(FOLDER_PATH + FILE_NAME, "r")\ndata = [x.strip() for x in file.readlines()]\nfile.close()')
file.close()
webbrowser.open(f"https://adventofcode.com/{YEAR}/day/{day}")