N = [ "black", "red", "maroon", "yellow" ]
C = [ "#000000", "#FF0000", "#800000", "#FFFF00" ]

listDict = []

def makeDict():
    global N, C, listDict
    for i in range(0, len(N)):
        dict = {}
        dict['name'] = N[i]
        dict['code'] = C[i]
        listDict.append(dict)




makeDict()
print(listDict)