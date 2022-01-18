N = 3
L = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]

import math
N = math.ceil(len(L)/N)

splitList = []

i = 1
buff = []
for e in L:
    buff.append(e)
    if(i % N == 0):
        splitList.append(buff)
        buff = []
    i+=1

if len(buff) > 0:
    splitList.append(buff)
    buff = []

print(splitList)