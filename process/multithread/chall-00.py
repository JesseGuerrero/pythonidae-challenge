from threading import Thread

for name in ["Henry", "Nick", "Trent", "John", "Devin"]:
    Thread(target=print(name)).start()