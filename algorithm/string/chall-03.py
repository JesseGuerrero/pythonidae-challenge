N = 10
S = 5
E = 8

import random as ran
arrElements = []
for i in range(0, N):
    if i >= 5 and i <= 8:
        arrElements.append(ran.randint(0, 15))
    else:
        arrElements.append(0)
arr = bytearray(arrElements)
print(arr)
