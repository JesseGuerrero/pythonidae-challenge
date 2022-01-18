L = [
    "MII-CyberSec",
    "Xathrya",
    "Reversing.ID"
]

def sortByLen():
    global L
    L.sort(key=len)


sortByLen()
print(L)