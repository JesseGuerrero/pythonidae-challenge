L = [1,3,"5-9",13]
L2 = []

for e in L:
    if isinstance(e, int):
        L2.append(e)
    if isinstance(e, str):
        l = str(e).split("-")
        for i in range(int(l[0]), int(l[1])+1):
            L2.append(i)

print(L2)