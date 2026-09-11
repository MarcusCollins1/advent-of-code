from time import time
t1 = time()
from math import isqrt

h=0
for b in range(106_700, 123_701, 17):
    for d in range(2, isqrt(b)+1):
        if b % d == 0:
            h+=1
            break
print(h)

print(f"Time Taken: {time()-t1:.2f}s")