FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 17 2022.txt"
FILE_NAME = "Day 17 2022 alt.txt"
FILE_NAME = "Day 17 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

class Shape:
    def __init__(self, width, height, positions):
        self.width = width
        self.height = height
        self.positions = positions
        self.min_x, self.max_x = 2, 1+self.width

NUM_SHAPES_NEEDED = 2022

movements = list(data[0].strip())
shapes = [Shape(4, 1, [(2, 0), (3, 0), (4, 0), (5, 0)]), Shape(3, 3, [(3, 2), (2, 1), (3, 1), (4, 1), (3, 0)]), Shape(3, 3, [(4, 2), (4, 1), (2, 0), (3, 0), (4, 0)]), Shape(1, 4, [(2, 3), (2, 2), (2, 1), (2, 0)]), Shape(2, 2, [(2, 1), (3, 1), (2, 0), (3, 0)])]
num_shapes_placed = 0
layers = []
shape_index = 0
movement_index = 0

while True:
    # create new shape
    layers += [list("......."), list("......."), list(".......")]
    shape = shapes[shape_index]
    shape_index = (shape_index+1)%len(shapes)
    for y in range(shape.height):
        curr = []
        for x in range(7):
            curr.append("@" if (x, y) in shape.positions else ".")
        layers.append(curr)
    while True:
        # move shape
        movement = movements[movement_index]
        for line in layers[::-1]:
            print(*line, sep="")
        print()
        # move right
        if movement == ">" and shape.max_x < 6:
            shape.max_x += 1
            temp = []
            for y in range(shape.height):
                curr = layers.pop(-1)
                curr = ["."]+curr[:-1]
                temp.append(curr)
            temp = temp[::-1]
            layers += temp
        # move left
        elif movement == "<" and shape.min_x > 0:
            shape.max_x -= 1
            temp = []
            for y in range(shape.height):
                curr = layers.pop(-1)
                curr = curr[1:]+["."]
                temp.append(curr)
            temp = temp[::-1]
            layers += temp
        movement_index = (movement_index + 1)%len(movements)

        for line in layers[::-1]:
            print(*line, sep="")
        print()

        # move down
        for y in range(-shape.height, 0):
            for x in range(len(layers[y])):
                if layers[y][x] == "@":
                    layers[y-1][x] = "@"
                    layers[y][x] = "."
        layers.pop(-1)
        for line in layers[::-1]:
            print(*line, sep="")
        print()
        # Check if stopped
        stopped = False
        # check if touching ground
        for item in layers[0]:
            if item == "@":
                stopped = True
                break
        # check if touching rock
        if not stopped:
            for y in range(-shape.height, 0):
                for x in range(len(layers[y])):
                    stopped = layers[y][x] == "@" and layers[y-1][x] == "#"
                    if stopped:
                        break
                if stopped:
                    break
        
        if stopped:
            for y in range(-shape.height, 0):
                for i, item in enumerate(layers[y]):
                    layers[y][i] = "#" if item == "@" else layers[y][i]
            num_shapes_placed += 1
            break
    if num_shapes_placed == NUM_SHAPES_NEEDED:
        break
print(len(layers)-1)
