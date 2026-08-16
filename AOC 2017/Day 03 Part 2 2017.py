target = 347991
# target = 368078
#target = 29
from math import sqrt


def pos(index):
    r = int(sqrt(index-1) + 1) // 2
    d = 2*r - 1
    i = index - d*d - 1
    return (r, i-r+1) if i < d else (r-i+d, r) if i < 2*d + 2 else \
        (-r, r-i-1+2*d+2) if i < 3*d + 2 else (i-r-3*d-2, -r)

m, s, i = {(0, 0): 1}, 1, 2
while s <= target:
    (x, y), i = pos(i), i + 1
    m[x, y] = s = sum(m.get((x + j % 3 - 1, y + j//3), 0) for j in range(-3, 6))
print(s)