L = [{'key': 1}, {'key': 10}, {'key': 5}]


def sort():
    global L, JSON
    L = (sorted(L, key = lambda i: i['key']))


sort()
print(L)