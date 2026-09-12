FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 15 2022.txt"
# FILE_NAME = "Day 15 2022 alt.txt"
# FILE_NAME = "Day 15 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

MAX_XY = 20
MAX_XY = 4000000

class Sensor:
    def __init__(self, x, y, beaconx, beacony):
        self.x = x
        self.y = y
        self.beaconx = beaconx
        self.beacony = beacony
        self.beaconDistance = abs(self.x-self.beaconx) + abs(self.y-self.beacony)

sensors = []
sensor_positions = set()
beacon_positions = set()
for line in data:
    line = list(map(int, line.strip().replace("Sensor at x=", "").replace(" y=", "").replace(": closest beacon is at x=", ",").replace(" y=", "").split(",")))
    current_sensor = Sensor(line[0], line[1], line[2], line[3])
    sensors.append(Sensor(line[0], line[1], line[2], line[3]))
    sensor_positions.add((line[0], line[1]))
    beacon_positions.add((line[2], line[3]))
print("Processed sensors")

for y in range(0, MAX_XY+1):
    if y % 100000 == 0:
        print(y)
    intervals = []
    for sensor in sensors:
        if sensor.beaconDistance-abs(sensor.y-y) < 0:
            continue
        min_x, max_x = max([sensor.x-(sensor.beaconDistance-abs(sensor.y-y)), 0]), min([sensor.x+(sensor.beaconDistance-abs(sensor.y-y)), MAX_XY])
        intervals.append([min_x, max_x])
    intervals = sorted(intervals)
    flag = True
    max_x = 0
    for i in range(len(intervals)):
        if max_x < intervals[i][0]:
            flag = False
            break
        max_x = max([max_x, intervals[i][1]])
    if max_x != MAX_XY or not flag:
        print(max_x+1, y)
        print((max_x+1)*4000000+y)
        break
