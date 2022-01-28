'''
Now that I understand hexpairs as a byte type this was
actually pretty quick.
'''

S1 = b'\xd5\x57\x7f\x20\xf5\x41\x60\x2b\xe0\x1c\x40\x01'
S2 = b'\x87\x32\x09\x45'

isS1Short = True
shorterLen = 0
if len(S1) < len(S2):
    shorterLen = len(S1)
else:
    shorterLen = len(S2)
    isS1Short = False

def getLength(wantsLong):
    if wantsLong:
        return len(S2) if isS1Short else len(S1)
    else:
        return len(S1) if isS1Short else len(S2)

listStr = []
x = 0
for i in range(0, getLength(True)):
    if x is getLength(False):
        x = 0
    if isS1Short:
        listStr.append(hex(S2[i] ^ S1[x]))
    else:
        listStr.append(hex(S1[i] ^ S2[x]))
    x+=1

print(listStr)

