D = {'K': 'V'}

def addKey(key : str) -> None:
    global D
    if (key == 'K'):
        print("Can't add K as key...")
        return
    for k in D.keys():
        if(key == k):
            print("No value can be replaced...")
            return
    D[key] = 'V'

#Main
addKey('K') #Can't add K
addKey('V') #executes
addKey('O') #executes
addKey('V') #No value replaced
