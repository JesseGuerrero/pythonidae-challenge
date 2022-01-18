L = [ 4, 5, 1, 6, 7, 2, 8, 9, 1, 6, 9 ]

def showTop() -> list:
    global L
    maxNum = max(L)

    newList = []
    for i in L:
        if i == maxNum:
            newList.append(i)
    return newList

print(showTop())

