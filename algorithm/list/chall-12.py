L = [ 1, 3, 5, 7, 9 ]
M = [ 2, 4, 6 ]
zippedList = []

length = 0
if len(L) < len(M):
    length = len(L)
else:
    length = len(M)

for i in range(0, length):
    zippedList.append((L[i], M[i]))

print(zippedList)