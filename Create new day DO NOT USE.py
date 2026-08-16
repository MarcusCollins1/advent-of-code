import webbrowser
from os import getcwd, path
import requests
SESSION_COOKIE = "53616c7465645f5f35878458bf60c7a18538781789c7224950a4dc0fe9571358534700a6e2893d817a75c2bc1525bd50cef795934500df11af009420571e94f4"
FOLDER_PATH = (getcwd()+"\\").replace("\\", "/")
YEAR = int(FOLDER_PATH.split("/")[-2].replace("AOC ", ""))
day = int(input("What day? "))
day = f"0{day}" if day < 10 else str(day)
PYTHON_FILE_PATH = f"Day {day} Part 1 {YEAR}.py"
if path.isfile(FOLDER_PATH+PYTHON_FILE_PATH):
    x = input("This day already exists are you sure you would like to replace it (y/n)? ").lower()
    if x != "y":
        quit()

with open(f"Day {day} {YEAR}.txt", "w") as file:
    url = f"https://adventofcode.com/{YEAR}/day/{int(day)}/input"
    cookies = {"session": SESSION_COOKIE}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    txt = response.text
    if txt[-1] == "\n": txt = txt[:-1]
    file.write(response.text)
with open(f"Day {day} {YEAR} test.txt", "w") as file:
    pass

file = open(FOLDER_PATH+PYTHON_FILE_PATH, "w")
file.write(f'from time import time\nt1 = time()\nFOLDER_PATH = "{FOLDER_PATH}"\nFILE_NAME = "Day {day} {YEAR}.txt"\nFILE_NAME = "Day {day} {YEAR} test.txt"\n\nfile = open(FOLDER_PATH + FILE_NAME, "r")\ndata = [x.strip() for x in file.readlines()]\nfile.close()\n\nprint(f"Time Taken: {{time()-t1:.3f}}s")')
file.close()
webbrowser.open(f"https://adventofcode.com/{YEAR}/day/{int(day)}")