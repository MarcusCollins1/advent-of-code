input_file = open("Day 13 2020.txt")
input_file = open("Day 13 2020 alt.txt")
data = input_file.readlines()
earliest = int(data[0].strip())
buses = data[1].strip().split(",")
while "x" in buses:
    buses.remove("x")
buses = list(map(int, buses))

closest = 0
closest_dif = float("inf")

for i in buses:
    curr_time = 0
    while curr_time < earliest:
        curr_time += i
    difference = curr_time-earliest
    if difference < closest_dif:
        closest = i
        closest_dif = difference
        
#print(closest_dif,closest)
print(closest_dif*closest)