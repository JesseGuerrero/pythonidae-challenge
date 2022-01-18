import random

L = [1,2,3,4,5,6,7,8,9]

def randomNum() -> int:
    global L
    return L[random.randint(0, len(L)-1)]

def randomNumPop() -> int:
    global L
    return L.pop(random.randint(0, len(L)-1))

print(randomNum())
print(randomNumPop())
print(L)