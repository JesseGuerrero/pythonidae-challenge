L = [ 1, 1, 2, 3, 4, 4, 6, 9 ]

def removeDups():
    global L
    uniques = []
    for e in L:
        if e in uniques:
            continue
        uniques.append(e)
    L = uniques


removeDups()
print(L)