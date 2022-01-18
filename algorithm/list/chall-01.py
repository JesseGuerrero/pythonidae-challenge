L = [ 1, 6, 7, 2, 8 ]

def mul3():
    global L
    buffer = []
    for e in L:
        buffer.append(e*3)
    L = buffer

mul3()
print(L)
