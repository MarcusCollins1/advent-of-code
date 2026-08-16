from shutil import copy
from os import remove, rename, listdir, getcwd
FOLDER_PATH = (getcwd()+"\\").replace("\\", "/")
SOURCE1 = f"{FOLDER_PATH}Create new day DO NOT USE.py"
SOURCE2 = f"{FOLDER_PATH}Create part 2 DO NOT USE.py"
FOLDERS = []
for folder in listdir(FOLDER_PATH):
    if "." not in folder:
        FOLDERS.append(folder)

for folder in FOLDERS:
    remove(FOLDER_PATH+folder+"\\"+"Create new day.py")
    remove(FOLDER_PATH+folder+"\\"+"Create part 2.py")
    copy(SOURCE1, FOLDER_PATH+folder)
    copy(SOURCE2, FOLDER_PATH+folder)
    rename(FOLDER_PATH+folder+"\\"+"Create new day DO NOT USE.py", FOLDER_PATH+folder+"\\"+"Create new day.py")
    rename(FOLDER_PATH+folder+"\\"+"Create part 2 DO NOT USE.py", FOLDER_PATH+folder+"\\"+"Create part 2.py")