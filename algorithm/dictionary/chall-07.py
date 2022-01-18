K = [ "name", "hp", "mp" ]
V = [ "xathrya", "100", "32" ]

D = {

}

def createDict():
    global K, V, D
    for i in range(0, len(K)):
        D[K[i]] = V[i]

createDict()
print(D)