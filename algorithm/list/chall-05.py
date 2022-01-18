L = [ 1, 1, 2, 3, 4, 4, 6, 9 ]
U = []

def getUniques():
    global L, U
    dups = []
    for e in L:
        if e in U:
            dups.append(e)
            continue
        U.append(e)
    for d in dups:
        U.remove(d)

getUniques()
print(U)