D = {
    "key1": 0,
    "key2": 2,
    "key3": 5
}

def deleteKey(key):
    global D
    hasKey = False
    for k in D.keys():
        if key == k:
            hasKey = True
    if hasKey:
        D.pop(key, None)

deleteKey("key2")
print(D)