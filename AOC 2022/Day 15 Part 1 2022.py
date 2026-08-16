FOLDER_PATH = "C:/Users/mjncollins/OneDrive - The Perse School/z/Documents/AOC/AOC 2022/"
FILE_NAME = "Day 15 2022.txt"
# FILE_NAME = "Day 15 2022 alt.txt"
# FILE_NAME = "Day 15 2022 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = file.readlines()
file.close()

DESIRED_ROW = 10
DESIRED_ROW = 2000000

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
    if DESIRED_ROW in range(current_sensor.y-current_sensor.beaconDistance, current_sensor.y+current_sensor.beaconDistance+1):
        sensors.append(Sensor(line[0], line[1], line[2], line[3]))
        sensor_positions.add((line[0], line[1]))
        beacon_positions.add((line[2], line[3]))
print("Processed sensors")

not_beacon_positions = set()
for sensor in sensors:
    for x1 in range(-sensor.beaconDistance+abs(DESIRED_ROW-sensor.y), sensor.beaconDistance-abs(DESIRED_ROW-sensor.y)+1):
        x2 = x1+sensor.x
        if (x2, DESIRED_ROW) not in sensor_positions and (x2, DESIRED_ROW) not in beacon_positions:
            not_beacon_positions.add((x2, DESIRED_ROW))
print("Found positions where beacons are not")

print(f"There are {len(not_beacon_positions)} places where beacons cannot be on {DESIRED_ROW}")