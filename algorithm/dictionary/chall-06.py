D = {
    "key1": 0,
    "key2": 2,
    "key3": 5,
    "key4": 5,
}

def deleteWithValue(value):
    global D
    keysToDelete = []
    for k, v in D.items():
        if D[k] == value:
            keysToDelete.append(k)
    for k in keysToDelete:
        D.pop(k, None)
deleteWithValue(5)
print(D)