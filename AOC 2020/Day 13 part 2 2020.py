input_file = open("Day 13 2020.txt")
input_file = open("Day 13 2020 alt.txt")
data = input_file.readlines()
earliest = int(data[0].strip())
temp_buses = data[1].strip().split(",")
buses = []
for bus in temp_buses:
    if bus == "x":
        buses.append(bus)
    else:
        buses.append(int(bus))

remainder = []
for i in range(len(buses)):
    if buses[i] != "x":
        remainder.append(buses[i] - i % buses[i])
    else:
        remainder.append("x")

a = buses[0]
curr_tot = 0
for i in range(1,len(buses)):
    if buses[i] != "x":
        b = int(buses[i])
        while curr_tot % b != remainder[i]:
            curr_tot += a
        a *= b
print(curr_tot)