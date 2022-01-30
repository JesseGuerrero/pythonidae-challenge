from threading import Thread, get_native_id

def printNameAndID(name):
    print("my name is " + name + " and my id is " + str(get_native_id()))

for name in ["Henry", "Nick", "Trent", "John", "Devin"]:
    Thread(target=printNameAndID, args=(name,)).start()