S = "heresy"
D = {}

def occurences():
    global S
    global D
    for c in S:
        hasKey = False
        for k in D.keys():
            if c == k:
                hasKey = True
        if hasKey:
            D[c] = D[c] + 1;
        else:
            D[c] = 1;

occurences()
print(D)