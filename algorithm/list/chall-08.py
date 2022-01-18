L = [ [2, 4, 3], [1, 5, 6], [9], [7, 9] ]

def makeOneDimension():
    global L
    oneD = []
    for l in L:
        for e in l:
            oneD.append(e)
    L = oneD

makeOneDimension()
print(L)
