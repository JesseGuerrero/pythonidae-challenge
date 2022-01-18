L = [ 3, 0, 4, 9, 7, 9, 7, 2, 9, 4, 1, 4, 2, 5, 5, 7, 4, 0, 6, 9 ]

def addOddIndicesInList() -> int:
    global L
    i = 0
    sum = 0
    for e in L:
        if i % 2 == 1:
           sum+=e
        i+=1
    return sum

print(addOddIndicesInList())
'''
Mine is correct, the challenge answer is wrong.
'''