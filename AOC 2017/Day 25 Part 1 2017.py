from time import time
t1 = time()

state = "A"
ones = set()
index = 0

test = False
num = 6 if test else 12_302_209

for _ in range(num):
    if state == "A":
        if index in ones:
            ones.remove(index)
            index -= 1
            state = "B" if test else "D"
        else:
            ones.add(index)
            index += 1
            state = "B"
    elif state == "B":
        if index in ones:
            if not test: ones.remove(index)
            index += 1
            state = "A" if test else "F"
        else:
            ones.add(index)
            index += -1 if test else 1
            state = "A" if test else "C"
    elif state == "C":
        if index in ones:
            # ones.add(index)
            index -= 1
            state = "A"
        else:
            ones.add(index)
            index -= 1
            state = "C"
    elif state == "D":
        if index in ones:
            # ones.add(index)
            index += 1
            state = "A"
        else:
            # ones.remove(index)
            index -= 1
            state = "E"
    elif state == "E":
        if index in ones:
            ones.remove(index)
            index += 1
            state = "B"
        else:
            ones.add(index)
            index -= 1
            state = "A"
    elif state == "F":
        if index in ones:
            ones.remove(index)
            index += 1
            state = "E"
        else:
            # ones.remove(index)
            index += 1
            state = "C"

print(len(ones))
print(f"Time Taken: {time()-t1:.2f}s")