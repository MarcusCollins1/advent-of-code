FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 3 2016.txt"
FILE_NAME = "Day 3 2016 alt.txt"
input_file = open(FOLDER_PATH+FILE_NAME, "r")
triangles = input_file.readlines()
input_file.close()
valid_triangles = 0
for triangle in triangles:
    triangle = sorted(list(map(int, triangle.split())))
    valid_triangles += (triangle[2] < sum(triangle[:2]))
print(valid_triangles)
