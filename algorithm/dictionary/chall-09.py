L = [ {'id':'1', 'room': '404', 'duration': '4'}, {'id':'2', 'room':'405'} ]


def deleteKey(key):
    global L
    if key == 'id':
        return
    for D in L:
        del D[key]


deleteKey("room")
print(L)