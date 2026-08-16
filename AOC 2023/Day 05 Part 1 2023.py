FOLDER_PATH = "C:/Users/Marcus Collins/OneDrive/Documents/AOC/AOC 2023/"
FILE_NAME = "Day 05 2023.txt"
# FILE_NAME = "Day 05 2023 alt.txt"
# FILE_NAME = "Day 05 2023 test.txt"

file = open(FOLDER_PATH + FILE_NAME, "r")
data = [x.strip() for x in file.readlines()]
file.close()

class Seed:
    def __init__(self, num:int) -> None:
        self.num = num
        self.soil = num
        self.fertilizer = num
        self.water = num
        self.light = num
        self.temperature = num
        self.humidity = num
        self.location = num
    def SetSoil(self, soil:int) -> None:
        self.soil = soil
        self.fertilizer = soil
        self.water = soil
        self.light = soil
        self.temperature = soil
        self.humidity = soil
        self.location = soil
    def SetFertilizer(self, fertilizer:int) -> None:
        self.fertilizer = fertilizer
        self.water = fertilizer
        self.light = fertilizer
        self.temperature = fertilizer
        self.humidity = fertilizer
        self.location = fertilizer
    def SetWater(self, water:int) -> None:
        self.water = water
        self.light = water
        self.temperature = water
        self.humidity = water
        self.location = water
    def SetLight(self, light:int) -> None:
        self.light = light
        self.temperature = light
        self.humidity = light
        self.location = light
    def SetTemperature(self, temperature:int) -> None:
        self.temperature = temperature
        self.humidity = temperature
        self.location = temperature
    def SetHumidity(self, humidity:int) -> None:
        self.humidity = humidity
        self.location = humidity
    def SetLocation(self, location:int) -> None:
        self.location = location
    
    def __repr__(self) -> str:
        return f"Seed: {self.num}, Soil: {self.soil}, Fertilizer: {self.fertilizer}, Water: {self.water}, Light: {self.light}, Temperature: {self.temperature}, Humidity: {self.humidity}, Location: {self.location}"

lines = []
curr = []
for line in data:
    if line == "":
        lines.append(curr)
        curr = []
    else:
        curr.append(line)
if curr != []:
    lines.append(curr)

target_seeds = list(map(int, lines[0][0].split(" ")[1:]))
seeds = [Seed(x) for x in target_seeds]

# seed-to-soil
curr = [list(map(int, x.split())) for x in lines[1][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.num <= source+length:
            seed.SetSoil(dest+(seed.num-source))

# soil-to-fertilizer
curr = [list(map(int, x.split())) for x in lines[2][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.soil <= source+length:
            seed.SetFertilizer(dest+(seed.soil-source))

# fertilizer-to-water
curr = [list(map(int, x.split())) for x in lines[3][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.fertilizer <= source+length: # type:ignore
            seed.SetWater(dest+(seed.fertilizer-source)) # type:ignore

# water-to-light
curr = [list(map(int, x.split())) for x in lines[4][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.water <= source+length: # type:ignore
            seed.SetLight(dest+(seed.water-source)) # type:ignore

# light-to-temperature
curr = [list(map(int, x.split())) for x in lines[5][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.light <= source+length: # type:ignore
            seed.SetTemperature(dest+(seed.light-source)) # type:ignore

# temperature-to-humidity
curr = [list(map(int, x.split())) for x in lines[6][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.temperature <= source+length: # type:ignore
            seed.SetHumidity(dest+(seed.temperature-source)) # type:ignore

# humidity-to-location
curr = [list(map(int, x.split())) for x in lines[7][1:]]
for dest, source, length in curr:
    for seed in seeds:
        if source <= seed.humidity <= source+length: # type:ignore
            seed.SetLocation(dest+(seed.humidity-source)) # type:ignore

print(min([seed.location for seed in seeds]))