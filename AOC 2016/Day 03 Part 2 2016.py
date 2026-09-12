FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2016/"
FILE_NAME = "Day 3 2016.txt"
FILE_NAME = "Day 3 2016 alt.txt"
input_file = open(FOLDER_PATH+FILE_NAME, "r")
data = input_file.readlines()
input_file.close()
triangles = []
for i in data:
    triangles.append(i.split())
valid_triangles = 0
for index in range(len(triangles)):
    num = index % 3
    triangle = sorted(list(map(int, [triangles[index-num][num], triangles[index+1-num][num], triangles[index+2-num][num]])))
    valid_triangles += (triangle[2] < sum(triangle[:2]))
print(valid_triangles)
