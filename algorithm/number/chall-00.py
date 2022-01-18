A = 15
B = 27
GCD = 0

def findGCD():
    global A, B, GCD
    buff = B*1
    B = A % B
    A = buff*1
    if B == 0:
        GCD = A*1
        return
    findGCD()


findGCD()
print(GCD)